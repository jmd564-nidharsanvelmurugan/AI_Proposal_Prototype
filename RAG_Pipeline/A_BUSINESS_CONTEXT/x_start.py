from typing import List
from pydantic import BaseModel

from dotenv import load_dotenv
import json
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from a_metadata_retrival import get_top_matching_proposals

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
# Business Context Generation Prompt (UPDATED)
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
  * "Industry Trends" (not "Navigating Financial Services Industry Trends")
  * "Executive Decision-Making" (not "Enhancing Executive Decisions through Timely Insights")
  * "Stakeholder Collaboration" (not "Collaboration from Key Stakeholders like CDO and CFO")

- Examples of BAD long names to AVOID:
  * "Navigating Financial Services Industry Trends and Regulatory Pressures"
  * "Enhancing Executive Decision-Making through Timely Performance Insights"
  * "Collaboration and Buy-In from Key Stakeholders: CDO, CFO, and Head of Operations"

RULES:
- Generate exactly 3 subsections.
- Use questionnaire answers to create short business-oriented subsection names.
- Do NOT generate content.
- Generate subsection names only (2-3 words each).
- Subsections should reflect the client's business situation.

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
CLIENT & BUSINESS CONTEXT

Client Name:
ABC Financial Services

Industry:
Financial Services

Primary Business Offerings:
Retail Banking, Commercial Lending, Wealth Management

Region:
United States

Key Stakeholders:
Chief Data Officer, CFO, Head of Operations

Business Model:
B2B

Project Driver:
Executive leadership lacks timely visibility into business performance.
"""


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

print("\n✅ Metadata extracted:")
print(json.dumps(metadata.model_dump(), indent=2))


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

print("\n✅ Business Context template generated:")
print(json.dumps(business_context_template.model_dump(), indent=2))


# =====================================================
# Step 4 - Generate Queries for Business Context Subsections
# =====================================================

print("\n" + "=" * 60)
print("STEP 4: Generating Retrieval Queries")
print("=" * 60)

subsections_list = []

for subsection in business_context_template.business_context.subsections:
    
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


# =====================================================
# Step 5 - Final Response
# =====================================================

response = {
    "questionnaire_metadata": metadata.model_dump(),
    "top_matching_proposals": top_proposals,
    "business_context": {
        "section_name": "Business Context",
        "subsections": subsections_list
    }
}


# =====================================================
# Display Final Response
# =====================================================

print("\n" + "=" * 60)
print("FINAL RESPONSE")
print("=" * 60)

print(json.dumps(response, indent=4, ensure_ascii=False))


# =====================================================
# Save to File
# =====================================================

with open("business_context_with_matches.json", "w", encoding="utf-8") as f:
    json.dump(response, f, indent=4, ensure_ascii=False)

print("\n" + "=" * 60)
print("✅ Saved to business_context_with_matches.json")
print("=" * 60)


# =====================================================
# Print Summary
# =====================================================

print("\n📊 SUMMARY:")
print(f"   - Questionnaire metadata extracted: 9 fields")
print(f"   - Top matching proposals found: {len(top_proposals)}")
print(f"   - Business Context subsections generated: {len(subsections_list)}")

if top_proposals:
    print("\n🏆 TOP 5 MATCHING PROPOSALS:")
    for prop in top_proposals:
        print(f"   {prop['rank']}. {prop['document_id']} (Score: {prop['score']})")
        print(f"      Solution: {prop['properties']['solution']}")
        print(f"      Region: {prop['properties']['region']}")