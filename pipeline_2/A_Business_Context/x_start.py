import os
import json
from datetime import datetime
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List

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
# Metadata schema
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
# Helper: generate a semantic retrieval query for the section
# ------------------------------------------------------------
def generate_section_query(questionnaire: str, metadata: dict, section_name: str) -> str:
    prompt = ChatPromptTemplate.from_template("""
You are an expert proposal retrieval specialist.

Extract 3–5 key phrases from the questionnaire that best represent the core
context, industry, and business drivers for the **{section_name}** section.

Questionnaire:
{questionnaire}

Metadata:
{metadata}

Rules:
- Return ONLY the concatenated phrase (spaces between words, no quotes).
- Maximum 12 words.
- Focus on concrete business context: industry, products, strategic drivers.
- Avoid generic words like "improve", "enhance", "data" unless specific.

Example for Business Context:
"wealth management financial advisory L2A pipeline reporting transformation"

Return only the retrieval phrase.
""")
    chain = prompt | llm
    response = chain.invoke({
        "questionnaire": questionnaire,
        "metadata": json.dumps(metadata, indent=2),
        "section_name": section_name
    })
    return response.content.strip()

# ------------------------------------------------------------
# Helper: generate Business Context content
# ------------------------------------------------------------
def generate_business_context_content(
    questionnaire: str,
    metadata: dict,
    retrieved_chunks: dict
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

    prompt = ChatPromptTemplate.from_template("""
You are a senior consulting proposal writer specializing in **Business Context** sections.

CLIENT QUESTIONNAIRE:
{questionnaire}

METADATA:
{metadata}

RETRIEVED KNOWLEDGE (supporting evidence):
{knowledge}

INSTRUCTIONS FOR BUSINESS CONTEXT SECTION:
- Start with "# Business Context" as a level‑1 heading (Markdown).
- Write 2–3 short paragraphs (max 250 words).
- Use the questionnaire as the ONLY source of client‑specific facts.
- Retrieved knowledge is for supporting evidence only – do not copy company names from it.
- Keep language professional, direct, and free of generic industry commentary.
- Do NOT use bullet points or subsection headings.
- Focus on: who the client is, what they do, what they want to improve.
- If the questionnaire does not mention something, leave it out.

CRITICAL: If retrieved knowledge is "NO_KNOWLEDGE_AVAILABLE", still write the section using only the questionnaire.

CONTENT:
""")

    chain = prompt | llm
    response = chain.invoke({
        "questionnaire": questionnaire,
        "metadata": json.dumps(metadata, indent=2),
        "knowledge": knowledge_text
    })
    return response.content.strip()

# ------------------------------------------------------------
# Main execution
# ------------------------------------------------------------
def main():
    # Load questionnaire from a file – ensure it's a single valid JSON object
    questionnaire_file = "questionnaire.json"
    if not os.path.exists(questionnaire_file):
        raise FileNotFoundError(f"Questionnaire file '{questionnaire_file}' not found.")
    
    with open(questionnaire_file, "r", encoding="utf-8") as f:
        questionnaire = json.load(f)   # must be a single JSON object, not multiple

    # 1. Extract metadata
    metadata = metadata_chain.invoke({"questionnaire": questionnaire})
    metadata_dict = metadata.model_dump()
    print("\n✅ Metadata extracted:")
    print(json.dumps(metadata_dict, indent=2))

    # 2. Get top matching proposals and child chunks for "Business Context"
    section_name = "Business Context"
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

    # 3. Generate section query (pass questionnaire as JSON string)
    questionnaire_str = json.dumps(questionnaire)
    section_query = generate_section_query(questionnaire_str, metadata_dict, section_name)
    print(f"\n🔍 Generated query: {section_query}")

    # 4. Retrieve relevant chunks using that query
    filtered_results = get_filtered_chunks_by_semantic_query(
        child_ids=all_child_ids,
        query=section_query,
        top_k=10
    )

    # 5. Generate content
    content = generate_business_context_content(
        questionnaire=questionnaire_str,
        metadata=metadata_dict,
        retrieved_chunks=filtered_results
    )

    print("\n" + "=" * 60)
    print("BUSINESS CONTEXT")
    print("=" * 60)
    print(content)

    # 6. Save outputs
    ensure_results_folder()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_to_json(metadata_dict, f"metadata_{timestamp}.json")
    save_to_json(filtered_results, f"filtered_chunks_{timestamp}.json")
    with open(f"x_results/business_context_{timestamp}.txt", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n✅ Saved to x_results/business_context_{timestamp}.txt")

if __name__ == "__main__":
    main()