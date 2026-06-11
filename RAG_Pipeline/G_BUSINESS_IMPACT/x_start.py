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
from b_subsection_filter import (
    get_filtered_chunks_for_section, 
    save_to_json, 
    ensure_results_folder,
    get_filtered_chunks_by_semantic_query
)

from langchain_openai import AzureChatOpenAI

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
# Business Impact Template Schema
# =====================================================

class BusinessImpactSubSection(BaseModel):
    subsection_name: str
    query: str = ""


class BusinessImpactSection(BaseModel):
    section_name: str = "Business Impact"
    subsections: List[BusinessImpactSubSection]


class BusinessImpactTemplate(BaseModel):
    business_impact: BusinessImpactSection


llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_deployment=os.getenv("gpt-5"),
    api_version="2024-02-15-preview",
    temperature=0,
)


metadata_llm = llm.with_structured_output(
    ProposalMetadata
)

business_impact_template_llm = llm.with_structured_output(
    BusinessImpactTemplate
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
# Business Impact Template Generation Prompt
# =====================================================

business_impact_template_prompt = ChatPromptTemplate.from_template(
"""
You are an expert Proposal Architect.

Generate ONLY the Business Impact section structure.

The Business Impact section should have subsections that logically group the impact areas.

Based on best practices, common impact categories include:

1. Financial Impact (ROI, cost savings, revenue impact)
2. Operational Impact (efficiency gains, time savings)
3. Strategic Impact (competitive advantage, scalability)
4. Risk Reduction (compliance, data quality, decision making)

RULES:
- Generate 3-5 business-oriented subsections.
- Use questionnaire answers to create meaningful subsection names.
- Do NOT generate content.
- Generate subsection names only (2-5 words each).

Questionnaire:
{questionnaire}

Metadata:
{metadata}
"""
)


# =====================================================
# Generate Section Query (for when no subsections selected)
# =====================================================

def generate_section_query(questionnaire: str, metadata: dict, section_name: str) -> str:
    """Generate a semantic rich query for the entire section."""
    
    query_prompt = f"""
You are an expert proposal retrieval specialist.

Generate a semantic retrieval phrase for the ENTIRE {section_name} section.

Questionnaire:
{questionnaire}

Metadata:
{json.dumps(metadata, indent=2)}

Rules:
- Return ONLY the retrieval phrase.
- Do NOT write a sentence, explanation, or use quotes.
- Capture the overall business meaning of business impact expected.
- Maximum 15 words.

Return only the retrieval phrase.
"""
    
    response = llm.invoke(query_prompt)
    return response.content.strip()


# =====================================================
# Chains
# =====================================================

metadata_chain = (
    metadata_prompt
    | metadata_llm
)

business_impact_template_chain = (
    business_impact_template_prompt
    | business_impact_template_llm
)


# =====================================================
# CORRECTED QUESTIONNAIRE (Proper Python Dict)
# =====================================================

questionnaire = {
    "categories": [
        {
            "category_id": 1,
            "category_name": "Business Context",
            "questions": [
                {"id": "1.1", "question": "What is the client/company name?", "answer": "PURE FINANCIAL ADVISORS LLC"},
                {"id": "1.2", "question": "What industry does the client operate in?", "answer": "Financial advisory and wealth management"},
                {"id": "1.3", "question": "What are the client's primary business offerings?", "answer": "Financial advisory services and asset management"},
                {"id": "1.4", "question": "What region/countries does the business operate in?", "answer": "United States"},
                {"id": "1.5", "question": "Who are the key business stakeholders?", "answer": "Jason Carver (Client Engagement Manager), Lee Equity Partners (investment partner)"},
                {"id": "1.6", "question": "What business model does the client follow?", "answer": "B2C"},
                {"id": "1.7", "question": "What is driving this initiative/project now?", "answer": "Pure is looking to develop enhanced Lead-to-AUM (L2A) pipeline and customer acquisition cost (CAC) reporting to provide more granular information about the journey from lead to AUM and return on marketing spend."}
            ]
        },
        {
            "category_id": 2,
            "category_name": "Overview",
            "questions": [
                {"id": "2.1", "question": "Which teams/processes are affected?", "answer": "Data, technology, and marketing teams involved in pipeline and customer acquisition reporting."},
                {"id": "2.2", "question": "What systems/platforms are currently being used?", "answer": "Salesforce, Tamarac, Azure Blob Storage, Microsoft Fabric, Azure Synapse, Power BI, and QuickBooks (to be integrated)."},
                {"id": "2.3", "question": "What reporting or analytics tools exist today?", "answer": "Power BI reporting suite."},
                {"id": "2.4", "question": "What databases/data sources are involved?", "answer": "Salesforce, Tamarac, Azure Blob Storage, and QuickBooks."},
                {"id": "2.5", "question": "What manual processes currently exist?", "answer": "Not mentioned in document."},
                {"id": "2.6", "question": "What integration challenges exist today?", "answer": "Need to connect and ingest data from QuickBooks and assess data quality for CAC reporting."},
                {"id": "2.7", "question": "Are there performance/scalability issues?", "answer": "Not mentioned in document."},
                {"id": "2.8", "question": "What are the primary data sources?", "answer": "Salesforce, Tamarac, Azure Blob Storage, and QuickBooks."},
                {"id": "2.9", "question": "What cloud/platform infrastructure exists?", "answer": "Microsoft Fabric and Azure Synapse data platforms."},
                {"id": "2.10", "question": "Are there data governance policies?", "answer": "Not mentioned in document."}
            ]
        },
        {
            "category_id": 3,
            "category_name": "Understanding",
            "questions": [
                {"id": "3.1", "question": "What business problem is the client trying to solve?", "answer": "To enhance and improve existing pipeline reporting and develop detailed Lead-to-AUM and Customer Acquisition Cost reporting."},
                {"id": "3.2", "question": "What are the current pain points?", "answer": "Limited granularity in existing pipeline reporting and lack of integrated CAC insights."},
                {"id": "3.3", "question": "What inefficiencies exist in the current process?", "answer": "Not mentioned in document."},
                {"id": "3.4", "question": "What capabilities/features are required?", "answer": "Enhanced L2A and CAC data model, Power BI reporting suite, data ingestion from QuickBooks, and data quality assessment."},
                {"id": "3.5", "question": "What workflows should be automated?", "answer": "Automated data ingestion and transformation pipelines for L2A and CAC reporting."},
                {"id": "3.6", "question": "What user roles/personas will use the system?", "answer": "Data and technology stakeholders, senior leadership, and marketing teams."},
                {"id": "3.7", "question": "What security/compliance requirements exist?", "answer": "Not mentioned in document."},
                {"id": "3.8", "question": "What integrations are mandatory?", "answer": "Integration with QuickBooks and Salesforce."}
            ]
        },
        {
            "category_id": 4,
            "category_name": "Objectives",
            "questions": [
                {"id": "4.1", "question": "What should the future-state solution achieve?", "answer": "Deliver a full Lead-to-AUM and CAC data model and reporting suite providing granular insights into pipeline performance and marketing ROI."},
                {"id": "4.2", "question": "What processes should become automated?", "answer": "Data ingestion, transformation, and reporting refresh processes."},
                {"id": "4.3", "question": "What insights should leadership gain?", "answer": "Granular understanding of the journey from lead to AUM and return on marketing spend."},
                {"id": "4.4", "question": "What user experience improvements are expected?", "answer": "Improved Power BI dashboards with clear KPI definitions and visualizations."},
                {"id": "4.5", "question": "What business processes need improvement?", "answer": "Pipeline reporting and customer acquisition cost tracking."},
                {"id": "4.6", "question": "What is the long-term vision for this solution?", "answer": "To drive data maturity and scalable reporting capabilities for Pure's growth."},
                {"id": "4.7", "question": "What scalability requirements exist?", "answer": "The data platform and reporting should be scalable to support future data sources and reporting needs."},
                {"id": "4.8", "question": "What systems should the future platform integrate with?", "answer": "Salesforce, QuickBooks, Tamarac, and Azure Fabric."},
                {"id": "4.9", "question": "What business decisions should AI support?", "answer": "Not mentioned in document."}
            ]
        },
        {
            "category_id": 5,
            "category_name": "Deliverables",
            "questions": [
                {"id": "5.1", "question": "What deliverables are expected from discovery?", "answer": "KPI Book, Power BI mock-ups, Data Model design, Data Gap Assessment, Technical Approach, and Phase 3B Implementation Plan."},
                {"id": "5.2", "question": "Should the engagement include solution architecture?", "answer": "Yes, the data model design and technical approach are part of the deliverables."},
                {"id": "5.3", "question": "Should wireframes/mockups be created?", "answer": "Yes, Power BI mock-ups limited to 8 views will be created."},
                {"id": "5.4", "question": "Should a roadmap/phased plan be prepared?", "answer": "Yes, a Phase 3B Implementation Plan will be prepared."},
                {"id": "5.5", "question": "Is a POC/MVP expected?", "answer": "Not explicitly mentioned, but the Design phase outputs serve as a foundation for the Build phase."},
                {"id": "5.6", "question": "What level of technical detail is expected in the proposal?", "answer": "Detailed data model, KPI logic, reporting requirements, and technical approach for QuickBooks integration."}
            ]
        },
        {
            "category_id": 6,
            "category_name": "Approach",
            "questions": [
                {"id": "6.1", "question": "Is real-time or batch processing required?", "answer": "Batch processing through automated pipelines in the Fabric data platform."},
                {"id": "6.2", "question": "Are APIs available for integrations?", "answer": "Not mentioned in document."},
                {"id": "6.3", "question": "What reports/dashboards are needed?", "answer": "8-page Power BI report focused on L2A and CAC reporting."},
                {"id": "6.4", "question": "Are approval workflows required?", "answer": "Not mentioned in document."},
                {"id": "6.5", "question": "What alerts/notifications are required?", "answer": "Not mentioned in document."},
                {"id": "6.6", "question": "What constraints, timelines, or dependencies must be considered?", "answer": "Phase 3A is 3 weeks; Phase 3B is 8-12 weeks; dependent on QuickBooks ingestion and data quality assessment."},
                {"id": "6.7", "question": "What is in scope for this engagement?", "answer": "Design and build of L2A and CAC data model, reporting suite, and QuickBooks integration."},
                {"id": "6.8", "question": "What is out of scope?", "answer": "Connections to systems other than Salesforce and QuickBooks, existing report migrations, enhancements to previous reporting deliverables, and platform architecture changes."}
            ]
        },
        {
            "category_id": 7,
            "category_name": "Outcomes",
            "questions": [
                {"id": "7.1", "question": "What are the expected business outcomes?", "answer": "Enhanced L2A and CAC reporting providing actionable insights into pipeline performance and marketing ROI."},
                {"id": "7.2", "question": "What KPIs or success metrics matter most?", "answer": "Lead-to-AUM conversion metrics and Customer Acquisition Cost KPIs."},
                {"id": "7.3", "question": "What risks exist if this problem is not solved?", "answer": "Limited visibility into marketing effectiveness and pipeline performance."},
                {"id": "7.4", "question": "What does success look like for the client?", "answer": "Accurate, automated, and insightful L2A and CAC reporting integrated into Power BI."},
                {"id": "7.5", "question": "What constraints exist?", "answer": "Data access, data quality, and dependency on QuickBooks integration."},
                {"id": "7.6", "question": "Are there timeline expectations?", "answer": "Phase 3A: 3 weeks; Phase 3B: 8-12 weeks."},
                {"id": "7.7", "question": "What dependencies exist?", "answer": "Access to Salesforce, QuickBooks, and existing Fabric and Synapse data platforms."}
            ]
        }
    ]
}


# =====================================================
# Placeholders for missing sections (to be filled later)
# =====================================================

# Outcomes placeholder (initially empty, will be filled later)
outcomes_placeholder = "[TO BE GENERATED - Outcomes will define what results are achieved]"


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

save_to_json(metadata_dict, f"metadata_{timestamp}.json")


# =====================================================
# Step 2 - Call Metadata Filter to Get Top Matching Proposals
# =====================================================

print("\n" + "=" * 60)
print("STEP 2: Calling Metadata Filter for Top Matching Proposals")
print("=" * 60)

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

top_proposals = get_top_matching_proposals(
    user_input=user_input,
    top_n=5
)

save_to_json(top_proposals, f"top_matching_proposals_{timestamp}.json")


# =====================================================
# Step 2.5 - Get Parent and Child Chunks
# =====================================================

print("\n" + "=" * 60)
print("STEP 2.5: Fetching Parent and Child Chunks")
print("=" * 60)

document_ids = [prop["document_id"] for prop in top_proposals]
print(f"📄 Document IDs: {document_ids}")

parent_chunks = get_parent_chunks_by_document_ids(document_ids, "Business Impact")
print(f"✅ Found {len(parent_chunks)} parent chunks")

all_child_ids = []
for parent in parent_chunks:
    for child_ref in parent.get("child_chunks", []):
        if child_ref.get("id") and child_ref["id"] not in all_child_ids:
            all_child_ids.append(child_ref["id"])

print(f"✅ Extracted {len(all_child_ids)} unique child chunk IDs")

child_chunks = get_child_chunks_by_ids(all_child_ids)
print(f"✅ Retrieved {len(child_chunks)} child chunks")

parent_chunks_safe = []
for pc in parent_chunks:
    pc_copy = pc.copy()
    if "child_chunks" in pc_copy:
        pc_copy["child_chunks_count"] = len(pc_copy["child_chunks"])
    parent_chunks_safe.append(pc_copy)

save_to_json({"parent_chunks": parent_chunks_safe, "child_chunks_count": len(child_chunks)}, f"chunks_{timestamp}.json")


# =====================================================
# Step 3 - Generate Business Impact Template
# =====================================================

print("\n" + "=" * 60)
print("STEP 3: Generating Business Impact Template")
print("=" * 60)

business_impact_template = business_impact_template_chain.invoke(
    {
        "questionnaire": questionnaire,
        "metadata": metadata.model_dump_json()
    }
)

template_dict = business_impact_template.model_dump()
print("\n✅ Business Impact template generated:")
print(json.dumps(template_dict, indent=2))

save_to_json(template_dict, f"business_impact_template_{timestamp}.json")


# =====================================================
# Step 4 - User Interaction: Include Subsections?
# =====================================================

print("\n" + "=" * 60)
print("STEP 4: User Interaction - Subsection Selection")
print("=" * 60)

subsections_to_include = []
include_subsections = input("\n📝 Do you want to include subsections? (yes/no): ").strip().lower()

use_query_filter = False
section_query = None

if include_subsections == "yes":
    print("\n📋 Available Subsections:")
    for i, subsection in enumerate(business_impact_template.business_impact.subsections, 1):
        print(f"   {i}. {subsection.subsection_name}")
    
    choice = input("\nDo you want to include (a)ll subsections or (s)pecific ones? (a/s): ").strip().lower()
    
    if choice in ["a", "all"]:
        subsections_to_include = business_impact_template.business_impact.subsections.copy()
        print(f"\n✅ Including all {len(subsections_to_include)} subsections")
        
    elif choice in ["s", "specific"]:
        print("\nEnter subsection numbers to include (comma-separated, e.g., 1,2,3):")
        selection = input("Your choice: ").strip()
        
        if selection:
            selected_indices = [int(x.strip()) - 1 for x in selection.split(",") if x.strip().isdigit()]
            for idx in selected_indices:
                if 0 <= idx < len(business_impact_template.business_impact.subsections):
                    subsections_to_include.append(business_impact_template.business_impact.subsections[idx])
            
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
    
    subsections_list = []
    generate_queries = "no"
    
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
Business Impact

Subsection:
{subsection.subsection_name}

Rules:
- Return ONLY the retrieval phrase.
- Do NOT write a sentence or explanation.
- Do NOT use quotes.
- Capture the business meaning.
- Maximum 12 words.

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
            for subsection in subsections_to_include:
                subsections_list.append({
                    "subsection": subsection.subsection_name,
                    "query": ""
                })
                print(f"\n   📌 {subsection.subsection_name}")
                print(f"      Query: (not generated)")
    
    print("\n" + "=" * 60)
    print("STEP 5: Filtering Chunks Based on Subsections")
    print("=" * 60)
    
    filtered_results = get_filtered_chunks_for_section(
        child_ids=all_child_ids,
        subsections=subsections_list,
        search_type=1,
        top_k_per_subsection=5
    )

else:
    print("\n⚠️ No subsections selected. Proceeding with section-level filtering...")
    
    use_query_filter = input("\n🔍 Do you want to use query-based semantic filtering? (yes/no): ").strip().lower()
    
    if use_query_filter == "yes":
        print("\n📝 Generating semantic query for the entire Business Impact section...")
        
        section_query = generate_section_query(str(questionnaire), metadata_dict, "Business Impact")
        print(f"\n   ✅ Generated Query: {section_query}")
        
        print("\n" + "=" * 60)
        print("STEP 5: Filtering Chunks with Semantic Query")
        print("=" * 60)
        
        filtered_results = get_filtered_chunks_by_semantic_query(
            child_ids=all_child_ids,
            query=section_query,
            top_k=10
        )
        
        subsections_list = []
        generate_queries = "yes"
        
    else:
        print("\n⚠️ Proceeding normally without filtering. Fetching all chunks...")
        
        print("\n" + "=" * 60)
        print("STEP 5: Fetching All Chunks (No Filtering)")
        print("=" * 60)
        
        filtered_results = get_filtered_chunks_for_section(
            child_ids=all_child_ids,
            subsections=[],
            search_type=1,
            top_k_per_subsection=10
        )
        
        subsections_list = []
        generate_queries = "no"
        section_query = None


# =====================================================
# Save filtered chunks to JSON
# =====================================================

save_to_json(filtered_results, f"filtered_chunks_{timestamp}.json")


# =====================================================
# Step 6 - Generate Business Impact Content
# =====================================================

print("\n" + "=" * 60)
print("STEP 6: Generating Business Impact Content")
print("=" * 60)

from c_generation import generate_business_impact_content

# Generate content with outcomes placeholder (initially empty)
business_impact_content = generate_business_impact_content(
    questionnaire=questionnaire,
    metadata=metadata_dict,
    retrieved_chunks=filtered_results,
    outcomes=outcomes_placeholder
)


# =====================================================
# Step 7 - Final Response
# =====================================================

response = {
    "timestamp": timestamp,
    "questionnaire_metadata": metadata_dict,
    "top_matching_proposals": top_proposals,
    "business_impact": {
        "section_name": "Business Impact",
        "subsections": subsections_list if subsections_list else [],
        "section_query": section_query if section_query else None
    },
    "retrieved_chunks": filtered_results,
    "generated_content": business_impact_content,
    "user_preferences": {
        "included_subsections": include_subsections == "yes",
        "included_subsections_count": len(subsections_list),
        "queries_generated": generate_queries == "yes",
        "use_query_filter": use_query_filter if include_subsections != "yes" else False,
        "section_query_used": section_query if section_query else None,
        "total_child_chunks": len(all_child_ids)
    }
}


# =====================================================
# Save Generated Content to File
# =====================================================

if business_impact_content:
    content_file = os.path.join("x_results", f"generated_business_impact_{timestamp}.txt")
    with open(content_file, "w", encoding="utf-8") as f:
        f.write(business_impact_content)
    print(f"✅ Generated content saved to: {content_file}")
else:
    print("⚠️ No content generated")

print("\n" + "=" * 60)
print("GENERATED BUSINESS IMPACT PREVIEW")
print("=" * 60)
if business_impact_content:
    preview = business_impact_content[:500] + "..." if len(business_impact_content) > 500 else business_impact_content
    print(preview)
else:
    print("No content generated")


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
if include_subsections == "yes":
    print(f"   - Subsections selected: {len(subsections_list)}")
    print(f"   - Queries generated: {'Yes' if generate_queries == 'yes' else 'No'}")
else:
    print(f"   - Query-based filtering: {'Yes' if use_query_filter == 'yes' else 'No'}")
    if use_query_filter == "yes":
        print(f"   - Section Query: {section_query}")
print(f"   - Content generated: {'Yes' if business_impact_content else 'No'}")

print("\n📁 Output files saved in 'x_results' folder:")
print(f"   - metadata_{timestamp}.json")
print(f"   - top_matching_proposals_{timestamp}.json")
print(f"   - chunks_{timestamp}.json")
print(f"   - business_impact_template_{timestamp}.json")
print(f"   - filtered_chunks_{timestamp}.json")
print(f"   - generated_business_impact_{timestamp}.txt")
print(f"   - final_response_{timestamp}.json")

if top_proposals:
    print("\n🏆 TOP 5 MATCHING PROPOSALS:")
    for prop in top_proposals[:5]:
        print(f"   {prop['rank']}. {prop['document_id']} (Score: {prop['score']})")
        print(f"      Solution: {prop['properties']['solution']}")
        print(f"      Region: {prop['properties']['region']}")