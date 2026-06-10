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
Context & Objectives 

 

BP is an integrated energy company with a global portfolio, operating through three business groups: gas & low carbon energy, production & operations and customers & products. Over recent years, BP has made significant investment in a modern cloud-based data and analytics architecture to enhance financial reporting processes, including its financial data foundation on Azure and Databricks, alongside services such as Azure Synapse Analytics, Power BI and Microsoft Purview, while continuing to rely on a number of legacy and local systems. This has resulted in a diverse but fragmented data landscape for financial actuals, management information and reconciliation across the group. 

 

The FP&A function is progressing Project Lighthouse to harmonise financial data, simplify the underlying technology stack and standardise reporting and planning processes across the organisation, with a clear focus on controlling tech stack proliferation and strengthening end-to-end data governance. Nevertheless, this project faces several key challenges in fully integrating data across the business groups, converging overlapping tools and embedding common data models and ways of working across the business.  

 

Challenges: 

Currently, BP faces significant challenges in fully leveraging its data infrastructure to deliver accurate, streamlined financial reporting. The FP&A leadership is looking for support to efficiently progress financial data harmonisation and improve reconciliation, reporting accuracy, and forecasting reliability. From our initial discussions we understand the core issues to include: 

 

Fragmented source of truth – Multiple systems (mentioned above) produce conflicting "headline" numbers for the same KPIs, with no single reconciled actuals dataset consumable by downstream reports or teams. 

Manual, error-prone reconciliation processes – Org/account/segment mappings scattered across Excel files, plus manual CSV edits for eliminations and top-down adjustments, and inherited Power BI logic – all driving ~20-day CFO actuals close cycles and key-person dependency. 

Mapping and ETL complexity – Incomplete mappings (especially business-group nuances), different transformation logic across pipelines, and legacy BPS constraints (quarterly inputs, 2-year horizon, aggregate org structure) prevent scalable, auditable group consolidation. 

Limited scalability for future needs – Current Power BI reconciliation tool serves a small central team but will be difficult to evolve into the governed shared dataset business leaders are planning for, aligned to IBP changes, S/4HANA migration, and downstream planning/analytics use cases. 

 

Overarching Objectives: 

JMAN can support the BP FP&A leadership in addressing these challenges and help Project Lighthouse as it works towards achieving the following overarching objectives: 

Deliver fully reconciled and trusted financial actuals – Establish a unified, transparent view of actuals across all entities to strengthen confidence in financial reporting and decision-making. 

Harmonise and modernise finance systems – Integrate FDF, FBW, and BPS into a consistent data and process framework that supports future modernisation, scalability, and migration readiness. 

Streamline and govern data and consolidation flows – Build efficient, well-governed data processes that effectively combine automation and oversight to improve consolidation speed, accuracy, and control. 

 

Immediate Objectives: 

JMAN proposes a focused 4-week discovery phase to assess and map the end-to-end actuals landscape, quantify reconciliation drivers, and determine feasibility for automation integration that will both: 

Serve as an operational foundation – Identify and prioritise the key drivers behind current actuals misalignment for the two pilot entities and define a sequenced roadmap for stabilisation 

Where feasible, evaluate structured automation opportunities – Assess whether existing mapping logic can be formalised into rule-based processes and whether recurring exceptions can be systematically identified. 

Approach 

Our approach to analysing financial actuals reporting deltas focuses on understanding and deep diving into the end-to-end data flows for two priority entities within an agreed business vertical.  

Using this foundation, JMAN will conduct an in-depth review of: 

Data discrepancies within the two pilot entities for the production & operations business to have targeted analysis. Both business unit and chosen entities are flexible and can be agreed upfront. 

A light-touch, high-level overview of current intercompany consolidation processes in that unit to provide contextual insight. 

This analysis will inform the design and planning of targeted next steps, highlighting improvement opportunities for BP while remaining aligned with the broader financial consolidation and reporting landscape. The suggested focus on the production & operations business follows BP’s strategic interests and builds on previous conversations. 

JMAN will deliver this discovery as follows: 

Understand the current end-to-end mapping and data flow by conducting stakeholder interviews, workshops, accessing source systems, and existing mapping artefacts to establish full transparency over processes, ownership, and key pain points 

Assess the different source systems and data granularity to validate hypotheses behind the actuals reconciliation deltas.  

Mapping Logic Design a potential target state addressing the identified key issues across the selected priority entity and business vertical. 

Plan next steps to implement the designed solution and providing recommendations between immediate stabilisation actions vs longer-term structural improvements 

This practical assessment of systems, data, and mapping artifacts will ensure that efforts to resolve mapping and broader system unification are targeted and effective, while directly supporting mappings for a subset of entities to inform possible automation solutions.  

Activities & Deliverables 

Scoping & Preparation (Week 0) 

The following activities will ensure timely delivery of the project, establishing the foundations for a smooth execution and an efficient discovery phase. 

BP to share access to necessary documentation – including current reconciliation results 

BP to provide access to relevant source systems, extracts & reporting layers 

Select priority business vertical – suggesting Production & Operations (upstream business) based on previous conversations, operational and strategic importance for BP 

Select 2 priority entities within the selected vertical – assessing entities by revenue contribution, strategic importance and expected complexity of data availability 

Create relevant stakeholder map + simplified RACI 

Schedule required interviews 

Review required documentation 

Validate access to relevant source systems, extracts & reporting layers (local ERPs, FBW, FDF, BPS, Power BI) 

 

Understand (Week 1 - 2) 

During the first few weeks, we will focus on conducting targeted stakeholder interviews and evaluating existing mappings while documenting findings, to gain a deep understanding of the data, processes and pain points within the selected scope and inform our assessment through defining clear hypotheses. 

Activities: 

Inter-company – conduct interviews with relevant stakeholders across finance on how inter-company consolidation is conducted in the selected business unit to understand:  

High-level intercompany consolidation processes 

High-level requirements from data sources  

Current pain points 

Business Vertical (Priority entities) – conduct interviews with relevant stakeholders from the 2 priority entities within the selected business vertical to: 

Understand data flows, systems and mapping artifacts 

Perform an initial high-level trace of end-to-end data flows to locate key transformation points and granularity gaps 

Evaluate the existing mapping logic and its feasibility for rule-based formalisation, identify exception patterns, and assess the operational feasibility of reducing manual intervention 

Document the process, people, tools and data sources involved 

Deliverables: 

Documentation of processes, systems and mappings – complete inventory of mapping artifacts (adjustment files, tables, code, models) with rules, rationale and risks captured for team continuity and reduced key-man risk 

Assess (Week 2 - 3) 

During the assessment we will test our hypotheses formed after the targeted interviews and documentation review by diving deep into the provided files and systems while assessing automation potential. 

Activities: 

Review financial adjustment files and existing org/account/segment mapping tables for the two priority entities to assess sources, transformations and current granularity gaps 

Highlight the occasions of manual interpretation, workarounds, leading to data quality constraints. Distinguishing between: 

Manual & rules-based processes with no tech supported workflow (high-automation potential) 

Manual overlays which are not rule-based (low automation potential – but ideally should be based on standardised considerations) 

Deliverables: 

Detailed root-cause diagnosis of the reconciliation gap – clearly determined and quantified drivers of reconciliation deltas for 2 prioritised entities, prioritised by impact and fixability, giving BP evidence to focus investment where it matters most 

Comprehensive end-to-end mapping of local ERPs, FBW, FDF, BPS and Power BI for 2 priority entities, showing data sources, granularity and handoffs 

 

[ADDING DECISION POINT BREAK HERE – GO / NO GO + OPTIONS] 

 

Mapping Logic Design (Week 3 - 4) 

The design phase will be condensing the results from interviews and assessments into targeted solution designs for data automation and reconciliation approach. 

Activities: 

Define a conceptual rule-based target mapping logic for the priority entities based on observed current practices 

Assess which steps are standardisable and suitable for automation 

Define required data structures, controls and process changes to reduce manual intervention 

Deliverables: 

Assessment of cross-system mapping processes – evaluation of current Excel/CSV processes versus programmatic alternatives (rules- or AI-based as suitable), quantifying coverage, accuracy and efficiency gains 

Proposed target-state approach for automated mapping (PoC scope) – defining the automated logic for the two priority entities (rules- or AI-based as suitable), including required data structures, control points, and process flow 

Plan (Week 3 - 4) 

Concluding the discovery phase, we aim to provide a tangible and pragmatic approach by suggesting the most suitable PoC design and provide a clear roadmap for implementation. 

Activities: 

Condensing findings into a targeted roadmap and prioritised next steps 

Testing assessment with key stakeholders  

Deliverables: 

Implementation Plan – detailed PoC action plan describing how the mapping use case will be deployed for the prioritised entities including the Technology requirement and level of resource (both internal and external) that would be required to achieve this 

 

Project Management and Ways of Working 

Ways of Working 

We collaborate closely with BP through a mix of in‑person and virtual engagement to ensure alignment and rapid progress. 

Engagement – Face‑to‑face interviews, workshops, and regular check‑ins to validate insights and co‑develop solutions. 

On‑Site Presence – JMAN will work from BP offices as needed to support close collaboration and smooth handovers. 

Cross‑Location Working – Chennai team members will spend two weeks in London to accelerate delivery and strengthen joint analysis. 

Governance – Weekly progress sessions and shared materials will maintain transparency and drive consistent momentum. 

 

Interview & workshop schedule: 

Timing 

Description 

Duration 

Participants 

Daily 

(Optional) Stand-up Call 

15 min 

Client project team 

Weekly 

Steering committees 

30 min 

Key BP stakeholders 

Bi-Weekly 

Deep-dive workshops (2 x per week) 

60 min 

Daniel, Dan & other relevant stakeholders 

Week 1 

Kick-off with key stakeholders 

90 min 

Key BP stakeholders 

Intercompany consolidation & reporting requirement interview 

60 min 

Finance stakeholders 

Priority entity #1 – Initial stakeholder interview 

60 min 

Entity #1 stakeholders 

Priority entity #1 – Process & system deep-dive 

120 min 

Entity #1 stakeholders 

Priority entity #2 – Initial stakeholder interview 

60 min 

Entity #2 stakeholders 

Priority entity #2 – Process & system deep-dive 

120 min 

Entity #2 stakeholders 

Week 2 

Process & mapping file deep-dive 

60 min 

Daniel, Dan & Finance Stakeholders 

Intercompany approach #1 – high-level process, tagging & mapping overview 

60 min 

Finance stakeholders 

Intercompany approach #2 – existing challenges 

60 min 

Finance stakeholders 

Priority entity #1 – Follow-up review & questions 

60 min 

Entity #1 stakeholders 

Priority entity #2 – Follow-up review & questions 

60 min 

Entity #2 stakeholders 

Week 3 

Review of ‘Assess’ findings for Entity #1 and #2 

60 min  

Key BP stakeholders (and others where relevant) 

Review of ‘Assess’ findings for inter-company consolidation 

60 min 

Key BP stakeholders (and others where relevant) 

Mapping Design workshop 

120 min 

Finance stakeholders 

Week 4  

Initial review of ‘Design’ approach for mappings 

60 min 

Daniel, Dan & Finance Stakeholders 

Follow-up review of ‘Design’ approach for mappings 

60 min 

Daniel, Dan & Finance Stakeholders 

Review of the ‘Plan’ and recommendations 

60 min 

Daniel, Dan & relevant stakeholders 

Final readout of findings, recommendations and next steps 

60 min 

Key BP stakeholders 

Out of Scope and Assumptions 

Out of Scope 

Any complete or fully operationalised data mapping 

Any optimisation to existing systems or implementation of new Solution identified part of this phase 

Any work outside of the chosen 2 priority entities 

Any additional entities must be captured by a Change Order as set out in Schedule 1 to the MSA. 

 

Assumptions 

Any relevant data extracts where possible provided ahead of project kick-off including information about relevant FP&A processes and related excel tools 

Access to systems and software as required for the work on this project 

Time and input provided by the relevant stakeholders as per 3.2, with key meetings diarized prior to project kick off 

Any delay for required access or data extracts may result in a billable timeline extension 

Timelines, Resources, and Commercials 

Timelines 

As outlined above, this project will last 4-weeks for the initial Discovery Phase. 

 

Resources 

Project oversight (Associate Partner)  

Technical oversight (Principal Architect) 

Finance SME 

2 x Data Science & AI SME 

Engagement Manager (100%) 

2 x Consultant  

Tech-Lead 

3 x Data Engineer 

 

Commercials 

Weekly Run Rate: 

GBP 31,765 per week (+ VAT) 

Total Project Price 

GBP 127,060 (+ VAT)  

Terms 

Any expenses incurred will be agreed with the Client before and charged at cost 

 
"""

    passage_2 = ""
    return passage_1, passage_2


# Remove the if __name__ == "__main__" block to prevent execution when imported