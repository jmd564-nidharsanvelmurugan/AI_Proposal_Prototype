import os
from typing import List
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from prompts import (
    PROMPT_WITH_HEADINGS,
    PROMPT_WITHOUT_HEADINGS
)

load_dotenv()


# =====================================================
# Schema - Updated with ALL metadata fields
# =====================================================

class SubSection(BaseModel):
    subsection_name: str
    content: str


class Section(BaseModel):
    section_name: str
    content: str = ""
    subsections: List[SubSection]


class ProposalKB(BaseModel):
    # Metadata fields
    business_offering: str  # SaaS, Financial Services, Field Services, Professional Services
    solution: str  # Core Reporting, Due Diligence, Data Advisory, Value Creation, Exit Prep
    region: str  # US, UK, Europe
    project_type: str  # Design and Discovery, Build, Both
    commercial_use_case: str  # Revenue bridge, Pipeline, Churn, Upsell/Cross sell, Operational Reporting
    technical_use_case: str  # Data platform, Gen AI, Data science, Full-stack development
    business_model: str  # B2B, B2C, D2C, C2C
    existing_infra_has_data_platform: bool  # true or false
    pe_relationship: str  # PE Firm, PE Portco, None
    
    # Sections (7 allowed sections only - Current State removed)
    sections: List[Section]


# =====================================================
# LLM Setup — Azure OpenAI
# =====================================================

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_deployment=os.getenv("gpt-5"),
    api_version="2024-02-15-preview",
    temperature=0,
)

structured_llm = llm.with_structured_output(ProposalKB)


# =====================================================
# Prompt Selector
# =====================================================

def get_prompt(option: int):
    if option == 1:
        return ChatPromptTemplate.from_template(PROMPT_WITH_HEADINGS)
    return ChatPromptTemplate.from_template(PROMPT_WITHOUT_HEADINGS)


def get_passages():
    passage_1 = """
    Approach, Timelines, and Deliverables 

Overview 

Kroll seek support in the delivery of a rapid, transaction-focused data cube and reporting solution to support a carve-out transaction process. We propose to break down the project into the following phases: 

Phase 1 Design & Data Assessment (2 weeks): 

Ensure focus and success in delivery by defining the key narrative and metrics to present, as well as understanding data quality, remediation options and agreeing resulting priority for reports to produce 

Carry out spot checks on key metric reconciliation, to then agree sign off approach and ways of working with Kroll 

The phase confirms scope and enables rolling straight onto a Phase 2; with JMAN having the supporting detail, access, and engagement plan with the business  

Phase 2: Build (~8 weeks – Exact scope to be determined in Phase 1):  

Build of prioritised KPIs and associated data cubes, potentially covering: 

Revenue & Sales - Providing Kroll the ability to track both revenue and opportunities across various dimensions (region, service line, project, etc), and demonstrate their revenue quality, diversity and sustainability, and opportunity development over time 

AUA – Providing Kroll the ability to understand their AUAs over time  

The scope, technology and format of cubes and reports to be determined in Phase 1 

The approach will prioritise the production of raw data cubes to be produced by start of May to support IM production, and dashboard creation will likely be treated as a secondary priority  

 

Phase 1 – Design & Data Assessment  

Deliverables 

Target narratives and KPIs – A list of target exit narratives and associated KPIs to be incorporated into the Revenue, Sales and AUA insights pack 

Output Design– Confirm format and function of final output highlighting, for example, Revenue, Sales and AUA insights (dashboards, cubes, supporting documentation), aligned to exit narratives and transaction requirements. This will include confirmation of data range to cover. 

Tooling & Technical Approach Agreement – Confirmation of the data preparation and visualisation tools (e.g., Alteryx, Power BI) to be used in Phase 2 development 

Reconciliation Approach Agreement - Outline of the reconciliation requirements and ways of working with the Finance teams to collaborate on the process (e.g. revenue, AUA, channels and loan types, maturity dates) 

Detailed Project Plan – A detailed plan for Phases 2, setting out approach, deliverables, timelines, and ways of working; factoring in other timings & requirements for the process 

 

Approach 

This phase will involve meetings with management, finance and technical representatives as well as independent assessment of provided data extracts 

Phase 2 – Build  

Deliverables 

Refreshable Analytics Pipeline – a manually refreshable analytical pipeline that cleans, transforms, and delivers the prioritised data cubes. This pipeline could be automated in a future engagement but would need transitioning into a scalable data infrastructure. 

Prioritised Outputs (agreed in Phase 1 e.g. Revenue, Sales Pipeline and AUA) 

Data Cubes – A reconciled and consolidated data cube focused on revenue, sales pipeline, serving as the foundation for the reporting suite, and can be shared with other during the transaction 

Dashboard – An interactive reporting suite presenting key metrics such as revenue trends, AUA performance, aligned to core transaction narratives (not expected to be prioritised for start of May) 

 

Approach 

This phase will be split into sub-phases based on the priority reporting, with technology and approach to be confirmed in Phase 1 

Assumptions on Data & Input from Kroll 

What Service Provider needs from Client: 

Access to relevant internal datasets (assumed csv extracts into a data room) by start of Phase 1. Require a Week 0 workshop to review data to be provided and refine SoW as required 

Responses to initial data queries shared in advanced of Week 1 

Where manual cleaning or inputting of data is required, JMAN will support as much as possible to accelerate data cleaning with the use of data tool. However, we anticipate requiring time from the Client to fill any collaboratively identified gaps in input datasets. We are assuming we will not be reconciling with work of another vendor acting in parallel. 

Weekly steer meets to review progress, blockers and priorities – with CFO, finance leads, Stonepoint & relevant advisors/DD providers 

Access to Finance teams and data/source system owners 

A SQL Environment provided by client, and relevant access, to host the technical solution. Can be hosted by JMAN if required. 

 

 

Engagement Required: 

 

Phase 1: Design & Data Assessment (2 weeks): 

 

Data and finance team briefings: Meetings to understand current data availability, processes, reconciliation approach and reporting (~6+ hrs) 

Narratives & KPI Workshop: Workshop(s) to identify required KPIs and requirements for reporting suite (2 x ~2 hrs) 

 

Phase 2: Build (~8 weeks):  

 

Steering Group: Touchpoint to review progress, blockers and priorities, and sign off outputs (~1hr / week) 

Working Group Sessions: Sessions to review outputs and unblock any challenges which might arise (~3 hrs / week) 

Reconciliation: Dedicated time during the middle of the project to support with reconciliation of outputs from source data to reporting (time tbc) 

 

Timelines 

Services start date: 

09/03/2026 

Services completion date: 

15/05/2026 

Milestones 

End of Week 1: Confirmation of target Metrics, Requirements, Data Profiling  

End of Week 2: Assessment of data limitations, date range coverage and reconciliation approach. Confirmation of scope of build; including metrics, dashboard structure, solution technology and format of output 

April 30th: Target deadline for prioritised cubes to be shared with Baird and Stonepoint for their IM 

Resource Commitment 

Resources: 

Full time analytics consultant, data engineer 

Engagement Manager & Principal oversight 

Location of Services 

Location of Services: 

 

JMAN Group Limited (London Office): 10 Lloyds Avenue, London, EC3N 3AJ, United Kingdom 

JMAN Digital Services Private Chennai Office: Module 0104 (A), First Floor, C Block South, Tidel Park, 4 Rajiv Gandhi Salai, Taramani, Chennai-600 113, India 

Fees and Payment 

Total Charges: 

$27,740 (+VAT) Weekly Run Rate 

 

Opportunity to review team and scale team/rate after Phase 1 to meet priority outputs 

Contacts 

Client Engagement Manager: 

David Blowers: david.blowers@kroll.com 

Service Provider Engagement Manager: 

Jamie Campbell jamiecampbell@jmangroup.com 

Subsequent Tasks 

Any subsequent tasks must be captured by a Change Order as set out in Schedule 1 to the Agreement. 

This SOW has been entered into by the parties on the Effective Date: 

 

 

 

.................................... 

Signed by David Blowers for and on behalf of the Client. 

 

 

.................................... 

Signed by Richard Cowen for and on behalf of the Service Provider. 

 
"""

    passage_2 = ""
    return passage_1, passage_2


# Remove the if __name__ == "__main__" block to prevent execution when imported