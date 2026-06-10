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
    passage_1 = """SOW Terms:  

Scope of Work 

Overview 

Prescient Healthcare Group is a global pharmaceutical strategy and decision‑support consultancy founded in 2007 and headquartered in London, with additional offices in the US, India, and China. The firm works with multinational pharmaceutical companies and emerging biotech organisations to provide clinical, commercial, and competitive insights throughout the drug lifecycle. Prescient has undergone significant private equity ownership changes that have shaped its growth. Baird Capital first invested in the company in 2017, helping expand its data‑driven technology platform and international footprint, and in January 2021, the business was acquired by Bridgepoint. Under Bridgepoint’s ownership, Prescient has continued scaling in a global decision‑support market valued at over $1.4 billion and growing 10–12% annually. Prescient has also executed a buy‑and‑build strategy, acquiring Strategic North and more recently Uptake, with another acquisition expected to complete shortly. These integrations have expanded the organisation’s operational complexity and system landscape. Internally, the leadership team is preparing for a targeted exit within the next ~12 months, increasing the importance of creating a unified data and technology environment, consistent KPIs, and a strong value‑creation narrative for potential investors. 

Current System Landscape 

Prescient’s current technology environment reflects a combination of organic growth and multiple acquisitions, resulting in a fragmented and inconsistent system landscape. The core Prescient business uses Salesforce as its primary CRM platform, Sage Intacct for finance, and Concur for expenses and invoice approvals. Project financials are managed through Kantata, though its configuration and adoption are limited, and it is not widely used for delivery tracking. The HR function currently operates on Oracle, but due to significant data quality issues, including inconsistent organisational hierarchies, the company plans to migrate to BambooHR in the near-term. Reporting across these systems is inconsistent, with most analysis performed through manual Excel extraction and stitching.  

The Uptake acquisition adds further complexity, operating on Xero for finance, CMAP for project management and CRM‑like functionality, and BambooHR for HR. Uptake will be moved onto Salesforce and Sage Intacct, with financial migration planned after its March year‑end close. The upcoming acquisition is expected to introduce another set of systems, including Xero for finance and bespoke internal tools for time, leave, and HR processes. Existing integrations between systems are limited. For example, Kantata and Sage Intacct share customer codes through an API for invoicing, but account setup remains manual, increasing the likelihood of mismatches or duplicates. Salesforce does not automatically push customer records to other systems, creating duplicated entry points and inconsistent customer identifiers. Historical data is spread across legacy systems such as Sage 50 and CMAP, with varying levels of completeness, and only partial migrations have been performed during past acquisitions. 

Current Data Challenges 

Prescient faces several critical data challenges across customers, financials, projects, HR, and drug/asset metadata. Customer and account data suffers from duplicate child accounts, inconsistent naming, and manual entry across multiple systems, leading to mismatch between Salesforce, Kantata, and Sage Intacct. There is no single customer master, and overlap across Prescient, Uptake, and the new acquisition requires complex mapping to understand the full client relationship landscape. Project and delivery data is fragmented between Kantata and CMAP, with Kantata used primarily for financial tracking rather than operational delivery, limiting its usefulness for utilisation or performance insights. 

Financial data is split across Sage Intacct, multiple Xero instances, and legacy Sage 50, with the cleanest consistent data only available from January 2023 onward due to staggered migrations. HR data is also inconsistent: Oracle has significant accuracy issues, historical role and grade structures vary across entities, and older HR systems may no longer be accessible. This complicates historical calculation across key financial and operational KPIs including margin by role, cost per FTE, and utilisation metrics. Drug and asset metadata suffers from free‑text entry in Salesforce, resulting in inconsistent or incomplete INN, brand, and code name fields. Only one of the three asset fields is mandatory, and projects covering multiple assets lack standardised allocation rules, limiting the ability to tie revenue to specific assets or phases. Patent data is not captured systemically and is currently being compiled manually for only recent revenue. Finally, reporting is heavily Excel‑driven, with no central data warehouse or unified schema, making analytics slow, manual, and highly error‑prone. Prescient management are keenly aware of their data challenges and have identified and actioned multiple workstreams focused on data remediation. 

Context 

Prescient has engaged JMAN to provide a proposal for an initial scope of work which seeks to establish a foundation for high-quality commercial and operational data to support business decision-making and prepare for an eventual transaction. This will focus on designing reporting solutions that provide clear visibility on growth drivers and value creation levers while addressing the data quality and reconciliation challenges that currently exist. There is particular interest in tracking sales and revenue across the molecule lifecycle with a forward-looking view on patent end dates, cross-selling and synergy benefits after acquisitions, and demonstrating the long-tenured, repeatable nature of client relationships. Whilst focusing on key growth drivers and transaction preparedness, the reporting solutions will ultimately deliver operational insights in the hands of the people who need data on a day-to-day basis.  

 

Project Overview 

JMAN will provide a roadmap and plan to build a core reporting suite. This will focus on delivering reporting for different user groups: from operational/partner-level reporting to management and board-level reporting, all the way up to investor-reporting. At time of exit, the dashboards can also support the demonstration of a compelling equity story for future investors, ensuring Prescient has one, single-source-of-truth for data and reporting. The reporting priorities and KPIs will be defined in collaboration with key Client stakeholders, absorbing existing requirements already defined and will incorporate JMAN’s recommendations from previous work building reporting for professional services businesses. 

JMAN recognises that Prescient has already made some progress with Power BI implementation but has not made investment in a single-source-of-truth (SSoT) data platform. Our approach will build upon current reporting, ensuring that our data architecture and infrastructure recommendations integrate with and enhance these existing platforms and technology rather than replacing them. Additionally, JMAN will be mindful of the upcoming system migrations, including BambooHR and a decision on Kantata vs. CMAP, to ensure our recommendations align with and complement these strategic initiatives. 

The proposal is broken into two phases. This proposal and statement of work covers the Design & Discovery Phase (outlined below). On completion of the Design & Discovery Phase, one of the deliverables will be a proposal and implementation plan for a Reporting Build Phase 2. 

 

Phase 1 – Design & Discovery 

 

Outputs - Part I (Align on target narratives, corresponding Value Levers, use cases and Metrics that matter) 

Equity Story & Growth Levers: Align with the business (and Bridgepoint) on the key narratives the business will want to present at exit. Ensure these are aligned with the reporting and contextual business requirements of the management team to operationally run and track performance. Translate these narratives into a broad set of KPIs and reporting dimensions. 

Reporting use cases, including prioritisation: On the back of Target equity narratives, work with the business to align on key value drivers that allow the management team to track business performance and evidence target narratives, leading to a prioritised set of use cases that have the most impact on the valuation and are relatively easy to implement. The prioritisation is to be agreed by the end of week 2, to support further development of Part II of outputs.  

Reporting suite design, including roadmap: Work collaboratively with key business stakeholders to align on the “north-star” vision of the end-state reporting landscape for Prescient, and develop a delivery roadmap for reporting, ensuring priority reports are delivered as part of Phase 2. This involves defining: 

User-groups: Who are the different user groups that will consume reporting at different levels of the business – e.g. Board/Investor, Management, and Operators (i.e. Partner/Division-leads, or Teams etc.) 

Reporting pillars/verticals: Agreeing on the key reporting pillars and their prioritisation across the business that will surface the relevant insights – e.g. finance, customer, people/HR, project/operational, sales, etc. 

Reports & tools: Across the different user-groups and reporting pillars/verticals, how will these be divided/presented in specific tools to allow the different user-groups visibility of what they require – e.g. a board report will likely aggregate the top-level KPIs across finance, customer, people etc. Whereas a partner report, might only include the relevant operational reporting, or a CFO pack only include the finance pillar of reporting. 

Data architecture and infrastructure design: A recommendation for the augmentation and development of data infrastructure to support the deployment of the platform for connection, ingestion, and consolidation of legacy, current, and new systems. The design will be cognizant of Prescient's ongoing buy-and-build strategy, its existing technology landscape, and will align with the planned system changes (e.g., Bamboo, Kantata). We will work in close collaboration with Prescient technical teams on recommendations, to ensure the data platform and reporting suite can be owned and maintained by internal teams following delivery of the platform and reporting in Phase 2. 

 

Outputs - Part II (Build further details on prioritised use case(s), targeting specific value levers) 

“Metrics that Matter” & dimension dictionary: A clearly defined list of metrics including data points required & proposed calculation methodology. This will be accompanied by the target dimensions with which Prescient wants to slice the business. The dictionary will be focused on the requirements of the priority use cases(s) identified at the end of week 2 - additional metrics beyond this will be noted down for future reference & development.  

Dashboard mock-ups: Design of the insights & reports for the priority metrics agreed as the priority use case. These visual mock-ups will capture layout, structure, and functionality requirements and will serve as the blueprint in the implementation phase. 

Conceptual data model: A high-level, conceptual group data model that outlines the structure and flow of data needed to deliver the agreed reporting requirements for the priority reporting use case. 

Data gap assessment and process recommendations: High-level assessment of data availability for priority reporting, identifying gaps in coverage to conduct a feasibility assessment during roadmap prioritisation. Where data is not (or poorly) available, work with stakeholders to provide data recommendations and identify areas for process improvement to improve quality and availability over time. Recommendations will be cognisant and work alongside currently planned/ongoing data remediation efforts and will consider changes required to unlock additional or future value-add use cases, where relevant.  

Implementation plan: A detailed plan outlining build phase activities, milestones, and timelines for developing the priority data assets and reports. The roadmap will be structured into prioritised, sprint-based phases to enable incremental delivery of use cases and value throughout the build. This implementation plan will include integration of go-forward systems as well as historical data. 

 

Benefits of Approach 

Service Provider Professional Services Expertise – extensive experience building data platforms for PE-backed professional services businesses, including Pharmaceuticals, across multiple industries and geographies. Our work with similar businesses enables tailored insights on organic revenue growth, quality of earnings, customer acquisition costs, product profitability and service line profitability, all critical to Prescient's growth. 

M&A Platform – final deliverables of a Build phase provide Prescient with a data and reporting suite for rapid data integration playbook for new acquisitions without immediate system migrations. This supports Prescient's strategy of 2-3 add-on acquisitions annually and ensures consistent reporting despite potential legacy system differences. 

Lasting Data Asset – a data platform and reporting suite is a lasting data asset for Prescient, this serves as a foundation for M&A and insights/reporting, ensuring Prescient is a mature, data-driven management team. 

Single-Source-of-Truth Data & Reporting – across the complex data landscape and multiple entities, this approach leaves Prescient with a consolidated, trusted, single-source-of-truth data asset that is the foundation for data-led decision-making. 

Leveraged for a Future Transaction – a data platform and reporting suite can serve as a data asset for future transactions, with two-fold effects: (i) easily serve up data for buy- and sell-side diligence, (ii) helps present the business as a data mature company with valuable data assets. 

Expertise in Diverse Data Maturity Landscape – JMAN has extensive experience working with extremely acquisitive businesses, with a broad range of data maturities (e.g. Excel-based to system-based reporting) and challenges in cross-system reconciliation. 

 

Approach 

Week 0: Pre-kick off 

Ensure JMAN has what they need to hit the ground running and are not blocked during the five-week project 

Data access: Work with Prescient to arrange full access to required systems (Salesforce, Sage, Kantata, CMAP), containing customer/revenue/operational data, plus any existing reports being generated on this data 

Meetings schedule: Work with Prescient to book the required workshops and meeting cadences 

Data architecture / infrastructure documentation: Liaise with internal technical stakeholders to receive all the existing documentation for reporting, infrastructure & systems landscape, and tech stack configurations, where these exist 

 

Weeks 1-2: Requirements, reporting design, and platform recommendation 

Define reporting suite end-state, capture, assess and prioritise use cases, and align on KPIs to support central management and operational reporting, driving a data model that ensures accurate KPI calculations and effective data management. Assess current technology infrastructure, define requirements, and recommend a scalable data platform, including available market options and pricing, both one-time and ongoing. 

Equity narratives and articulation using data: Workshops with Prescient Management and Bridgepoint to understand the Prescient equity narratives and translate these into a set of metrics and reporting cuts that can support their articulation. 

Reporting suite design: Workshops with Prescient to define the report suite design end-state (user-groups, reporting pillars/verticals, reports and tools). Capture full set of use cases across the business working with Prescient stakeholders, and define priority based on both EBITDA and Exit Valuation impact. For the agreed highest priority use cases, define key performance indicators (KPIs) for priority reporting. JMAN’s expectation based on discussions to date and our experience is the primary priority will be customer and revenue reporting – this will be confirmed with Prescient in workshops. JMAN will build upon the ‘Metrics that Matter’ for pharma commercialisation platforms that were discussed in detail during the scoping workshops. 

Existing reporting and requirements: Spend time understanding existing reports shared, including meetings with report owners to understand existing process, and understanding further ‘wish list’ of future KPIs Prescient wants to report on. 

Going more granular: Confirming the required level of granularity for metrics and key segments/dimensions (i.e. entities, geographies, brands, partners, etc.). JMAN will have an initial sense of these based on the scoping workshop. 

Define the data and analytics roadmap: Starting with the highest priority use cases, define a roadmap utilising the agreed prioritisation scoring for the long list of use cases, working in parallel with Prescient timelines for data remediation, system changes, and transaction. 

Data architecture workshop: Review any existing data infrastructure, tooling, softwares, and recommend a data platform design to meet the reporting requirements and serve as a scalable foundation for future use-cases. 

Data architecture recommendation: Develop a data architecture recommendation that builds upon Prescient's investment in Power BI and integrates with the existing technology stack. This will be developed in collaboration with Prescient technical teams and agreed prior to the final read out. 

 

Decision Point: At the end of Week 2, there is a key Decision point meeting with Prescient management to align and agree on 

Use case prioritisation, and data & analytics roadmap – this will be used to define the scope of the data gap assessment conducted in Weeks 3&4 which will define the data remediation plan. 

Data platform recommendation – this will be used to define the platform of choice and inform the implementation planning (timing and cost) to be conducted in the Build Phase (Phase 2).  

 

Week 3-4: Data source assessment and initial model design 

Gain a clear understanding of current data sources, data points, and reporting processes that will support priority reporting. Begin development of the target state data model. 

Current state: Understand the existing business terms, metric calculations, data sources, and reports being generated by Prescient, and revise KPIs / logic definition as required  

KPI Calculation logic: Define the formulas and calculations required to derive priority KPIs and metrics from the data 

Design initial dashboard mock-ups: Based on the agreed highest priority reporting use cases, draft dashboard mock-ups to help inform implementation plan and data model design. 

Dashboard mock up iteration & finalisation: Working with management, iterate and finalise mock ups for priority reporting use cases. 

Data source review: Identify relevant data sources (e.g., Sage, Salesforce, Kantata, CMAP) and tables that will feed into priority reporting. Specific focus on reconciliation between project management systems (Kantata, CMAP) and financial reporting systems (Sage). 

Data gap assessment: Evaluate the availability of data for priority reporting, and where data is not available work with stakeholders to determine a path forward (e.g. automated extraction of data from invoices) 

Data availability prioritisation: Identify the most critical data coverage issues that need to be addressed to enable priority reporting and provide recommendations or develop plans for the Phase 2 build on how these can be enriched or cleaned.  

Client & Product hierarchy framework: Building upon current hierarchy definitions, develop an initial framework for establishing a proper parent-child client and product hierarchy. 

Data model: Highlight the required relationships between data sources in the platform to be able to execute and create the calculation logic for priority reporting. Design the data model that accounts for Prescient's key dimensions/reporting matrix (i.e. geographies, accounts, and service lines). 

 

Week 5: Solution design and implementation plan development 

Finalise the data model design, develop implementation recommendations, and create a roadmap for execution of the data platform build/augmentation and priority use-case reporting build-out. 

Finalise data model: based on system learnings, feedback from management, and mock-up finalisation, confirm the end-state data model design. 

Data cleaning and enrichment recommendations: based on the data coverage and data gap assessment in Weeks 3&4, provide recommendations for and confirm approaches for tackling data challenges, cleaning, or enrichment in Phase 2 (e.g. external source, GenAI deployment). This will work in tandem with ongoing/planned data remediation efforts defined by Prescient and will look to scope in Phase 2 data remediation that can be handled directly by JMAN. 

Implementation plan: Based on the current infrastructure Prescient has, design a build plan to deliver the priority core reporting. The implementation plan will align with timelines for planned system upgrades and existing reporting. 

Other use cases: Highlight how the data platform design will support second priority reporting and additional use cases, for example entity-level operational sales & pipelines reporting, project profitability analytics, or more advanced ML/AI expansion or retention prediction engines. 

 

Timelines 

Week 0 Start Date: 

16 March 2026 

Week 1 Start Date: 

23 March 2026 

Timelines: 

5-weeks 

Services Completion Date: 

24 April 2026 

 

Assumptions & Requirements 

Out of scope: 

JMAN will not start any technical development of the build phase during the initial engagement. This involves (but is not limited to) data cleansing, architecture set-up, tool provisions, system connectivity, or dashboard development. 

Required support from data source owners: 

JMAN will have access to extracts and source systems ahead of kick off for the data sources included in scope 

JMAN has access to data system owners / providers to resolve any clarifications around data availability and end points 

Required support and time from the client: 

These may be revised based on the pre-kick off sessions, but our current requirement from Prescient would be: 

Jason McKenna, Rachael Farmer, Andy Clarke, Swati Kkatyal and other key members of the management team, and potentially Bridgepoint representation 

Part I 

Equity Story & Growth Levers: Week 1, Session 1 (90 mins): JMAN will prepare set of target equity narratives and underlying value levers to test and validate 

Equity Story & Growth Levers: Week 1, Session 2 (90 mins): JMAN to present refined narratives specific to Prescient for sign off. JMAN to also present first draft of Metrics that Matter 

Reporting Use cases & Suite: Week 1: 4 Sessions 60-minutes each with different functions: Commercial / Sales, Finance, Operations. People / HR to gather use-cases and current pain points  

Reporting Use cases & Suite: Week 2 (60 mins): Use cases playback and Prioritisation framework output 

Data Architecture Current State: Week 1, Session 1 (60 mins): Workshop to understand current state architecture and any in-flight changes or planned changes 

Data Architecture Current State & Future Requirements: Week 1, Session 2 (60 mins): JMAN playback of understanding and requirements gathering for future platform across key areas 

Data Architecture Requirements: Week 2, Session 1 (60 mins): Playback and validation 

Data Architecture Recommendation: Week 2, Session 1 (60 mins): JMAN to present optionality alongside recommendation in accordance with gathered requirements 

Part II 

Metrics that Matter: Week 3, Session 1 (60 mins): JMAN to present typical definitions and calculation logic for priority use case KPIs and gather feedback 

Metrics that Matter: Week 3, Session 2 (30 mins): JMAN to present refined KPIs definitions and calculations and gather feedback 

Metrics that Matter: Week 3, Session 3 (30 mins): To be used as needed for final iterations 

Reporting Mock-ups: Week 3, Session 1 (60 mins): JMAN to present initial mock ups and gather feedback 

Reporting Mock-ups: Week 4, Session 2 (30 mins): JMAN to present refined mock ups and gather feedback 

Reporting Mock-ups: Week 5, Session 3 (30 mins): To be used as needed for final iterations 

Data Gap Assessment & Data Model: Week 4, Session 1 (60 mins): JMAN to present early findings from gap assessment 

Data Gap Assessment & Data Model: Week 5, Session 2 (60 mins): JMAN to present final assessment & process recommendations  

Final output alignment: Week 5 (45 mins): JMAN and Prescient management to review final output and align on messaging ahead of final readout 

Final Readout: Week 5 (120 mins): Final readout and next steps 

Data & Technical Leads 

Where possible, bi-weekly check-ins with a nominated Client “technical lead” who can support in ensuring the design and planning for the data platform is aligned and feedback is incorporated 

General support in coordinating data access and addressing blockers throughout engagement 

Relevant system owners (incl. individual brands / billing systems) 

Max. 30-minutes to complete a pre-workshop technical survey to minimise time required with individuals 

1-hour deep dive workshop (per system) to understand their systems, data availability, data quality and reporting processes 

 

Resource Commitment 

Resources: 

Blended team of Associate Partner, Architect, Engagement Manager, Consultants and Data Engineers 

 

Location of Services 

Location of Services: 

 

It is expected the work will be completed remotely and/or from JMAN’s offices:   

London Office: 10 Lloyds Avenue, London, EC3N 3AJ  

Chennai Office: Module 0104 (A), First Floor, C Block South, Tidel Park, 4 Rajiv Gandhi Salai, Taramani, Chennai-600 113, India  

New York Office: 1500 Broadway, New York, NY 10036 

 

Fees and Payment 

List Price Weekly Run Rate: 

£24,976 (+VAT) 

Engagement Total: 

£124,884 (+VAT) 

Discount: 

JMAN would be willing to offer a 30% first engagement discount as an investment in the relationship with Prescient. 

Discounted Weekly rate: 

£17,483 (+VAT) 

Discounted Engagement Total: 

£87,419 (+VAT) 

 

Contacts 

Client Engagement Manager: 

Rachael Farmer (rfarmer@prescienthg.com) 

Service Provider Engagement Manager(s): 

Harrison Tull (harrisontull@jmangroup.com) 

Gerard Pieterse (gerardpieterse@jmangroup.com) 

 

Subsequent Tasks 

Any subsequent tasks must be captured by a Change Order as set out in Schedule 1 to the Agreement. 

This SOW has been entered into by the parties on the Effective Date: 

 

 

 

.................................... 

Signed by Rachael Farmer for and on behalf of the Client. 

 

 

.................................... 

Signed by Richard Cowen for and on behalf of the Service Provider. 

 

"""

    passage_2 = ""
    return passage_1, passage_2


# Remove the if __name__ == "__main__" block to prevent execution when imported