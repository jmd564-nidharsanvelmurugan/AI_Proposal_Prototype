import os
import json
import glob
from datetime import datetime
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional

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

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

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

def load_questionnaire(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read().strip()
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        lines = [line.strip() for line in content.splitlines() if line.strip()]
        objects = []
        for line in lines:
            try:
                objects.append(json.loads(line))
            except:
                pass
        if objects:
            return objects
        raise ValueError("Could not parse questionnaire file")

def get_latest_section_file(section_name: str) -> Optional[str]:
    folder_map = {
        "Objectives": ("../C_Objectives/x_results", "objectives"),
        "Deliverables": ("../D_Deliverables/x_results", "deliverables"),
    }
    if section_name not in folder_map:
        return None
    folder, prefix = folder_map[section_name]
    pattern = os.path.join(folder, f"{prefix}_*.txt")
    files = glob.glob(pattern)
    if not files:
        return None
    return max(files, key=os.path.getmtime)

def generate_section_query(questionnaire_str: str, metadata: dict, section_name: str) -> str:
    prompt = ChatPromptTemplate.from_template("""
You are an expert proposal retrieval specialist.
Extract 3–5 key phrases from the questionnaire that best represent the core
**activities, phases, and methodology** for the **{section_name}** section.

Questionnaire:
{questionnaire_str}

Metadata:
{metadata}

Rules:
- Return ONLY the concatenated phrase (spaces between words, no quotes).
- Maximum 12 words.
- Focus on concrete activities: discovery workshops, data model design, power bi build, testing.
- Avoid generic words.

Example for Approach:
"discovery workshops data model design power bi build testing deployment"

Return only the retrieval phrase.
""")
    chain = prompt | llm
    response = chain.invoke({
        "questionnaire_str": questionnaire_str,
        "metadata": json.dumps(metadata, indent=2),
        "section_name": section_name
    })
    return response.content.strip()

def generate_approach_content(
    questionnaire_str: str,
    metadata: dict,
    retrieved_chunks: dict,
    previous_sections: dict
) -> str:
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

    # Include only Objectives and Deliverables as context
    relevant_prev = ""
    for name in ["Objectives", "Deliverables"]:
        if name in previous_sections:
            short = previous_sections[name][:500] + "..." if len(previous_sections[name]) > 500 else previous_sections[name]
            relevant_prev += f"\n--- {name} ---\n{short}\n"

    # Trimmed prompt as defined above
    prompt = ChatPromptTemplate.from_template("""
You are a senior consulting proposal writer specializing in **Approach** sections.

CLIENT QUESTIONNAIRE:
{questionnaire_str}

METADATA:
{metadata}

RETRIEVED KNOWLEDGE (supporting evidence):
{knowledge}

{prev_context}

INSTRUCTIONS FOR APPROACH SECTION:

- Start with "# Approach" as a level‑1 heading (Markdown).

- Write **two introductory paragraphs**:
  * First paragraph: Describe how the engagement is tailored to the client's unique challenges and opportunities (use client name, industry, business model, and the specific focus – e.g., building from scratch, using Gen AI for churn).
  * Second paragraph: Explain the structured, phased methodology and how it ensures alignment with client needs.

- Then, for each phase, use the following **exact format**:

  **Phase X: [Phase Name], Duration: X weeks, Timeline: Week Y to Week Z**

  **Summary:** [One sentence describing the phase's purpose and what it establishes.]

  **Activities:**  
  - [Activity 1]  
  - [Activity 2]  
  - [Activity 3]  
  (Add 4–6 bullet points per phase. Use the timeline from the questionnaire if available; otherwise infer logical durations.)

- After the last phase, write a **concluding paragraph** that reinforces the value of the phased approach (e.g., "This structured, phased approach ensures that [Client Name]’s platform and capabilities are developed with precision, agility, and a clear focus on delivering measurable business outcomes aligned with stakeholder expectations.").

- Use the questionnaire as the ONLY source for timelines, technologies (e.g., cloud, ETL, Gen AI), and deliverables. Do NOT repeat objectives or outcomes.

CRITICAL: Follow the exact formatting – headings, bold phase lines, "Summary:", "Activities:", and bullet points with "-". Use blank lines between sections for readability.

CONTENT:
""")
    chain = prompt | llm
    response = chain.invoke({
        "questionnaire_str": questionnaire_str,
        "metadata": json.dumps(metadata, indent=2),
        "prev_context": relevant_prev,
        "knowledge": knowledge_text
    })
    return response.content.strip()

def main():
    questionnaire_file = "questionnaire.json"
    if not os.path.exists(questionnaire_file):
        raise FileNotFoundError(f"File '{questionnaire_file}' not found.")
    questionnaire = load_questionnaire(questionnaire_file)
    questionnaire_str = json.dumps(questionnaire)

    metadata = metadata_chain.invoke({"questionnaire": questionnaire_str})
    metadata_dict = metadata.model_dump()
    print("\n✅ Metadata extracted:")
    print(json.dumps(metadata_dict, indent=2))

    # Load only Objectives and Deliverables
    previous_sections = {}
    for section_name in ["Objectives", "Deliverables"]:
        file_path = get_latest_section_file(section_name)
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                previous_sections[section_name] = f.read()
            print(f"📄 Loaded previous '{section_name}' from {file_path}")
        else:
            print(f"⚠️ No previous '{section_name}' file found – generating without it.")

    section_name = "Approach"
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

    section_query = generate_section_query(questionnaire_str, metadata_dict, section_name)
    print(f"\n🔍 Generated query: {section_query}")

    filtered_results = get_filtered_chunks_by_semantic_query(
        child_ids=all_child_ids,
        query=section_query,
        top_k=10
    )

    content = generate_approach_content(
        questionnaire_str=questionnaire_str,
        metadata=metadata_dict,
        retrieved_chunks=filtered_results,
        previous_sections=previous_sections
    )

    print("\n" + "=" * 60)
    print("APPROACH")
    print("=" * 60)
    print(content)

    ensure_results_folder()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_to_json(metadata_dict, f"metadata_{timestamp}.json")
    save_to_json(filtered_results, f"filtered_chunks_{timestamp}.json")
    with open(f"x_results/approach_{timestamp}.txt", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n✅ Saved to x_results/approach_{timestamp}.txt")

if __name__ == "__main__":
    main()