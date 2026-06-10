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
Context[TW1.1]
Ridge & Partners LLP is a multi-disciplinary property services and construction consultancy providing infrastructure engineering, architectural, quantity surveying, and related professional services across the UK. Following investment from Horizon Capital in April 2023, Ridge has continued to experience significant growth, with revenues increasing from £65m in FY21 to £134m currently, representing a 100% increase in three years. While approximately 10-15% of this growth has come from acquisitions, the vast majority has been organic, with 12% organic growth in the last year despite challenging market conditions.
Ridge operates across approximately 12 offices in a matrix structure organized by both office location and service line. The business is structured around approximately 100 teams, with each team having a specific discipline and geography. The key service lines (5-6 in total) represent approximately 75-80% of revenues, including architecture, quantity surveying, and project management. The business serves roughly 800 active customers across diverse sectors including residential, public and private healthcare, advanced manufacturing, life sciences, F1, and data centres, with no significant customer concentration (largest customer representing approximately 5% of revenue). Ridge has strong customer retention, with 85% of revenue coming from repeat business, which has been a key driver of organic growth.
Ridge's current growth strategy includes continued organic expansion alongside a targeted M&A approach, with plans to complete 2-3 add-on acquisitions per year. The company has a history of acquisitions dating back to 2005, with recent acquisitions including Concert (29 people in 2023) and Jubb (100 people in November 2024). These acquisitions have been driven by various strategic rationales, including geographic expansion, service line enhancement, and sector expertise (such as data centers and engineering capabilities). Ridge typically takes 4-5 months to fully integrate acquisitions onto their systems, with Jubb currently operating on separate systems with planned migration in July 2025.

The company is currently upgrading core systems, with a new financial system (moving from Sage 200 to MS D365) due to go live in September/October 2025, a new CRM implementation in planning stages, and project management system improvements planned. They are also in the process of implementing Microsoft Fabric for improved reporting capabilities.
Despite this impressive growth trajectory, Ridge currently faces challenges in demonstrating where and how this growth is occurring across sectors, customers, and cohorts beyond anecdotal evidence. The business operates on a fixed fee model with a multiplier effect approach (as opposed to a more typical utilization model). While this multiplier structure drives clear targets and billability behaviors, timesheet compliance has historically been a challenge, affecting project profitability data quality.
Additionally, Ridge experiences significant challenges with data reconciliation between their project management system (Workspace) and financial reporting systems (currently Sage). A monthly "sludge journal" is required to adjust between these systems, creating difficulties in establishing a single source of truth. The business has identified the need for improved data quality, particularly around proper client classification, with no clear parent-child hierarchy properly defined (estimated 35,000 rows of data to clean). This becomes particularly challenging when tracking relationships where clients may have multiple special purpose vehicles (SPVs) or where project dynamics involve working for an end client initially, then transferring to a contractor. Ultimately, Ridge would like to be able to track “customer pathways” but also “project/site pathways”.
Ridge has engaged JMAN to provide a proposal for an initial scope of work which seeks to establish a foundation for high-quality commercial data to support business decision-making and prepare for an eventual transaction. This will focus on designing reporting solutions that provide clear visibility on growth drivers and value creation levers while addressing the data quality and reconciliation challenges that currently exist. There is particular interest in tracking cross-selling benefits after acquisitions, and demonstrating the repeatable nature of client relationships despite intermittent project delivery patterns. Whilst focusing on key growth drivers, the reporting solutions will ultimately deliver operational insights in the hands of the people who need data on a day-to-day basis. 

Overview
JMAN will provide a roadmap and plan to build a core reporting suite. This will focus on delivering reporting for different user groups: from operational/partner-level reporting to management and board-level reporting, all the way up to investor-reporting. The dashboards will also eventually be able to be leveraged to support the demonstration a compelling equity story for future investors, ensuring Ridge has one, single-source-of-truth for data and reporting. The reporting priorities and KPIs will be defined in collaboration with key Client stakeholders, absorbing existing requirements already defined and will incorporate JMAN’s recommendations from previous work building reporting for professional services businesses.
JMAN recognises that Ridge has already made progress with Power BI implementation and is moving toward Microsoft Fabric. Our approach will build upon these investments, ensuring that our data architect and infrastructure recommendations integrate with and enhance these existing platforms rather than replacing them. Additionally, we will be mindful of the upcoming system migrations, including the D365 migration in September/October 2025 and the CRM implementation, to ensure our recommendations align with and complement these strategic initiatives.
Our proposal is broken into two phases. Those proposal and statement of work covers the Design & Discovery Phase (outlined below). On completion of the Design & Discovery Phase, one of the deliverables will be a proposal and implementation plan, for a Reporting Build Phase 2.

Phase 1 – Design & Discovery

Outputs
•	Equity Story, Future Narratives, and Reporting Requirements: Align with the business (and Horizon) on the key narratives the business will want to present at exit. Ensure these are aligned with the reporting and contextual business requirements of the management team to operationally run and track performance. These narratives and reporting areas will be the foundation to develop the KPI framework.
•	“Metrics that Matter” KPI framework: Recommended metrics to provide critical reporting across the business and visibility on the “metrics that matter”, to help support the key equity narratives ahead of a future investment process. These KPIs will critically also provide management and operational visibility to support decision-making and value creation throughout the remainder of the hold. These metrics will be mapped across the reporting suite design, to identify at which level these should be surfaced, measured, and tracked. The KPI framework will absorb and build on any existing reporting.
•	Reporting suite design: Work collaboratively with key business stakeholders to align on the “north-star” vision of the end-state reporting landscape for Ridge, and develop a delivery roadmap for reporting, ensuring priority reports are delivered as part of Phase 2. This involves defining:
i.	User-groups: Who are the different user groups that will consume reporting at different levels of the business – e.g. Board/Investor, Management, and Operators (i.e. Partner/Division-leads, or Teams etc.)
ii.	Reporting pillars/verticals: Agreeing on the key pillars of reporting across the business that will surface the relevant insights – e.g. finance, customer, people/HR, project/operational, sales, etc.
iii.	Reports & tools: Across the different user-groups and reporting pillars/verticals, how will these be divided/presented in specific tools to allow the different user-groups visibility of what they require – e.g. a board report will likely aggregate the top-level KPIs across finance, customer, people etc. Whereas a partner report, might only include the relevant operational reporting, or a CFO pack only include the finance pillar of reporting.
•	Dashboard mock-ups: For the priority reporting suite/dashboard, ensure that the display of these KPIs and metrics provides the right level of granularity, insights are actionable, and provides the data clarity on an end-state goal for the data model and dashboards
•	Data model: Design a high-level data model that will satisfy the longer-term reporting requirements, and a detailed data model required to deliver the priority reporting use-case 
•	Data architecture and infrastructure design: A recommendation for the augmentation and development of data infrastructure to support the deployment of the platform for connection, ingestion, and consolidation of legacy, current, and new systems. The design will be cognizant of Ridge's ongoing buy-and-build strategy, it’s existing data infrastructure (i.e. Fabric), and will align with the planned system upgrades (D365 in September/October 2025, CRM implementation). We will work in close collaboration with Ridge technical teams on recommendations, to ensure the data platform and reporting suite can be owned and maintained by internal teams following delivery of the platform and reporting in Phase 2.
•	Data gap assessment and process recommendations: High-level assessment of data availability for priority reporting, identifying gaps in coverage to conduct a feasibility assessment during roadmap prioritisation. Where data is not (or poorly) available, work with stakeholders to provide data recommendations and identify areas for process improvement to improve quality and availability over time. This will consider changes required to unlock additional or future value-add use cases, where relevant.[EE2.1] As part of the Phase 2 plan, JMAN’s plan will provide recommendations on more advanced, centralized ways to clean or enrich data, being targeted on the required reporting data components. (i.e. using externally available data sources, or deploying GenAI, etc.). Depending on the extent of the cleaning required and the approach, this may add time to our typical Phase 2 timelines, but we'll make this clear in the Implementation Roadmap deliverable in Phase 1 and ensure we're aligned.[TW3.1]
•	Implementation plan: the above outputs packaged in a Phase 2 proposal for support to execute on the development and build out of a core reporting suite, underpinned by a best-in-class data platform/architecture. This will focus on delivering the suites incrementally, while harnessing and growing internal capability. This implementation plan will include integration of go-forward systems as well as historical data.

Benefits of Approach
•	Service Provider Professional Services Expertise – extensive experience building data platforms for PE-backed professional services businesses. Our work with similar businesses enables tailored insights on organic revenue growth, quality of earnings, customer acquisition costs, and service line profitability, all critical to Ridge's growth.
•	M&A Platform – final deliverables of a Build phase provide Ridge with a data and reporting suite for rapid integration (3-4 weeks) of new acquisitions without immediate system migrations. This supports Ridge's strategy of 2-3 add-on acquisitions annually and ensures consistent reporting despite potential legacy system differences.
•	Lasting Data Asset – a data platform and reporting suite is a lasting data asset for Ridge, this serves as a foundation for M&A and insights/reporting, ensuring Ridge is a mature, data-driven management team.
•	Single-Source-of-Truth Data & Reporting – across the complex data landscape and multiple entities, this approach leaves Ridge with a consolidated, trusted, single-source-of-truth data asset that is the foundation for data-led decision-making.
•	Leveraged for a Future Transaction – a data platform and reporting suite can serve as a data asset for future transactions, with two-fold effects: (i) easily serve up data for buy- and sell-side diligence, (ii) helps present the business as a data mature company with valuable data assets.
•	Expertise in Diverse Data Maturity Landscape – JMAN has extensive experience working with extremely acquisitive businesses, with a broad range of data maturities (e.g. Excel-based to system-based reporting) and challenges in cross-system reconciliation.

Approach
Week 0: Pre-kick off
Ensure JMAN has what they need to hit the ground running and are not blocked during the three-week project[EE4.1][TW4.2]
•	Data access: Work with Ridge to arrange full access to required systems/existing warehousing (Workspace, Sage, Power BI, Azure/Fabric), containing customer/revenue/operational data, plus any existing reports being generated on this data
•	Meetings schedule: Work with Ridge to book the required workshops and meeting cadences
•	Data architecture / infrastructure documentation: Liaise with internal technical stakeholders to receive all the existing documentation for reporting, infrastructure & systems landscape, and tech stack configurations, where these exist
•	Existing data infrastructure deep-dive: pre-kick off sessions with technical teams to dive into existing data architecture and infrastructure. 
•	Existing reporting review: Review current Power BI dashboards and reporting tools used by office managing partners to identify what is working well and where gaps exist.

Week 1-2: Requirements and reporting design
Define priority reports, key use cases, and align on KPIs to support central management and operational reporting, driving a data model that ensures accurate KPI calculations and effective data management.
•	Reporting suite design: Workshops with Ridge to define the report suite design end-state (user-groups, reporting pillars/verticals, reports and tools). Then clearly define the target use cases and key performance indicators (KPIs) for priority reporting. JMAN’s expectation is the primary priority for a Services Business will be customer and revenue reporting – this will be confirmed with Ridge in workshops. JMAN will bring an initial outline of this give the detailed discussion during the scoping workshops.
•	Absorb existing reporting and requirements: spend time understanding existing reports shared, including meetings with report owners to understand existing process, and understanding further ‘wish list’ of future KPIs Ridge wants to report on.
•	Going more granular: Confirming the required level of granularity for metrics and key segments/dimensions (i.e. entities, geographies, brands, partners, etc.). JMAN will have an initial sense of these based on the scoping workshop.
•	Calculation logic: Define the formulas and calculations required to derive priority KPIs and metrics from the data
•	Dashboard mock up design: Provide mock ups based on discussions with the management team and our prior experience designing professional services reporting suites
•	Current state: Understand the existing business terms, metric calculations, data sources, and reports being generated by Ridge, and revise KPIs / logic definition as required
•	Data platform workshop: Review any existing data infrastructure, tooling, softwares, and recommend a data platform design to meet the reporting requirements and serve as a scalable foundation for future use-cases
•	Align on priority future use cases: Align on how the development in the platform should be designed to service future second priority reporting and future use-cases

Week 2: Data source assessment and initial model design
Gain a clear understanding of current data sources, data points, and reporting processes that will support priority reporting. Begin development of the target state data model.
•	Data source review: Identify relevant data sources (Workspace, Sage, etc.) and tables that will feed into priority reporting. Specific focus on reconciliation between the project management system (Workspace) and financial reporting systems (Sage/D365), including analysing the current "sludge journal" process to understand the adjustments being made and their rationale.
•	Data gap assessment: Evaluate the availability of data for priority reporting, and where data is not available work with stakeholders to determine a path forward (e.g. automated extraction of data from invoices)
•	Data availability prioritization: Identify the most critical data coverage issues that need to be addressed to enable priority reporting, and provide recommendations or develop plans for the Phase 2 build on how these can be enriched or cleaned
•	Client hierarchy framework: Develop an initial framework for establishing a proper parent-child client hierarchy, including how to handle SPVs and projects where Ridge initially works for end clients and then for contractors.
•	Data model: Highlight the required relationships between data sources in the platform to be able to execute and create the calculation logic for priority reporting. Design the data model that accounts for Ridge's key dimensions/reporting matrix (i.e. teams, offices, and service lines).

Week 3: Solution design and implementation plan development
Finalize the data model design, develop implementation recommendations, and create a roadmap for execution of the data platform build/augmentation and priority use-case reporting build-out.
•	Data platform recommendation: Develop a data architecture recommendation that builds upon Ridge's investments in Power BI and the planned Microsoft Fabric migration[EE5.1] This will be developed in collaboration with Ridge technical teams, and agreed prior to the final read out.[TW6.1]
•	Iterate dashboard mock-ups: based on feedback from management, confirm draft dashboard mock-ups to help inform implementation plan and data model design.
•	Finalize data model: based on system learnings, feedback from management, and mock-up finalization, confirm the end-state data model design.
•	Data cleaning and enrichment recommendations: based on the data coverage and data gap assessment in Week 2, provide recommendations for and confirm approaches for tackling data challenges, cleaning, or enrichment in Phase 2 (e.g. external source, GenAI deployment). 
•	Implementation plan: Based on the current infrastructure Ridge has, design a build plan to deliver the priority core reporting. The implementation plan will align with timelines for planned system upgrades and existing reporting.
•	Other use cases: Highlight how the data platform design will support second priority reporting and additional use cases, for example entity-level operational sales & pipelines reporting, project profitability analytics, or more advanced ML/AI expansion or retention prediction engines.

A.	Timelines
Week 0 Start Date:	24th March, 2025
Week 1 Start Date:	31st March, 2025
Timelines:	3-weeks
Services Completion Date:	18th April, 2025

B.	Assumptions & Requirements
Out of scope:	JMAN will not start any technical development of the build phase during the initial engagement. This involves any data architecture set-up, tool provisions, system connectivity, or dashboard development.
Required support from data source owners:	•	JMAN will have access to extracts and source systems ahead of kick off for the data sources included in scope
•	JMAN has access to data system owners / providers to resolve any clarifications around data availability and end points
Required support and time from the client:	These may be revised based on the pre-kick off sessions, but our current requirement from Ridge would be:[EE7.1][TW7.2]
•	Ed Ethelston, Adrian O’Hickey, Julie Guppy, Neil Lovett, Phil Baker and other key members of the management team, and potentially Horizon representation
o	Week 1: 90-minute KPI review session – JMAN will prepare relevant use-cases, reports, and metrics following the scoping workshops
o	Wek 1: 60-minute KPI follow-up – second deep-dive in Week 1 to continue iterating on KPIs
o	Week 2: 60-minute KPI testing – deep-dive on logic to deliver prioritized KPIs
o	Week 2: 90-minute dashboard mock-up review session, plus potential follow-ups based on iterative feedback
o	Week 2: 60-minute technical recommendation testing, to ensure pre-alignment with Ridge technical team before final recommendations
o	Week 3: 60-minute final readout and recommendation walkthrough
o	1-hour weekly Steerco update to ensure discovery and recommendations are aligned with the group
•	Data & Technical Leads
o	Where possible, bi-weekly check-ins with a nominated Client “technical lead” who can support in ensuring the design and planning for the data platform is aligned and feedback is incorporated
o	General support in coordinating data access and addressing blockers throughout engagement
•	Relevant system owners (incl. individual brands / billing systems)
o	Max. 30-minutes to complete a pre-workshop technical survey to minimise time required with individuals
o	1-hour deep dive workshop (per system) to understand their systems, data availability, data quality and reporting processes

C.	Resource Commitment
Resources:	Blended team of Associate Partner, Architect, Engagement Manager, Consultant and Solutions Consultant

D.	Location of Services
Location of Services:
	It is expected the work will be completed remotely and/or from JMAN’s offices:  
•	London Office: 10 Lloyds Avenue, London, EC3N 3AJ 
•	Chennai Office: Taj Wellington Mews, TRIL Info park Limited, Old Mahabalipuram Road, Taramani, Chennai 600113
•	New York Office: 1500 Broadway, New York, NY 10036

E.	Fees and Payment
List Price Weekly Run Rate:	£16,590 (+VAT)
Engagement Total:	£49,770 (+VAT)
Discount:	JMAN would be willing to offer a 15% first engagement discount as an investment in the relationship with Ridge which will continue into the next phase of work.
Discounted Engagement Total:	£42,305 (+VAT)

F.	Contacts
Client Engagement Manager:	Ed Ethelston (edethelston@ridge.co.uk)

Service Provider Engagement Manager(s):	Harrison Tull (harrisontull@jmangroup.com)


G.	Subsequent Tasks
Any subsequent tasks must be captured by a Change Order as set out in Schedule 1 to the Agreement.
This SOW has been entered into by the parties on the Effective Date:



....................................
Signed by Ed Ethelston for and on behalf of the Client.	

....................................
Signed by Richard Cowen for and on behalf of the Service Provider.

"""

    passage_2 = ""
    return passage_1, passage_2


# Remove the if __name__ == "__main__" block to prevent execution when imported