from typing import List
from pydantic import BaseModel

from dotenv import load_dotenv
import json
import os
from datetime import datetime
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from a_metadata_retrival import (
    get_top_matching_proposals, 
    get_parent_chunks_by_document_ids,
    get_child_chunks_by_ids
)
from b_subsection_filter import get_filtered_chunks_for_section, save_to_json, ensure_results_folder

load_dotenv()


# =====================================================
# Metadata Schema
# =====================================================

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


# =====================================================
# Business Context Only Schema
# =====================================================

class BusinessContextSubSection(BaseModel):
    subsection_name: str
    query: str = ""


class BusinessContextSection(BaseModel):
    section_name: str = "Business Context"
    subsections: List[BusinessContextSubSection]


class BusinessContextTemplate(BaseModel):
    business_context: BusinessContextSection


# =====================================================
# LLM
# =====================================================

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

metadata_llm = llm.with_structured_output(
    ProposalMetadata
)

business_context_llm = llm.with_structured_output(
    BusinessContextTemplate
)


# =====================================================
# Metadata Extraction Prompt
# =====================================================

metadata_prompt = ChatPromptTemplate.from_template(
"""
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
"""
)


# =====================================================
# Business Context Generation Prompt
# =====================================================

business_context_prompt = ChatPromptTemplate.from_template(
"""
You are an expert Proposal Architect.

Generate ONLY the Business Context section structure.

The Business Context section MUST contain these 3 subsections:

1. Industry Trends (or Industry Drivers)
2. Executive Decision-Making (or Strategic Rationale)  
3. Stakeholder Collaboration (or Stakeholder Landscape)

RULES FOR SUBSECTION NAMES:
- Keep names SHORT (2-3 words maximum)
- Be specific to the client's industry and situation
- Examples of GOOD short names:
  * "Industry Trends"
  * "Executive Decision-Making"
  * "Stakeholder Collaboration"

RULES:
- Generate exactly 3 subsections.
- Use questionnaire answers to create short business-oriented subsection names.
- Do NOT generate content.
- Generate subsection names only (2-3 words each).

Questionnaire:
{questionnaire}

Metadata:
{metadata}
"""
)


# =====================================================
# Chains
# =====================================================

metadata_chain = (
    metadata_prompt
    | metadata_llm
)

business_context_chain = (
    business_context_prompt
    | business_context_llm
)


# =====================================================
# Sample Questionnaire
# =====================================================

questionnaire = """
"categories": [
    {
      "category_id": 1,
      "category_name": "Business Context",
      "questions": [
        {
          "id": "1.1",
          "question": "What is the client/company name?",
          "answer": "PURE FINANCIAL ADVISORS LLC"
        },
        {
          "id": "1.2",
          "question": "What industry does the client operate in?",
          "answer": "Financial advisory and wealth management"
        },
        {
          "id": "1.3",
          "question": "What are the client's primary business offerings?",
          "answer": "Financial advisory services and asset management"
        },
        {
          "id": "1.4",
          "question": "What region/countries does the business operate in?",
          "answer": "United States"
        },
        {
          "id": "1.5",
          "question": "Who are the key business stakeholders?",
          "answer": "Jason Carver (Client Engagement Manager), Lee Equity Partners (investment partner)"
        },
        {
          "id": "1.6",
          "question": "What business model does the client follow?",
          "answer": "B2C"
        },
        {
          "id": "1.7",
          "question": "What is driving this initiative/project now?",
          "answer": "Pure is looking to develop enhanced Lead-to-AUM (L2A) pipeline and customer acquisition cost (CAC) reporting to provide more granular information about the journey from lead to AUM and return on marketing spend."
        }
"""


# =====================================================
# Create results folder
# =====================================================

ensure_results_folder()
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")


# =====================================================
# Step 1 - Extract Metadata from Questionnaire
# =====================================================

print("\n" + "=" * 60)
print("STEP 1: Extracting Metadata from Questionnaire")
print("=" * 60)

metadata = metadata_chain.invoke(
    {
        "questionnaire": questionnaire
    }
)

metadata_dict = metadata.model_dump()
print("\n✅ Metadata extracted:")
print(json.dumps(metadata_dict, indent=2))

# Save metadata to JSON
save_to_json(metadata_dict, f"metadata_{timestamp}.json")


# =====================================================
# Step 2 - Call Metadata Filter to Get Top Matching Proposals
# =====================================================

print("\n" + "=" * 60)
print("STEP 2: Calling Metadata Filter for Top Matching Proposals")
print("=" * 60)

# Prepare user input from extracted metadata
user_input = {
    "solution": [metadata.solution],
    "business_offering": [metadata.business_offering],
    "commercial_use_case": [metadata.commercial_use_case],
    "project_type": [metadata.project_type],
    "existing_infra": [metadata.existing_infra],
    "business_model": [metadata.business_model],
    "region": [metadata.region]
}

print("\n📋 User Input for Matching:")
for key, value in user_input.items():
    print(f"   - {key}: {value}")

# Get top 5 matching proposals
top_proposals = get_top_matching_proposals(
    user_input=user_input,
    top_n=5
)

# Save top matching proposals to JSON
save_to_json(top_proposals, f"top_matching_proposals_{timestamp}.json")


# =====================================================
# Step 2.5 - Get Parent and Child Chunks
# =====================================================

print("\n" + "=" * 60)
print("STEP 2.5: Fetching Parent and Child Chunks")
print("=" * 60)

# Get document IDs from top proposals
document_ids = [prop["document_id"] for prop in top_proposals]
print(f"📄 Document IDs: {document_ids}")

# Get parent chunks for Business Context section
parent_chunks = get_parent_chunks_by_document_ids(document_ids, "Business Context")
print(f"✅ Found {len(parent_chunks)} parent chunks")

# Extract all child chunk IDs
all_child_ids = []
for parent in parent_chunks:
    for child_ref in parent.get("child_chunks", []):
        if child_ref.get("id") and child_ref["id"] not in all_child_ids:
            all_child_ids.append(child_ref["id"])

print(f"✅ Extracted {len(all_child_ids)} unique child chunk IDs")

# Get child chunks
child_chunks = get_child_chunks_by_ids(all_child_ids)
print(f"✅ Retrieved {len(child_chunks)} child chunks")

# Save parent and child chunks
parent_chunks_safe = []
for pc in parent_chunks:
    pc_copy = pc.copy()
    if "child_chunks" in pc_copy:
        pc_copy["child_chunks_count"] = len(pc_copy["child_chunks"])
    parent_chunks_safe.append(pc_copy)

save_to_json({"parent_chunks": parent_chunks_safe, "child_chunks_count": len(child_chunks)}, f"chunks_{timestamp}.json")


# =====================================================
# Step 3 - Generate Business Context Template
# =====================================================

print("\n" + "=" * 60)
print("STEP 3: Generating Business Context Template")
print("=" * 60)

business_context_template = business_context_chain.invoke(
    {
        "questionnaire": questionnaire,
        "metadata": metadata.model_dump_json()
    }
)

template_dict = business_context_template.model_dump()
print("\n✅ Business Context template generated:")
print(json.dumps(template_dict, indent=2))

# Save template to JSON
save_to_json(template_dict, f"business_context_template_{timestamp}.json")


# =====================================================
# Step 4 - User Interaction: Include Subsections? (NO EXIT)
# =====================================================

print("\n" + "=" * 60)
print("STEP 4: User Interaction - Subsection Selection")
print("=" * 60)

subsections_to_include = []
include_subsections = input("\n📝 Do you want to include subsections? (yes/no): ").strip().lower()

if include_subsections == "yes":
    print("\n📋 Available Subsections:")
    for i, subsection in enumerate(business_context_template.business_context.subsections, 1):
        print(f"   {i}. {subsection.subsection_name}")
    
    choice = input("\nDo you want to include (a)ll subsections or (s)pecific ones? (a/s): ").strip().lower()
    
    if choice in ["a", "all"]:
        subsections_to_include = business_context_template.business_context.subsections.copy()
        print(f"\n✅ Including all {len(subsections_to_include)} subsections")
        
    elif choice in ["s", "specific"]:
        print("\nEnter subsection numbers to include (comma-separated, e.g., 1,2,3):")
        selection = input("Your choice: ").strip()
        
        if selection:
            selected_indices = [int(x.strip()) - 1 for x in selection.split(",") if x.strip().isdigit()]
            for idx in selected_indices:
                if 0 <= idx < len(business_context_template.business_context.subsections):
                    subsections_to_include.append(business_context_template.business_context.subsections[idx])
            
            if subsections_to_include:
                print(f"\n✅ Selected {len(subsections_to_include)} subsections:")
                for sub in subsections_to_include:
                    print(f"   - {sub.subsection_name}")
            else:
                print("\n⚠️ No valid subsections selected. Continuing with empty list...")
        else:
            print("\n⚠️ No subsections selected. Continuing with empty list...")
    else:
        print(f"\n⚠️ Invalid choice '{choice}'. Continuing with empty list...")
else:
    print("\n⚠️ Skipping subsection inclusion. Continuing with empty list...")


# =====================================================
# Step 5 - User Interaction: Generate Queries? (NO EXIT)
# =====================================================

print("\n" + "=" * 60)
print("STEP 5: User Interaction - Query Generation")
print("=" * 60)

subsections_list = []

if subsections_to_include:
    generate_queries = input("\n🔍 Do you want to generate retrieval queries for the selected subsections? (yes/no): ").strip().lower()
    
    if generate_queries == "yes":
        print("\n📝 Generating retrieval queries...")
        
        for subsection in subsections_to_include:
            
            query_prompt = f"""
You are an expert proposal retrieval specialist.

Generate a short semantic retrieval phrase for vector search.

Questionnaire:
{questionnaire}

Section:
Business Context

Subsection:
{subsection.subsection_name}

Rules:
- Return ONLY the retrieval phrase.
- Do NOT write a sentence.
- Do NOT write an explanation.
- Do NOT use quotes.
- Capture the business meaning.
- Include key business concepts.
- Maximum 12 words.
- Suitable for semantic vector retrieval.

Return only the retrieval phrase.
"""

            query = llm.invoke(query_prompt)
            subsection.query = query.content.strip()
            
            subsections_list.append({
                "subsection": subsection.subsection_name,
                "query": subsection.query
            })
            
            print(f"\n   📌 {subsection.subsection_name}")
            print(f"      Query: {subsection.query}")
        
    else:
        print("\n⚠️ Skipping query generation. Queries will be empty.")
        
        for subsection in subsections_to_include:
            subsections_list.append({
                "subsection": subsection.subsection_name,
                "query": ""
            })
            
            print(f"\n   📌 {subsection.subsection_name}")
            print(f"      Query: (not generated)")
else:
    print("\n⚠️ No subsections selected. Skipping query generation...")
    generate_queries = "no"


# =====================================================
# Step 6 - Filter Chunks Based on Subsections
# =====================================================

print("\n" + "=" * 60)
print("STEP 6: Filtering Chunks Based on Subsections")
print("=" * 60)

# Filter chunks using subsection_filter
filtered_results = get_filtered_chunks_for_section(
    child_ids=all_child_ids,
    subsections=subsections_list,
    search_type=1,  # Semantic search
    top_k_per_subsection=5
)

# Save filtered chunks to JSON
save_to_json(filtered_results, f"filtered_chunks_{timestamp}.json")


# =====================================================
# Step 7 - Generate Business Context Content
# =====================================================

print("\n" + "=" * 60)
print("STEP 7: Generating Business Context Content")
print("=" * 60)

from c_generation import generate_business_context_content

# Generate content from filtered chunks
business_context_content = generate_business_context_content(
    questionnaire=questionnaire,
    metadata=metadata_dict,
    retrieved_chunks=filtered_results
)


# =====================================================
# Step 8 - Final Response
# =====================================================

response = {
    "timestamp": timestamp,
    "questionnaire_metadata": metadata_dict,
    "top_matching_proposals": top_proposals,
    "business_context": {
        "section_name": "Business Context",
        "subsections": subsections_list if subsections_list else []
    },
    "retrieved_chunks": filtered_results,
    "generated_content": business_context_content,
    "user_preferences": {
        "included_subsections": include_subsections == "yes",
        "included_subsections_count": len(subsections_list),
        "queries_generated": generate_queries == "yes",
        "total_child_chunks": len(all_child_ids)
    }
}


# =====================================================
# Save Generated Content to File
# =====================================================

if business_context_content:
    content_file = os.path.join("x_results", f"generated_business_context_{timestamp}.txt")
    with open(content_file, "w", encoding="utf-8") as f:
        f.write(business_context_content)
    print(f"✅ Generated content saved to: {content_file}")
else:
    print("⚠️ No content generated - chunks may be missing")

# Print generated content preview
print("\n" + "=" * 60)
print("GENERATED BUSINESS CONTENT PREVIEW")
print("=" * 60)
if business_context_content:
    preview = business_context_content[:500] + "..." if len(business_context_content) > 500 else business_context_content
    print(preview)
else:
    print("No content generated (no chunks available)")


# =====================================================
# Display Final Response Summary
# =====================================================

print("\n" + "=" * 60)
print("FINAL RESPONSE SUMMARY")
print("=" * 60)

# Print summary without full text
response_summary = {
    "timestamp": response["timestamp"],
    "questionnaire_metadata": response["questionnaire_metadata"],
    "top_matching_proposals_count": len(response["top_matching_proposals"]),
    "business_context_subsections": response["business_context"]["subsections"],
    "retrieved_chunks_summary": {
        k: len(v) for k, v in response["retrieved_chunks"].items()
    },
    "generated_content_length": len(response["generated_content"]) if response["generated_content"] else 0,
    "user_preferences": response["user_preferences"]
}

print(json.dumps(response_summary, indent=4, ensure_ascii=False))


# =====================================================
# Save Final Response to JSON
# =====================================================

save_to_json(response, f"final_response_{timestamp}.json")


# =====================================================
# Print Summary
# =====================================================

print("\n📊 SUMMARY:")
print(f"   - Timestamp: {timestamp}")
print(f"   - Questionnaire metadata extracted: 9 fields")
print(f"   - Top matching proposals found: {len(top_proposals)}")
print(f"   - Total child chunks retrieved: {len(all_child_ids)}")
print(f"   - Subsections selected: {len(subsections_list)}")
print(f"   - Queries generated: {'Yes' if generate_queries == 'yes' else 'No'}")
print(f"   - Content generated: {'Yes' if business_context_content else 'No'}")

print("\n📁 Output files saved in 'x_results' folder:")
print(f"   - metadata_{timestamp}.json")
print(f"   - top_matching_proposals_{timestamp}.json")
print(f"   - chunks_{timestamp}.json")
print(f"   - business_context_template_{timestamp}.json")
print(f"   - filtered_chunks_{timestamp}.json")
print(f"   - generated_business_context_{timestamp}.txt")
print(f"   - final_response_{timestamp}.json")

if top_proposals:
    print("\n🏆 TOP 5 MATCHING PROPOSALS:")
    for prop in top_proposals[:5]:
        print(f"   {prop['rank']}. {prop['document_id']} (Score: {prop['score']})")
        print(f"      Solution: {prop['properties']['solution']}")
        print(f"      Region: {prop['properties']['region']}")