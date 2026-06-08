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
# Schema
# =====================================================

class SubSection(BaseModel):
    subsection_name: str
    content: str


class Section(BaseModel):
    section_name: str
    content: str = ""
    subsections: List[SubSection]


class ProposalKB(BaseModel):
    solution: str
    region: str
    sections: List[Section]


# =====================================================
# LLM Setup — Azure OpenAI (replaces Groq)
# =====================================================

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_MODEL_NAME_1"),
    api_version="2023-06-01-preview",
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
Description of the Services 

Context 

Saffery is a UK-based chartered accountancy and advisory firm with roots extending back to 1855, making it one of the country’s longest-established independent professional services firms. Today, the organisation operates as a significant mid-tier practice with multiple offices across the UK and international presences in markets such as Guernsey, Geneva, Zurich, and the Cayman Islands. Saffery is a member firm of Nexia International, a global network of independent accounting and consulting practices, which broadens its reach and cross-border advisory capacity.  

Saffery provides a comprehensive suite of services that cover the core needs of corporate and private clients across diverse sectors: 

Audit and Assurance, ensuring regulatory compliance and financial transparency.  

Tax Advisory & Compliance, from personal tax and corporate tax planning to transfer pricing and R&D incentives.  

Accounting Services, including bookkeeping, financial statements preparation, and reporting support.  

Business and Transaction Advisory, encompassing due diligence, deal support, and exit readiness planning.   

Specialist Sector Practices, such as sports and entertainment, real estate, professional practices, not-for-profit, and international/high-net-worth clients.  

During its evolution, Saffery has selectively expanded its capability and reach through strategic actions, including the acquisition of specialist teams (such as the Film & TV unit from a competitor, boosting its sports and entertainment advisory expertise) and the establishment of international offices, enhancing its ability to serve clients with global footprints.  

The firm’s partner-led, people-centric model and its emphasis on deep, long-standing client relationships are central to its value proposition. Saffery’s advisory approach is built around high-touch engagement, sector expertise, and trusted continuity over time, attributes that underpin client loyalty and recurring revenue streams. 

As Saffery enters a period of exit preparation, the firm is focused on sharpening how its performance and value creation story are articulated to prospective investors. Central to this is building a clear, defensible view of customer and revenue dynamics that evidence revenue quality, client durability, margin drivers, and scalability within its partner-led model. Enhanced reporting and analytics will enable management to translate deep client relationships and sector expertise into a compelling, data-backed equity narrative ahead of exit. 

 

Overview 

JMAN will provide a roadmap and plan to build a customer cube, a customer-centric multi-dimensional data model, focusing on delivering historic customer reporting for a transaction eventdifferent user groups: from operational/partner-level reporting to management and board-level reporting, all the way up to investor-reporting. The dashboards will support what is required for transaction diligence, ensuring Saffery has one, single-source-of-truth for data and reporting.  The reporting priorities and KPIs will be defined in collaboration with key Client stakeholders, absorbing existing requirements, and will incorporate JMAN’s recommendations from previous work building clientcustomer reporting for professional services businesses. 

JMAN recognises that Saffery has already invested in developing a Microsoft Fabric data lake that stores PMS data (via API) and HR data (via batch uploads), and that this data is being used for reporting. Saffery have also indicated a preference for operating within the Microsoft ecosystem, with a preference for and Power BI reporting. Our approach will build upon these frameworks, ensuring that our data architecture and infrastructure recommendations integrate with and enhance existing platforms rather than replacing them.  

Our proposal is broken into two phases. This proposal and statement of work covers the Design & Discovery Phase (outlined below). On completion of the Design & Discovery Phase, one of the deliverables will be a proposal and implementation plan for a customer cube build (Phase 2). 

 

Outputs 

Equity Story, Future Narratives, and Reporting Requirements: align with the business (and investors) on the key narratives the business will want to present at exit. Ensure these are aligned with the reporting and contextual business requirements of the management team to operationally run and track performance. These narratives and reporting areas will be the foundation to develop the KPI framework. 

“Metrics that Matter” KPI framework: Recommended metrics to provide critical reporting across the business and visibility on the “metrics that matter”, to help support the key equity narratives ahead of a future investment process. These KPIs will critically also provide management and operational visibility to support decision-making and value creation throughout the remainder of the hold. These metrics will be mapped across the reporting suite design, to identify at which level these should be surfaced, measured, and tracked. The KPI framework will absorb existing reporting requirements already shared with JMAN including the Finance Board Report, CPO Report and Power BI reports and future requirements e.g. revenue / client metrics, staff and partners. 

Reporting suite design: Work collaboratively with key business stakeholders to align on the “north-star” vision of the end-state reporting landscape for Saffery. This involves defining: 

User-groups: Who are the different user groups that will consume reporting at different levels of the business – e.g. Board/Investor, Management, and Operators (i.e. Partner/Division-leads, or Sales teams etc.) 

Reporting pillars/verticals: Agreeing on the key pillars of reporting across the business that will surface the relevant insights – e.g. finance, customer, people/HR, project/operational, sales, etc. 

Reports & tools: Across the different user-groups and reporting pillars/verticals, how will these be divided/presented in specific tools to allow the different user-groups visibility of what they require – e.g. a board report will likely aggregate the top-level KPIs across finance, customer, people etc. Whereas a partner report, might only include the relevant operational reporting, or a CFO pack only include the finance pillar of reporting. 

Client Cube Design: Work collaboratively with key business stakeholders to align on the vision of the Client Cube and associated reporting landscape for Saffery. This involves defining: 

User Groups: Who are the different user groups that will consume reporting at different levels of the business – e.g. Board/Investor, Management, and Operators (i.e. Partner/Division-leads, or Teams etc.) 

Reports: Across the different user-groups how will specific, relevant and valuable insights be divided/presented to allow visibility to the different user groups. 

Dashboard mock-ups: For the priority Client reporting suite/dashboard areas, ensure that the display of these KPIs and metrics provides the right level of granularity, insights are actionable, and provides the data clarity on an end-state goal for the data model and dashboards 

Data model: Design a data model that would satisfy all the reporting/insight requirements irrespective of order or phasing of delivery. 

Data Gap Assessment and Process Recommendations: Assessment of data availability for Client Cube build and reporting, identifying gaps in coverage to conduct a feasibility assessment during implementation planning. Where data is not (or poorly) available, work with stakeholders to provide data recommendations and identify areas for process improvement to improve quality and availability over time. This will consider changes required to unlock additional or future value-add use cases, where relevant.   

Data architecture and infrastructure design: Recommendation for new or augmentation of data infrastructure to support the deployment of the platform for connection, ingestion and consolidation of legacy, current and new systems. The design will be cogniszant of Saffery’s ongoing buy-and-build strategy. 

Implementation plan: the above outputs packaged in a Phase 2 proposal for support to execute on the development and build out of a core reporting suite, underpinned by a best-in-class data platform/architecture. This implementation plan will include integration of go-forward systems as well as historical data. 

 

Benefits of Approach 

Service Provider Professional Services Expertise – extensive experience building data platforms for acquisitive, PE-backed professional services and accountancy businesses. 

M&A Platform – final deliverables of a Build phase leave Saffery with a data and reporting suite that allows rapid integration (3-4 weeks) of a new acquisition into reporting, without requiring system migrations. 

Lasting Data Asset – a data platform and reporting suite is a lasting data asset for Saffery, this serves as a foundation for M&A and insights/reporting, ensuring Saffery is a mature, data-driven management team. 

Single-Source-of-Truth Data & Reporting – across the complex data landscape and multiple brands, this approach leaves Saffery with a consolidated, trusted, single-source-of-truth data asset that is the foundation for data-led decision-making. 

Leveraged for a Future Transaction – a data platform and reporting suite can serve as a data asset for future transactions, with two-fold effects: (i) easily serve up data for buy- and sell-side diligence, (ii) helps present the business as a data mature company with valuable data assets. 

Expertise in Diverse Data Maturity Landscape – JMAN has extensive experience working with extremely acquisitive businesses, with a broad range of data maturities (e.g. Excel-based to system-based reporting). 

 

Approach 

Week 0: Pre-kick off 

Ensure JMAN has what they need to hit the ground running and are not blocked during the three-week project 

Data Access: Work with Saffery to arrange full access to required systems/existing warehousing (Microsoft Fabric, Power BI), containing customer data, plus existing reporting being generated on this data. Specific attention to be paid to reconciliation sources to ensure Phase 2 outputs align. 

Meetings Schedule: Work with Saffery to book the required workshops and meeting cadences. 

Data Architecture / Infrastructure Documentation: Liaise with internal technical stakeholders to receive all the existing documentation for reporting, infrastructure & systems landscape, and tech stack configurations, where these exist. 

Existing Data Infrastructure Deep-Dive: Build on initial sessions to dive into existing data architecture and infrastructure.  

Existing Reporting Review: Build on initial sessions to review current Power BI dashboards and reporting tools used by key stakeholders to identify successes and gaps.  

 

Week 1-2: Requirements and Customer Cube Design 

Define customer reports and align on KPIs to support reporting, driving a data model that ensures accurate KPI calculations and effective data management. 

Current State: Review current state reporting, and define business terms, requirements, and processes, as well as metric calculations, data sources, and reports being generated by Saffery. Revise KPIs and logic definition as required, and scope further ‘wish list’ of future KPIs Saffery may want to report on. 

Customer Cube Design: Workshops with Saffery to define the customer cube design end-state (user-groups and reports). Then clearly define the target use cases and key performance indicators (KPIs) for customer reporting. JMAN will bring an initial outline of customer reporting and conduct detailed discussion during these scoping workshops. 

Going More Granular: Confirm the required level of granularity for metrics and key segments/dimensions (customer bands, industry, service line etc.) JMAN will have an initial sense of these based on week 0 activities. 

Calculation Logic: Define the formulae and calculations required to derive customer reporting KPIs and metrics from the data. 

Data Platform Workshop: Review existing data infrastructure, tooling, and software to surface requirements for a data platform design that meets the reporting requirements and serves as a scalable foundation for future use-cases.  

Dashboard Mock Up Design: Provide mock ups based on discussions with the management team and our prior experience designing customer reporting dashboards. 

 

Week 2: Data Source Assessment and Initial Model Design 

Gain a clear understanding of current data sources, data points, and processes that will support customer reporting. Begin development of the target state data model. 

Data Source Review: Identify relevant data sources that will feed into customer reporting. Specific focus on ensuring capability for reconciliation between key metrics and P&L. 

Data Gap Assessment: Evaluate the availability of data for customer reporting, and where data is not available work with stakeholders to determine a path forward. 

Data Availability Prioritisation: Identify the most critical data coverage issues that need to be addressed to enable customer reporting and provide recommendations or develop plans for the Phase 2 build on how these can be enriched or cleaned. 

Data model: Highlight the required relationships between data sources in the platform to be able to execute and create the calculation logic for customer reporting. Design the data model that accounts for Saffery's key dimensions/reporting matrix. 

Iterate Customer Cube mock-ups: Based on feedback from management, confirm draft dashboard mock-ups to help inform implementation plan and data model design. 

 

Week 3: Solution Design and Implementation Plan Development 

Finalize the data model design, develop implementation recommendations, and create a roadmap for execution of the data platform and customer reporting build. 

Data cleaning and enrichment recommendations: Based on the data gap and availability assessments in Week 2, provide recommendations and confirm approaches for tackling data challenges, cleaning, or enrichment.  

Data Platform Recommendation: Develop a data architecture recommendation that supports and enhances the customer cube and facilitates seamless integration into existing data infrastructure. 

Finalise data model: Based on system learnings, feedback from management, and mock-up finalization, confirm the end-state data model design. 

Implementation plan: Based on the current infrastructure Saffery has, design a build plan, including associated costs, to deliver customer reporting. 

 

Timelines 

Services start date: 

9th March 2026 

Services completion date: 

27th March 2026 

 

Assumptions & Requirements 

Out of scope: 

JMAN will not start any technical development of the build phase during the initial engagement. This involves any data architecture set-up, tool provisions, system connectivity, or dashboard development. 

Required support from data source owners: 

JMAN will have access to extracts and source systems ahead of kick off for the data sources included in scope 

JMAN has access to data system owners / providers to resolve any clarifications around data availability and end points 

Required support and time from the client: 

These may be revised based on the pre-kick off sessions, but our current requirement from Saffery would be: 

TBD names of Saffery management team other key members of the management team (e.g. COO, CRO), and potentially Apiary representation 

Week 1: Initial 2-hour reporting requirements prioritisation workshop and business context deep-dive (i.e. brand/entity walkthrough, service hierarchy, etc.) 

Week 1: 90-minute KPI review session – JMAN will prepare relevant use-cases, reports, and metrics following first workshop 

Week 2: 60-minute KPI testing (smaller group) – deep-dive on logic to deliver prioritized KPIs 

Week 2: 60-minute dashboard mock-up review session, plus potential follow-ups based on iterative feedback 

Week 5: 90-minute final readout and recommendation walkthrough 

1-hour weekly Steerco update to ensure discovery and recommendations are aligned with the group 

Data & Technical Leads 

Where possible, bi-weekly check-ins with a nominated Client “technical lead” who can support in ensuring the design and planning for the data platform is aligned and feedback is incorporated 

General support in coordinating data access and addressing blockers throughout engagement 

Relevant system owners (incl. individual brands / billing systems) 

Max. 30-minutes to complete a pre-workshop technical survey to minimise time required with individuals 

1-hour deep dive workshop (per brand) to understand their systems, data availability, data quality and reporting processes. Where brands share systems (e.g. ERP/CRMs) JMAN can combine workshops to reduce time. 

An available contact per brand/system available during week 3 and 4 to address any clarification questions 

 

Resource Commitment 

Resources: 

Blended team of Associate Partner, Architect, Engagement Manager, Consultant and Solutions Consultant 

 

Location of Services 

Location of Services: 

 

It is expected the work will be completed remotely and/or from JMAN’s offices:   

London Office: 10 Lloyds Avenue, London, EC3N 3AJ  

New York Office: 1500 Broadway, New York, NY 10036 

Chennai Office: Taj Wellington Mews, TRIL Info park Limited, Old Mahabalipuram Road, Taramani, Chennai 600113 

 

Fees and Payment 

Phase 1 List Price Weekly Run Rate: 

£15,75021,655 (+VAT) 

Engagement Total: 

£64,96563,000 (+VAT) 

Discount: 

JMAN would be willing to offer a 15% first engagement discount as an investment in the relationship with Saffery which will continue into the next phase of work. 

Phase 1 Discounted Engagement Total: 

£54,97553,550 (+VAT) 

Indicative Phase 2 Weekly Run Rate: 

£22,000 (+VAT)TBD 

 

Contacts 

Client Engagement Manager: 

TBD : email Jonathan O’Brien: Jonathan.OBrien@saffery.com 

Julie Berry: Julie.Berry@Saffery.com 

Service Provider Engagement Manager(s): 

Natalie Cramp: nataliecramp@jmangroup.com 

Gerard Pieterse: gerardpieterse@jmangroup.com 

 

Subsequent Tasks 

Any subsequent tasks must be captured by a Change Order as set out in Schedule 1 to the Agreement. 

This SOW has been entered into by the parties on the Effective Date: 

 

 

 

.................................... 

Signed by TBD Jonathan O’Brien for and on behalf of the Client. 

 

 

.................................... 

Signed by Richard Cowen for and on behalf of the Service Provider. 

 
"""

    passage_2 = """
"""
    return passage_1, passage_2