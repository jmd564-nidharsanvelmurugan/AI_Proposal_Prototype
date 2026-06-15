import os
import json
from datetime import datetime
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional

# Your existing retrieval helpers
from a_metadata_retrieval import (
    get_top_matching_proposals,
    get_parent_chunks_by_document_ids,
    get_child_chunks_by_ids
)
from b_subsection_filter import (
    save_to_json,
    ensure_results_folder,
    get_filtered_chunks_by_semantic_query
)

load_dotenv()

# ------------------------------------------------------------
# Metadata schema (must match your DB columns)
# ------------------------------------------------------------
class ProposalMetadata(BaseModel):
    business_offering: str
    solution: str
    region: str
    project_type: str
    commercial_use_case: str
    technical_use_case: str
    business_model: str
    existing_infra: str
    pe_relationship: str

# ------------------------------------------------------------
# LLM setup (Azure or Groq)
# ------------------------------------------------------------
USE_AZURE = os.getenv("USE_AZURE", "true").lower() == "true"
if USE_AZURE:
  llm = AzureChatOpenAI(
      azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
      api_key=os.getenv("AZURE_OPENAI_KEY"),
      azure_deployment=os.getenv("gpt-5"),
      api_version="2024-02-15-preview",
      temperature=0,
  )
else:
    from langchain_groq import ChatGroq
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY")
    )

metadata_llm = llm.with_structured_output(ProposalMetadata)

# ------------------------------------------------------------
# Metadata extraction prompt (embedded)
# ------------------------------------------------------------
metadata_prompt = ChatPromptTemplate.from_template("""
You are an expert Proposal Discovery Analyst.

Analyze the questionnaire responses and classify the engagement.

Return ONLY values from the allowed lists below.

Business Offering:
- SaaS
- Financial Services
- Field Services
- Professional Services

Solution:
- Core Reporting
- Due Diligence
- Data Advisory
- Value Creation
- Exit Prep

Region:
- US
- UK
- Europe

Project Type:
- Design and Discovery
- Build
- Both

Commercial Use Case:
- Revenue Bridge
- Pipeline
- Churn
- Upsell/Cross Sell
- Operational Reporting

Technical Use Case:
- Data Platform
- Gen AI
- Data Science
- Full-Stack Development

Business Model:
- B2B
- B2C
- D2C
- C2C

Existing Infra:
- Yes
- No

PE Relationship:
- PE Firm
- PE Portco

Rules:
- Select the closest matching value.
- Never invent values outside the lists.
- Infer values from the questionnaire.
- Return structured output only.

Questionnaire:
{questionnaire}
""")

metadata_chain = metadata_prompt | metadata_llm

# ------------------------------------------------------------
# Helper: load questionnaire robustly
# ------------------------------------------------------------
def load_questionnaire(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read().strip()
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        # Try JSON Lines (multiple objects)
        lines = [line.strip() for line in content.splitlines() if line.strip()]
        objects = []
        for line in lines:
            try:
                objects.append(json.loads(line))
            except:
                pass
        if objects:
            return objects
        raise ValueError(f"Could not parse questionnaire file")

# ------------------------------------------------------------
# Helper: generate a semantic retrieval query for Overview section
# ------------------------------------------------------------
def generate_section_query(questionnaire_str: str, metadata: dict, section_name: str) -> str:
    prompt = ChatPromptTemplate.from_template("""
You are an expert proposal retrieval specialist.

Extract 3–5 key phrases from the questionnaire that best represent the core
**current state, systems, teams, and infrastructure** for the **{section_name}** section.

Questionnaire:
{questionnaire_str}

Metadata:
{metadata}

Rules:
- Return ONLY the concatenated phrase (spaces between words, no quotes).
- Maximum 12 words.
- Focus on concrete: affected teams, systems/platforms, data sources, infrastructure.
- Avoid generic words like "current" unless specific.

Example for Overview:
"data technology marketing teams Salesforce QuickBooks Azure Fabric Power BI"

Return only the retrieval phrase.
""")
    chain = prompt | llm
    response = chain.invoke({
        "questionnaire_str": questionnaire_str,
        "metadata": json.dumps(metadata, indent=2),
        "section_name": section_name
    })
    return response.content.strip()

# ------------------------------------------------------------
# Helper: generate Overview content (with previous context)
# ------------------------------------------------------------
def generate_overview_content(
    questionnaire_str: str,
    metadata: dict,
    retrieved_chunks: dict,
    previous_sections: Optional[dict] = None
) -> str:
    # Format retrieved knowledge
    knowledge_text = "NO_KNOWLEDGE_AVAILABLE"
    if retrieved_chunks and "semantic_filtered" in retrieved_chunks:
        chunks = retrieved_chunks["semantic_filtered"]
        if chunks:
            texts = []
            for chunk in chunks[:5]:
                text = chunk.get("text") or chunk.get("actual_text_data") or ""
                if text:
                    if len(text) > 800:
                        text = text[:800] + "..."
                    texts.append(f"• {text}")
            if texts:
                knowledge_text = "\n".join(texts)

    # Format previous sections (e.g., Business Context)
    prev_context = ""
    if previous_sections:
        prev_context = "\nPreviously written sections (do NOT repeat facts from them):\n"
        for name, content in previous_sections.items():
            prev_context += f"\n--- {name} ---\n{content[:500]}...\n"

    prompt = ChatPromptTemplate.from_template("""
You are a senior consulting proposal writer specializing in **Overview** sections.

CLIENT QUESTIONNAIRE:
{questionnaire_str}

METADATA:
{metadata}

RETRIEVED KNOWLEDGE (supporting evidence):
{knowledge}

{prev_context}

INSTRUCTIONS FOR OVERVIEW SECTION:
- Start with "# Overview" as a level‑1 heading (Markdown).
- Write 2–3 short paragraphs (max 250 words total).
- Use the questionnaire as the ONLY source of client‑specific facts.
- Focus on the **current state** of the client's operations, including:
  * Affected teams and processes
  * Systems and platforms currently being used
  * Reporting and analytics tools that exist today
  * Data sources and databases involved
  * Existing cloud/platform infrastructure
  * Current manual processes (if mentioned)
  * Integration challenges (if mentioned)
- Do NOT repeat facts already covered in previous sections (like Business Context).
- Keep language factual, direct, and free of generic industry commentary.
- If the questionnaire does not mention something, leave it out.

CRITICAL: Do NOT mention problems, solutions, or future state – just describe what exists today.

CONTENT:
""")

    chain = prompt | llm
    response = chain.invoke({
        "questionnaire_str": questionnaire_str,
        "metadata": json.dumps(metadata, indent=2),
        "knowledge": knowledge_text,
        "prev_context": prev_context
    })
    return response.content.strip()

# ------------------------------------------------------------
# Main execution for Overview
# ------------------------------------------------------------
def main():
    # 1. Load questionnaire
    questionnaire_file = "questionnaire.json"
    if not os.path.exists(questionnaire_file):
        raise FileNotFoundError(f"File '{questionnaire_file}' not found.")
    questionnaire = load_questionnaire(questionnaire_file)
    questionnaire_str = json.dumps(questionnaire)

    # 2. Extract metadata
    metadata = metadata_chain.invoke({"questionnaire": questionnaire_str})
    metadata_dict = metadata.model_dump()
    print("\n✅ Metadata extracted:")
    print(json.dumps(metadata_dict, indent=2))

    # 3. Load previous Business Context content
    previous_sections = {}
    bc_file = "../A_Business_Context/x_results/business_context_20260612_151414.txt"
    if os.path.exists(bc_file):
        with open(bc_file, "r", encoding="utf-8") as f:
            previous_sections["Business Context"] = f.read()
        print("\n📄 Loaded previous Business Context for context.")
    else:
        print("\n⚠️ No previous Business Context found – generating without it.")

    # 4. Get top matching proposals and child chunks for "Overview"
    section_name = "Overview"
    user_input = {
        "solution": [metadata.solution],
        "business_offering": [metadata.business_offering],
        "commercial_use_case": [metadata.commercial_use_case],
        "project_type": [metadata.project_type],
        "existing_infra": [metadata.existing_infra],
        "business_model": [metadata.business_model],
        "region": [metadata.region]
    }
    top_proposals = get_top_matching_proposals(user_input, top_n=5)
    document_ids = [p["document_id"] for p in top_proposals]

    parent_chunks = get_parent_chunks_by_document_ids(document_ids, section_name)
    all_child_ids = []
    for parent in parent_chunks:
        for child_ref in parent.get("child_chunks", []):
            if child_ref.get("id"):
                all_child_ids.append(child_ref["id"])
    all_child_ids = list(set(all_child_ids))

    # 5. Generate semantic query for Overview
    section_query = generate_section_query(questionnaire_str, metadata_dict, section_name)
    print(f"\n🔍 Generated query: {section_query}")

    # 6. Retrieve relevant chunks
    filtered_results = get_filtered_chunks_by_semantic_query(
        child_ids=all_child_ids,
        query=section_query,
        top_k=10
    )

    # 7. Generate content (with previous context)
    content = generate_overview_content(
        questionnaire_str=questionnaire_str,
        metadata=metadata_dict,
        retrieved_chunks=filtered_results,
        previous_sections=previous_sections if previous_sections else None
    )

    print("\n" + "=" * 60)
    print("OVERVIEW")
    print("=" * 60)
    print(content)

    # 8. Save outputs
    ensure_results_folder()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_to_json(metadata_dict, f"metadata_{timestamp}.json")
    save_to_json(filtered_results, f"filtered_chunks_{timestamp}.json")
    with open(f"x_results/overview_{timestamp}.txt", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n✅ Saved to x_results/overview_{timestamp}.txt")

if __name__ == "__main__":
    main()