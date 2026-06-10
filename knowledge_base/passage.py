passage_1 = """
Context & understanding your needs 

Sabio are a customer experience specialist, who have traditionally been rooted in Enterprise Contact Centre with differentiated bolt-on services of AI-powered automaton and data analytics. Sabio have planned for an transaction event in year of time. The focus of the business has changed over the past 12 months to index further on AI-powered automation as the core proposition with contact centre and data analytics as cross-sell opportunities. 

AI-automation as a proposition offers a higher margin for Sabio and is a key equity narrative to demonstrate increasing revenue, margin and profitability in this proposition. 

To articulate and evidence key equity narratives ahead of a transaction event, Sabio would like to build out exit data cubes that enable customer, product and project level revenue and profitability reporting. Getting to this level of detail is critical to Sabio being able to a) demonstrate their key growth stories and b) ensure that management and operational teams have the right data available to support decision making. 

Sabio have a complex systems landscape, with multiple ERPs / finance systems, operational system & CRM instance containing pipeline and annuity contracts. The key data challenges that Sabio have identified from the current system landscape are: 

Historical revenue data is not split out by pillar (AI, data analytics & contact centre) and retrospectively achieving this will be complicated due to varying levels of granularity across systems 

There is not a consistent customer identifier across systems, with issues arising such as duplicates, complex corporate structures and pseudonyms 

There is existing data architecture in place which brings in data from some, but not all, of Sabio's source systems into an Azure synapse data lake. Sabio's CTO has begun to develop roadmap and thinking on a migration to Microsoft Fabric. The data lake does not currently contain data from either of Sage 200 or Microsoft Dynamics NAV. The data that is loaded into the data lake is done so through a direct ETL process, with no transformations applied within the data lake. Connections are made directly from Power BI to the data lake for reporting, with business logic and transformations done within Power BI. 

Existing reporting exists at Sabio within Salesforce, Power BI and excel, that offers visibility into several important metrics, however, has gaps to the target metrics and granularity Sabio would like to evidence at a future transaction event: 

Salesforce reports are built and managed by the commercial ops team, and allow visibility into bookings, pipelines and performance against targets. The consensus is that the data is good for historic bookings and near term (in quarter) pipeline, however pipeline further out is less reliable 

Power BI reports include visibility on professional services revenue and managed service revenue and renewals. The Power BI reports provide granular detail, however a challenge identified by Sabio is the ability to view high-level, but important, customer and product revenue trends. 

There is currently a revenue cube which is maintained in excel, however this is not segmented by pillar as this data has not been historically available 

 

Significant thinking by Sabio has been put into identifying the KPIs and growth narratives that will be critical for a future transaction event. The support that is needed is focused on assessing the data available across systems and designing data models and flows that will enable Sabio to consistently and accurately produce the target reporting. 

This will be best served through a Diagnostic and Design phase in which Sabio would want an assessment of current gaps in data and processes, define the required data models and agree a best-in-class supporting technical architecture that can support both day-to-day management reporting and a transaction. 

 

Outcomes 

Sabio would like a clear path to being able to demonstrate key growth narratives through design, and eventual implementation, of exit cubes to demonstrate: 

Key Customer journeys and evolution of products / repeat revenue profiles over time including upsell, NRR & GRR and cross-sell of strategically important propositions like AI and data & traditional Contact Center, as well as the change in revenue mix across the three key pillars 

Customer, product, project level profitability in an exit cube that links jobs back to invoicing to ascertain at a more granular level the profitability for Sabio across customers and products 

Much of the thinking on KPIs and key growth narratives has been done already by Sabio, and therefore the focus for Sabio is on understanding how to leverage, clean and model their data to evidence this through reporting. This will be the main emphasis of the initial engagement, to give clarity on the path to having best-in-class data models that can support accurate and automated production of key KPIs. 

This journey will be outlined in an implementation roadmap, and will factor in key foundational elements such as a) the design of versatile data models, b) data clean up and remediation c) suggested data capture and process changes and d) adaptions to existing data infrastructure / architecture to enable automated reporting from a best-in-class data platform 

Specific focus will be applied to how we can apportion historical revenue to each pillar and how customers are consistently mapped across systems 

Deliverables 

Support with consolidating the definitions of the "metrics that matter" and reporting outputs that are crucial to demonstrating Sabio's growth narratives. (Summarising, agreeing and documenting the thinking that is already in place) 

Design and documentation of the versatile data models, detailing in-scope data sources (e.g., Salesforce, Sage 200 etc.,) and their end-to-end data flows from source systems to final output tables, with consideration for future reporting use cases 

A data gap assessment focusing on the availability, granularity, and time horizons for key KPIs and dimensions and a remediation plan for any data quality gaps, process changes or changes to system data capture that are required to build out the data cubes 

A comprehensive review and design and target future state data architecture that will facilitate automated and reconciled data cubes 

A phased delivery and implementation roadmap that outlines the short to medium term plan for investing in data and reporting across both reporting use cases (e.g. repeat revenue bridges, profitability reporting) and foundational infrastructure (e.g. data platform, governance, and processes)  

Alongside the core set of deliverables, JMAN will also support to provide an opinion on: 

Sabio's target operation model 

Exiting BI reports and their place in the future state data and reporting architecture 

 

'Metrics that matter' Definition & Alignment: building on the thinking Sabio have done already on important metrics and report design, we would support with definition alignment and documentation through an initial workshop at the beginning of the project to frame the data model design and focus our data assessment on the most important metrics and sources 

 

Conceptual Data Model: providing a comprehensive view of all in scope data sources, including the definition of key entities, relationships, and end-to-end data flows from source systems through to final output tables. The model will be designed with scalability and flexibility in mind to support future reporting and analytics use cases. 

 

KPI Feasibility & Data Gap Assessment: a review of Sabio's ability to report on the defined KPIs, based on the quality, completeness, and granularity of data captured in source systems. Highlights key data gaps and recommendations to address them. 

 

Tech Architecture Review & Design: recommendations for a best-in-class design of future state architecture including cloud data platform, scalable pipeline design, and governance structures that future-proof reporting infrastructure. Sabio have existing Power BI reporting that is critical to operations, so JMAN will design an architecture that enables continuity or reporting without building a second source of truth. 

 

Strategic Implementation Roadmap: a clear, time-bound plan To delivery against Sabio's reporting ambitions – from establishing best-in-class data foundations through to dashboard development and governance implementation. Considers other strategic business priorities, resourcing, scalability and potential for a future transaction timeline. 

 

 

Scope Data Source 

The systems in scope for the design and discovery are: 

# 

Source system 

Purpose 

Region (If Applicable) 

Contact 

1 

Sage 200 

Finance System 

UK 

Andrew 

2 

Microsoft Dynamics NAV 

Finance System  

Europe 

Carlos 

3 

Salesforce 

Bookings & Contracts System 

 

Jason 

4 

Certinia / Finance Force 

Operations System 

 

Jason 

5 

ServiceNow 

Managed Service Support System (Ops) 

 

Jason 

6 

Workday 

FP&A System 

 

Jason 

7 

IRIS 

HR & Payroll System 

 

Jason 

8 

Azure Data Lake 

Data Lake 

 

Gavin 

 

Benefits of Approach 

Through partnership with JMAN and the deliverables outlined, we will bring the following benefits: 

Single-Source-of-Truth (SSOT) Data & Reporting – across the complex data landscape and multiple systems, this approach leaves Sabio with a consolidated, trusted, single-source-of-truth data asset that is the foundation for a successful transaction process and data-led decision-making, including the housing of key business logic and data governance practices, which enable consistent reporting and alignment across the business. 

De-risked Transaction Execution – SSOT enables consistency across all bidder-facing figures and can be easily updated throughout the process as needed. This eliminates the data preparation concerns for the management team, allowing them to focus on executing the transaction. 

Service Provider Expertise – extensive experience building data cubes for acquisitive, PE-backed businesses to support transaction processes. 

Expertise in Diverse Data Maturity Landscape – JMAN has extensive experience working with acquisitive businesses, with a broad range of data maturities (e.g. Excel-based to system-based reporting). 

Approach 

Mobilisation: Pre-kick off 

Ensure JMAN has what they need to hit the ground running and are not blocked during the four-week project 

Kick-off meetings: An initial meeting upfront to assess the status of key resources and clarify the access and engagement needed from key stakeholders to ensure success. 

Data access and requests: Work with Sabio to arrange full access to required systems/existing warehousing, containing customer/revenue/operational data, plus any existing reports being generated on this data. See specific data request list in Section C. 

Meetings schedule: Work with Sabio to book the required workshops and meeting cadences – meeting schedule outlined in supporting document shared with Sabio, 

Data architecture / infrastructure documentation: Liaise with Rob (CTO) and other internal technical stakeholders to receive all the existing documentation for reporting, infrastructure & systems landscape, and tech stack configurations, where these exist. 

Weeks 1: Understanding Sabio's Current Data Landscape and Target Metrics 

Consolidate and agree on key KPIs definitions, and begin to dive into the systems landscape to build out the target-state architecture and data model design 

KPI Workshop: A single-day workshop to consolidate and document the existing thinking done on key KPIs and growth narratives, including understanding existing business terms, metric calculations, data sources and systems. This will ensure consistency of definitions and give JMAN the context required to build out appropriate data model designs. 

Data architecture and infrastructure review: Understand the current architecture and infrastructure, identify key challenges and constraints, and recommend best-in-class Azure tooling and services. JMAN will work with Rob to understand the existing landscape, and any future development / investments, to assess the suitability of these for the reporting Sabio desire. 

Systems workshops: Conduct deep dive sessions with system owners to understand data required and the data currently captured to feed priority reporting from Salesforce, Sage, Certinia and other key systems. This will support JMAN in understanding how data is generated and used, how systems interact both through existing integrations and manual rekeying of data, and where the main gaps in data flows exist. 

Going more granular: Reviewing and aligning on the required level of granularity for metrics and key segments/dimensions, including period of tracking and use-cases for the future state reporting. This will follow on from the KPI workshop and produce an output showing the targeted depth and cuts of key metrics that Sabio want available at a future transaction event. 

 

Weeks 2-3: Understand Sources and Data Models 

Gain a clear understanding of current data sources, data points, and processes that will feed the target exit cube data models. Provide recommendations to improve data availability & quality and design target state data model. 

Conceptual Data model: Provide a documentation of all in scope data sources, including the definition of key entities, relationships, and end-to-end data flows from source systems through to final output tables. 

Data source review: Identify relevant data sources & tables that will need to feed into priority reporting. JMAN will conduct a forensic review of the existing data quality and granularity of data required to produce the target metrics. 

Feasibility assessment: Define business rules for what good looks like for each of the required attributes and validate the availability and quality of data against these rules and where data is not available work with stakeholders to determine a path forward. 

Future-state architecture design: JMAN will work with the CTO and other technical stakeholders to build out Sabio's target future state architecture that will underpin management & operational reporting and preparation for a future transaction event. This architecture, when built, will be built in Sabio's environment and will incorporate and supplement existing systems/tooling, roadmaps and strategic thinking from a technical perspective. 

 

Week 4 only: Delivery Plan & Roadmap 

A delivery plan to build the exit cubes and reporting artefacts 

Data governance & process recommendations: Identify areas for process and data recommendations to improve quality and data availability for the attributes for the metrics that matter, which will then be actioned during a subsequent build. 

Data & Reporting Roadmap: Outline prioritised roadmap for broader reporting suite including key dependencies to deliver best-in-class data and reporting foundations. 

 

Timelines 

Services start date: 

Mobilisation week: 16th March 2026 

Week 1: 23rd March 2026 

Services completion date: 

21st April 2026 

Out of Scope 

Not included in the Services: 

JMAN will not start any technical development of the build phase during the initial engagement. This involves any data architecture set-up, tool provisions, system connectivity, or dashboard development. 

 

JMAN will perform the gap assessment and KPI feasibility on only the source systems listed in this scope. If it is determined that additional source systems need to feed into the target data cubes, additional time may be required that could accrue additional costs 

 

 

Resource Commitment 

Resources: 

A blended team of consulting and engineering resources including an engagement manager and oversight from an Associate Partner and a Principal Architect 

Location of Services 

Location of Services: 

 

JMAN Group Limited (London Office): 10 Lloyds Avenue, London, EC3N 3AJ, United Kingdom 

JMAN Digital Services Private Ltd (Chennai Office): Module 0104 (A), First Floor, C Block South, Tidel Park, 4 Rajiv Gandhi Salai, Taramani, Chennai-600 113, India 

Fees and Payment  

Total Charges: 

£10,370 / week + VAT (inclusive of 40% discount as an investment in a partnership) 

£41,480 + VAT (total phase cost) 

 

 

Contacts 

Client Engagement Manager: 

Michael Andrews michael.andrews@sabiogroup.com 

 

Service Provider Engagement Manager: 

John Chapple Gill johnchapplegill@jmangroup.com 

 

Prerequisites and Assumptions 

JMAN team will require access to the in-scope source systems to conduct the scope of work. This access must be provisioned before the start of week1 to ensure that timelines are adhered to. Delays in providing access to all the source systems may cause overall timelines to extend at additional costs. 

It is expected that to access the source systems and data lake, the JMAN team members on the project will be provided with Sabio accounts on a named basis. No data will leave Sabio's azure environment or the source system. If extracts are required these will be stored on Sabio's Sharepoint in a folder that the JMAN team can have read access to.  

Its is also expected that the JMAN team will require AVDs or Cloud PCs to be created and allocated to access data. In this case, these must be provisioned ahead of week 1 starting to ensure there are no delays to the scheduled timelines. 

Subsequent Tasks 

Any subsequent tasks must be captured by a Change Order as set out in Schedule 1 to the Agreement. 

This SOW has been entered into by the parties on the Effective Date: 

 

 

 

.................................... 

Signed by Darren Hayward for and on behalf of the Client. 

 

 

.................................... 

Signed by Richard Cowen for and on behalf of the Service Provider. 

 
"""