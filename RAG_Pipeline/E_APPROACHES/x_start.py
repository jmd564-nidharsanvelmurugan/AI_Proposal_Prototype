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
from c_generation import (
    generate_approach_content,
    extract_tech_stack,
    check_data_platform_required
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
# Approach Template Schema
# =====================================================

class ApproachSubSection(BaseModel):
    subsection_name: str
    query: str = ""


class ApproachSection(BaseModel):
    section_name: str = "Approach"
    subsections: List[ApproachSubSection]


class ApproachTemplate(BaseModel):
    approach: ApproachSection


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

approach_template_llm = llm.with_structured_output(
    ApproachTemplate
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
# Approach Template Generation Prompt
# =====================================================

approach_template_prompt = ChatPromptTemplate.from_template(
"""
You are an expert Proposal Architect.

Generate ONLY the Approach section structure.

The Approach section should have subsections that logically group the methodology phases.

Based on the questionnaire, common approach categories include:

1. Mobilization & Discovery (e.g., Pre-kick-off, Current State Analysis)
2. Requirements & Design (e.g., KPI Definition, Data Model Design, Mock-ups)
3. Assessment & Feasibility (e.g., Data Gap Assessment, Quality Review)
4. Planning & Roadmap (e.g., Implementation Plan, Cost Estimation)

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
# Generate Section Query
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
- Capture the overall business meaning of the approach.
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

approach_template_chain = (
    approach_template_prompt
    | approach_template_llm
)


# =====================================================
# Questionnaire (Same as before with Approach section)
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
      "category_name": "Data Platform & Tech Stack",
      "questions": [
        {
          "id": "3.1", 
          "question": "Does the client have an existing data platform? (Yes/No)", 
          "answer": "Yes"
        },
        {
          "id": "3.2", 
          "question": "Which data platform(s) are currently used? (Select all that apply: Microsoft Fabric, Azure Synapse, Snowflake, Google BigQuery, AWS Redshift, Databricks, Other)", 
          "answer": "Microsoft Fabric, Azure Synapse"
        },
        {
          "id": "3.3", 
          "question": "Which CRM system(s) does the client use?", 
          "answer": "Salesforce"
        },
        {
          "id": "3.4", 
          "question": "Which reporting/BI tools does the client use?", 
          "answer": "Power BI"
        },
        {
          "id": "3.5", 
          "question": "Which databases are currently in use?", 
          "answer": "Azure Blob Storage"
        },
        {
          "id": "3.6", 
          "question": "What cloud infrastructure is used?", 
          "answer": "Microsoft Azure"
        },
        {
          "id": "3.7", 
          "question": "What integration methods are available? (APIs, ETL tools, Manual exports, Third-party connectors)", 
          "answer": "APIs, ETL tools (to be determined)"
        },
        {
          "id": "3.8", 
          "question": "What is the estimated data volume?", 
          "answer": "Medium (1-10 TB)"
        },
        {
          "id": "3.9", 
          "question": "What is the data update frequency?", 
          "answer": "Daily batch processing"
        },
        {
          "id": "3.10", 
          "question": "Are there any data quality tools in place?", 
          "answer": "No"
        },
        {
          "id": "3.11", 
          "question": "What systems need to be integrated as part of this engagement?", 
          "answer": "QuickBooks, Salesforce"
        },
        {
          "id": "3.12", 
          "question": "Are there any constraints on the tech stack (e.g., must use existing platforms, no additional licensing)?", 
          "answer": "Must leverage existing Microsoft Fabric and Azure Synapse investments"
        }
      ]
    },
    {
      "category_id": 4,
      "category_name": "Understanding",
      "questions": [
        {"id": "4.1", "question": "What business problem is the client trying to solve?", "answer": "To enhance and improve existing pipeline reporting and develop detailed Lead-to-AUM and Customer Acquisition Cost reporting."},
        {"id": "4.2", "question": "What are the current pain points?", "answer": "Limited granularity in existing pipeline reporting and lack of integrated CAC insights."},
        {"id": "4.3", "question": "What inefficiencies exist in the current process?", "answer": "Not mentioned in document."},
        {"id": "4.4", "question": "What capabilities/features are required?", "answer": "Enhanced L2A and CAC data model, Power BI reporting suite, data ingestion from QuickBooks, and data quality assessment."},
        {"id": "4.5", "question": "What workflows should be automated?", "answer": "Automated data ingestion and transformation pipelines for L2A and CAC reporting."},
        {"id": "4.6", "question": "What user roles/personas will use the system?", "answer": "Data and technology stakeholders, senior leadership, and marketing teams."},
        {"id": "4.7", "question": "What security/compliance requirements exist?", "answer": "Not mentioned in document."},
        {"id": "4.8", "question": "What integrations are mandatory?", "answer": "Integration with QuickBooks and Salesforce."}
      ]
    },
    {
      "category_id": 5,
      "category_name": "Objectives",
      "questions": [
        {"id": "5.1", "question": "What should the future-state solution achieve?", "answer": "Deliver a full Lead-to-AUM and CAC data model and reporting suite providing granular insights into pipeline performance and marketing ROI."},
        {"id": "5.2", "question": "What processes should become automated?", "answer": "Data ingestion, transformation, and reporting refresh processes."},
        {"id": "5.3", "question": "What insights should leadership gain?", "answer": "Granular understanding of the journey from lead to AUM and return on marketing spend."},
        {"id": "5.4", "question": "What user experience improvements are expected?", "answer": "Improved Power BI dashboards with clear KPI definitions and visualizations."},
        {"id": "5.5", "question": "What business processes need improvement?", "answer": "Pipeline reporting and customer acquisition cost tracking."},
        {"id": "5.6", "question": "What is the long-term vision for this solution?", "answer": "To drive data maturity and scalable reporting capabilities for Pure's growth."},
        {"id": "5.7", "question": "What scalability requirements exist?", "answer": "The data platform and reporting should be scalable to support future data sources and reporting needs."},
        {"id": "5.8", "question": "What systems should the future platform integrate with?", "answer": "Salesforce, QuickBooks, Tamarac, and Azure Fabric."},
        {"id": "5.9", "question": "What business decisions should AI support?", "answer": "Not mentioned in document."}
      ]
    },
    {
      "category_id": 6,
      "category_name": "Deliverables",
      "questions": [
        {"id": "6.1", "question": "What deliverables are expected from discovery?", "answer": "KPI Book, Power BI mock-ups, Data Model design, Data Gap Assessment, Technical Approach, and Phase 3B Implementation Plan."},
        {"id": "6.2", "question": "Should the engagement include solution architecture?", "answer": "Yes, the data model design and technical approach are part of the deliverables."},
        {"id": "6.3", "question": "Should wireframes/mockups be created?", "answer": "Yes, Power BI mock-ups limited to 8 views will be created."},
        {"id": "6.4", "question": "Should a roadmap/phased plan be prepared?", "answer": "Yes, a Phase 3B Implementation Plan will be prepared."},
        {"id": "6.5", "question": "Is a POC/MVP expected?", "answer": "Not explicitly mentioned, but the Design phase outputs serve as a foundation for the Build phase."},
        {"id": "6.6", "question": "What level of technical detail is expected in the proposal?", "answer": "Detailed data model, KPI logic, reporting requirements, and technical approach for QuickBooks integration."}
      ]
    },
    {
      "category_id": 7,
      "category_name": "Approach",
      "questions": [
        {"id": "7.1", "question": "Is real-time or batch processing required?", "answer": "Batch processing through automated pipelines in the Fabric data platform."},
        {"id": "7.2", "question": "Are APIs available for integrations?", "answer": "Not mentioned in document."},
        {"id": "7.3", "question": "What reports/dashboards are needed?", "answer": "8-page Power BI report focused on L2A and CAC reporting."},
        {"id": "7.4", "question": "Are approval workflows required?", "answer": "Not mentioned in document."},
        {"id": "7.5", "question": "What alerts/notifications are required?", "answer": "Not mentioned in document."},
        {"id": "7.6", "question": "What constraints, timelines, or dependencies must be considered?", "answer": "Phase 3A is 3 weeks; Phase 3B is 8-12 weeks; dependent on QuickBooks ingestion and data quality assessment."},
        {"id": "7.7", "question": "What is in scope for this engagement?", "answer": "Design and build of L2A and CAC data model, reporting suite, and QuickBooks integration."},
        {"id": "7.8", "question": "What is out of scope?", "answer": "Connections to systems other than Salesforce and QuickBooks, existing report migrations, enhancements to previous reporting deliverables, and platform architecture changes."}
      ]
    },
    {
      "category_id": 8,
      "category_name": "Outcomes",
      "questions": [
        {"id": "8.1", "question": "What are the expected business outcomes?", "answer": "Enhanced L2A and CAC reporting providing actionable insights into pipeline performance and marketing ROI."},
        {"id": "8.2", "question": "What KPIs or success metrics matter most?", "answer": "Lead-to-AUM conversion metrics and Customer Acquisition Cost KPIs."},
        {"id": "8.3", "question": "What risks exist if this problem is not solved?", "answer": "Limited visibility into marketing effectiveness and pipeline performance."},
        {"id": "8.4", "question": "What does success look like for the client?", "answer": "Accurate, automated, and insightful L2A and CAC reporting integrated into Power BI."},
        {"id": "8.5", "question": "What constraints exist?", "answer": "Data access, data quality, and dependency on QuickBooks integration."},
        {"id": "8.6", "question": "Are there timeline expectations?", "answer": "Phase 3A: 3 weeks; Phase 3B: 8-12 weeks."},
        {"id": "8.7", "question": "What dependencies exist?", "answer": "Access to Salesforce, QuickBooks, and existing Fabric and Synapse data platforms."}
      ]
    }
  ]
}

# =====================================================
# Placeholders for other sections
# =====================================================

business_context_placeholder = """
Pure Financial Advisors LLC operates in the financial advisory and wealth management industry in the United States. The firm offers financial advisory services and asset management to individual clients (B2C business model).

The firm currently uses Salesforce for CRM, Tamarac for portfolio management, and Azure Fabric/Synapse for data platform. QuickBooks is used for financials but is not yet integrated.

The initiative is driven by the need to develop enhanced Lead-to-AUM (L2A) pipeline and Customer Acquisition Cost (CAC) reporting.
"""

problem_statement_placeholder = """
Pure Financial Advisors faces several critical reporting limitations:

1. Limited Granularity in Pipeline Reporting
2. No Integrated CAC Visibility
3. Manual Reporting Processes
4. Inconsistent KPI Definitions
5. Data Quality Gaps
6. No Real-Time Visibility
"""

objectives_placeholder = """
This engagement aims to achieve the following measurable objectives:

1. Establish automated L2A and CAC reporting framework
2. Reduce manual reporting effort by 80%
3. Enable executive leadership to access real-time metrics
4. Integrate QuickBooks with existing Azure Fabric/Synapse
5. Create 8-page Power BI reporting suite
"""

deliverables_placeholder = """
### Assessment Deliverables
- KPI Definition Book
- Data Gap Assessment

### Design Deliverables
- Data Model Design
- Power BI Mock-ups (8 views)
- Technical Approach Document

### Planning Deliverables
- Implementation Roadmap
- Cost and Resource Estimates
"""


# =====================================================
# Main Execution
# =====================================================

def main():
    """Main execution for Approach section generation."""
    
    ensure_results_folder()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Step 1 - Extract Metadata
    print("\n" + "=" * 60)
    print("STEP 1: Extracting Metadata from Questionnaire")
    print("=" * 60)
    
    metadata = metadata_chain.invoke({"questionnaire": questionnaire})
    metadata_dict = metadata.model_dump()
    print("\n✅ Metadata extracted:")
    print(json.dumps(metadata_dict, indent=2))
    save_to_json(metadata_dict, f"approach_metadata_{timestamp}.json")
    
    # Step 2 - Get Top Matching Proposals
    print("\n" + "=" * 60)
    print("STEP 2: Getting Top Matching Proposals")
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
    
    top_proposals = get_top_matching_proposals(user_input=user_input, top_n=5)
    save_to_json(top_proposals, f"approach_top_proposals_{timestamp}.json")
    
    # Step 3 - Get Parent and Child Chunks
    print("\n" + "=" * 60)
    print("STEP 3: Fetching Parent and Child Chunks")
    print("=" * 60)
    
    document_ids = [prop["document_id"] for prop in top_proposals]
    print(f"📄 Document IDs: {document_ids}")
    
    parent_chunks = get_parent_chunks_by_document_ids(document_ids, "Approach")
    print(f"✅ Found {len(parent_chunks)} parent chunks")
    
    all_child_ids = []
    for parent in parent_chunks:
        for child_ref in parent.get("child_chunks", []):
            if child_ref.get("id") and child_ref["id"] not in all_child_ids:
                all_child_ids.append(child_ref["id"])
    
    print(f"✅ Extracted {len(all_child_ids)} unique child chunk IDs")
    child_chunks = get_child_chunks_by_ids(all_child_ids)
    print(f"✅ Retrieved {len(child_chunks)} child chunks")
    
    # Step 4 - Generate Approach Template
    print("\n" + "=" * 60)
    print("STEP 4: Generating Approach Template")
    print("=" * 60)
    
    approach_template = approach_template_chain.invoke({
        "questionnaire": questionnaire,
        "metadata": metadata.model_dump_json()
    })
    
    template_dict = approach_template.model_dump()
    print("\n✅ Approach template generated:")
    print(json.dumps(template_dict, indent=2))
    save_to_json(template_dict, f"approach_template_{timestamp}.json")
    
    # Step 5 - Check Data Platform Requirement
    print("\n" + "=" * 60)
    print("STEP 5: Checking Data Platform Requirement")
    print("=" * 60)
    
    data_platform_required = check_data_platform_required(questionnaire)
    tech_stack = extract_tech_stack(questionnaire)
    
    print(f"📊 Data Platform Required: {'✅ YES' if data_platform_required else '❌ NO'}")
    print(f"🔧 Tech Stack Extracted:")
    print(f"   - Systems: {tech_stack['systems'][:3] if tech_stack['systems'] else 'None'}")
    print(f"   - Data Platforms: {tech_stack['data_platforms'][:3] if tech_stack['data_platforms'] else 'None'}")
    print(f"   - Reporting Tools: {tech_stack['reporting_tools'][:3] if tech_stack['reporting_tools'] else 'None'}")
    print(f"   - Integrations: {tech_stack['integrations_needed'][:3] if tech_stack['integrations_needed'] else 'None'}")
    
    # Step 6 - User Interaction for Subsection Selection
    print("\n" + "=" * 60)
    print("STEP 6: Subsection Selection")
    print("=" * 60)
    
    subsections_to_include = []
    include_subsections = input("\n📝 Do you want to include subsections? (yes/no): ").strip().lower()
    
    filtered_results = None
    subsections_list = []
    generate_queries = "no"
    section_query = None
    
    if include_subsections == "yes":
        print("\n📋 Available Subsections:")
        for i, subsection in enumerate(approach_template.approach.subsections, 1):
            print(f"   {i}. {subsection.subsection_name}")
        
        choice = input("\nDo you want to include (a)ll subsections or (s)pecific ones? (a/s): ").strip().lower()
        
        if choice in ["a", "all"]:
            subsections_to_include = approach_template.approach.subsections.copy()
            print(f"\n✅ Including all {len(subsections_to_include)} subsections")
        elif choice in ["s", "specific"]:
            selection = input("Enter subsection numbers (comma-separated): ").strip()
            if selection:
                selected_indices = [int(x.strip()) - 1 for x in selection.split(",") if x.strip().isdigit()]
                for idx in selected_indices:
                    if 0 <= idx < len(approach_template.approach.subsections):
                        subsections_to_include.append(approach_template.approach.subsections[idx])
        
        if subsections_to_include:
            generate_queries = input("\n🔍 Generate retrieval queries? (yes/no): ").strip().lower()
            
            for subsection in subsections_to_include:
                if generate_queries == "yes":
                    query_prompt = f"""
Generate a short semantic retrieval phrase for Approach subsection: {subsection.subsection_name}
Questionnaire: {questionnaire}
Return ONLY the retrieval phrase (max 12 words).
"""
                    query = llm.invoke(query_prompt)
                    subsection.query = query.content.strip()
                
                subsections_list.append({
                    "subsection": subsection.subsection_name,
                    "query": subsection.query
                })
                print(f"   📌 {subsection.subsection_name} -> Query: {subsection.query if subsection.query else '(not generated)'}")
        
        filtered_results = get_filtered_chunks_for_section(
            child_ids=all_child_ids,
            subsections=subsections_list,
            search_type=1,
            top_k_per_subsection=5
        )
        
    else:
        use_query_filter = input("\n🔍 Use query-based semantic filtering? (yes/no): ").strip().lower()
        
        if use_query_filter == "yes":
            section_query = generate_section_query(questionnaire, metadata_dict, "Approach")
            print(f"\n   ✅ Generated Query: {section_query}")
            
            filtered_results = get_filtered_chunks_by_semantic_query(
                child_ids=all_child_ids,
                query=section_query,
                top_k=10
            )
        else:
            print("\n⚠️ Fetching all chunks (no filtering)...")
            filtered_results = get_filtered_chunks_for_section(
                child_ids=all_child_ids,
                subsections=[],
                search_type=1,
                top_k_per_subsection=10
            )
    
    save_to_json(filtered_results, f"approach_filtered_chunks_{timestamp}.json")
    
    # Step 7 - Generate Approach Content
    print("\n" + "=" * 60)
    print("STEP 7: Generating Approach Content")
    print("=" * 60)
    
    approach_content = generate_approach_content(
        questionnaire=questionnaire,
        metadata=metadata_dict,
        retrieved_chunks=filtered_results,
        business_context=business_context_placeholder,
        problem_statement=problem_statement_placeholder,
        objectives=objectives_placeholder,
        deliverables=deliverables_placeholder
    )
    
    # Step 8 - Save Final Response
    response = {
        "timestamp": timestamp,
        "questionnaire_metadata": metadata_dict,
        "top_matching_proposals": top_proposals,
        "approach": {
            "section_name": "Approach",
            "subsections": subsections_list,
            "section_query": section_query
        },
        "tech_stack": tech_stack,
        "data_platform_required": data_platform_required,
        "retrieved_chunks": filtered_results,
        "generated_content": approach_content
    }
    
    if approach_content:
        content_file = os.path.join("x_results", f"generated_approach_{timestamp}.txt")
        with open(content_file, "w", encoding="utf-8") as f:
            f.write(approach_content)
        print(f"✅ Generated content saved to: {content_file}")
    
    save_to_json(response, f"approach_final_response_{timestamp}.json")
    
    # Step 9 - Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"\n📊 Approach Section Generation Complete!")
    print(f"   - Timestamp: {timestamp}")
    print(f"   - Data Platform Required: {data_platform_required}")
    print(f"   - Tech Stack Items: {sum(len(v) for v in tech_stack.values())}")
    print(f"   - Top Proposals Found: {len(top_proposals)}")
    print(f"   - Content Generated: {len(approach_content)} characters")
    
    print("\n📄 Generated Approach Preview:")
    print("=" * 60)
    preview = approach_content[:600] + "..." if len(approach_content) > 600 else approach_content
    print(preview)
    
    return response


if __name__ == "__main__":
    response = main()