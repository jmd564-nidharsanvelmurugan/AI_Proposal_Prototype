from typing import List
from pydantic import BaseModel

from dotenv import load_dotenv
import json
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

import sys
import os

import json 

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, project_root)

# print("project_root =", project_root)
# print("sys.path[0] =", sys.path[0])

from retrieval.int_start import iterateor


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
# Template Schema
# =====================================================

class SubSection(BaseModel):
    subsection_name: str
    query: str = ""


class Section(BaseModel):
    section_name: str
    subsections: List[SubSection]


class ProposalTemplate(BaseModel):
    sections: List[Section]


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

template_llm = llm.with_structured_output(
    ProposalTemplate
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
# Template Generation Prompt
# =====================================================
template_prompt = ChatPromptTemplate.from_template(
"""
You are an expert Proposal Architect.

Generate a proposal structure.

The proposal MUST contain ONLY these sections:

1. Business Context
2. Overview
3. Understanding
4. Objectives
5. Deliverables
6. Approach
7. Outcomes

Rules:

- Generate all sections.
- Generate 2-3 business-oriented subsections for each section.
- Use questionnaire answers.
- Do not generate content.
- Generate subsection names only.
- Avoid generic subsection names.
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

template_chain = (
    template_prompt
    | template_llm
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


OVERVIEW

Affected Teams:
Finance, Operations, Executive Leadership

Current Systems:
SQL Server, Salesforce, Excel

Reporting Tools:
Power BI, Excel

Databases:
SQL Server, CRM Database

Manual Processes:
Manual report preparation and KPI consolidation

Integration Challenges:
Disconnected source systems

Performance Issues:
Slow report generation

Primary Data Sources:
ERP, CRM, Finance Systems

Cloud Infrastructure:
Azure

Data Governance:
Basic governance framework exists


UNDERSTANDING

Business Problem:
Leadership lacks a single source of truth.

Current Pain Points:
Manual reporting, inconsistent KPIs.

Process Inefficiencies:
Multiple teams preparing duplicate reports.

Required Features:
Centralized reporting, KPI monitoring, executive dashboards.

Workflows To Automate:
Report generation, KPI tracking.

User Personas:
Executives, Finance Analysts, Operations Managers.

Compliance Requirements:
SOX compliance.

Mandatory Integrations:
Salesforce, ERP, Data Warehouse.


OBJECTIVES

Future State:
Centralized enterprise reporting platform.

Processes To Automate:
Executive reporting and KPI distribution.

Leadership Insights:
Revenue trends, operational performance.

UX Improvements:
Self-service dashboards.

Business Process Improvements:
Reduce reporting cycle times.

Long-Term Vision:
Enterprise analytics platform.

Scalability Requirements:
Support future acquisitions.

Future Integrations:
CRM, ERP, HR Systems.

AI Decisions:
Predictive forecasting and anomaly detection.


DELIVERABLES

Expected Deliverables:
Discovery Report, Solution Architecture, Roadmap.

Solution Architecture:
Yes

Wireframes:
Yes

Roadmap:
Yes

POC:
Yes

Technical Detail:
High


APPROACH

Processing:
Batch + Near Real-Time

APIs Available:
Yes

Required Reports:
Executive KPI Dashboard

Approval Workflows:
Yes

Notifications:
Executive KPI Alerts

Constraints:
Limited budget and timeline

In Scope:
Reporting modernization

Out Of Scope:
ERP replacement


OUTCOMES

Expected Business Outcomes:
Improved decision-making and reporting efficiency.

KPIs:
Reporting cycle time, dashboard adoption.

Risks:
Poor executive visibility.

Success Criteria:
Reporting cycle reduced by 70%.

Timeline:
6 months

Dependencies:
ERP and CRM integration.
"""

# =====================================================
# Step 1 - Extract Metadata
# =====================================================

metadata = metadata_chain.invoke(
    {
        "questionnaire": questionnaire
    }
)

# =====================================================
# Step 2 - Generate Template
# =====================================================

template = template_chain.invoke(
    {
        "questionnaire": questionnaire,
        "metadata": metadata.model_dump_json()
    }
)

# =====================================================
# Response To UI
# =====================================================

response = {
    "metadata": metadata.model_dump(),
    "sections": [
        {
            "section": section.section_name,
            "subsections": [
                subsection.subsection_name
                for subsection in section.subsections
            ]
        }
        for section in template.sections
    ]
}

# =====================================================
# Display
# =====================================================

# import json

# print(
#     json.dumps(
#         response,
#         indent=4
#     )
# )

# =====================================================
# Generate Queries
# =====================================================

choice = input(
    "\nGenerate retrieval queries? (yes/no): "
).strip().lower()

if choice == "yes":

    print("\nGenerating retrieval queries...\n")

    for section in template.sections:

        for subsection in section.subsections:

            query_prompt = f"""
You are an expert proposal retrieval specialist.

Generate a short semantic retrieval phrase for vector search.

Questionnaire:
{questionnaire}

Section:
{section.section_name}

Subsection:
{subsection.subsection_name}

Rules:

- Return ONLY the retrieval phrase.
- Do NOT write a sentence.
- Do NOT write an explanation.
- Do NOT use quotes.
- Capture the business meaning.
- Include key business concepts.
- Include key technologies if relevant.
- Maximum 12 words.
- Suitable for semantic vector retrieval.

Good Examples:

Current Challenges
manual reporting and KPI visibility challenges

Business Objectives
centralized executive reporting and analytics modernization

Reporting Tools and Databases
Power BI reporting with SQL Server and CRM

Future State Vision
enterprise analytics platform with automated insights

Return only the retrieval phrase.
"""

            query = llm.invoke(query_prompt)

            subsection.query = query.content.strip()

# =====================================================
# Response To UI
# =====================================================

response = {
    "metadata": metadata.model_dump(),
    "sections": [
        {
            "section": section.section_name,
            "subsections": [
                {
                    "subsection": subsection.subsection_name,
                    "query": subsection.query
                }
                for subsection in section.subsections
            ]
        }
        for section in template.sections
    ]
}

# =====================================================
# Display
# =====================================================

# print(
#     json.dumps(
#         response,
#         indent=4
#     )
# )




print("######################################################")
print("Calling Iterator .... ")



word_doc = iterateor(
    response_iter=response,
    reponse_type=2,
    questionnaire=questionnaire
)

# Pretty print
print("WORD DOC")
print(json.dumps(word_doc, indent=4, ensure_ascii=False))

# Save to file
with open("generated_proposal.json", "w", encoding="utf-8") as f:
    json.dump(word_doc, f, indent=4, ensure_ascii=False)

print("Saved to generated_proposal.json")



