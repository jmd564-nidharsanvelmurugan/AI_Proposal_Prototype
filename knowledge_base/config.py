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
Proposal Document
 
1 Business Context
 
Any Hour Group, LLC operates as a B2B SaaS provider within the United States, delivering technology solutions tailored to meet the evolving needs of its enterprise clients. The company's business model centers on subscription-based software offerings, which necessitate a robust and scalable data infrastructure to support ongoing customer engagement and retention efforts.
 
As a portfolio company under a private equity fund, Any Hour Group, LLC is positioned at a critical juncture where optimizing operational efficiencies and maximizing customer lifetime value are paramount. The existing data platform infrastructure provides a foundational capability for advanced analytics and business intelligence, enabling the organization to monitor key performance indicators and respond proactively to market dynamics.
 
The focus on churn reduction underscores the strategic importance of leveraging data-driven insights to enhance customer retention. This emphasis aligns with the broader commercial imperative to sustain recurring revenue streams and drive long-term growth within a competitive SaaS landscape. The project's design and discovery phase will build upon the current data platform to deepen understanding of customer behavior and identify actionable opportunities to mitigate attrition risks.
 
2 Our Understanding of your needs
 
2.1 Problem Statement
 
Any Hour Group, LLC, operating as a B2B SaaS provider within the US market, is currently facing challenges related to customer churn. As a portfolio company under a private equity fund, the imperative to optimize customer retention and maximize lifetime value is critical. Despite having an existing data platform infrastructure, the organization requires enhanced capabilities to leverage data effectively for churn analysis and mitigation. The complexity of integrating disparate data sources and extracting actionable insights has limited the ability to proactively address churn risks and inform strategic decision-making.
 
2.2 Proposed Solution
 
To address these challenges, we propose a comprehensive due diligence approach focused on the design and discovery of an advanced data platform solution tailored to churn management. This solution will:
 
• Conduct a thorough assessment of the current data platform to identify gaps and opportunities for enhancement.
 
• Develop a robust data architecture that integrates relevant customer, usage, and transactional data to enable holistic churn analysis.
 
• Implement advanced analytics and machine learning models to predict churn propensity with high accuracy.
 
• Establish intuitive reporting and visualization tools to empower stakeholders with real-time insights into churn drivers and trends.
 
• Align data governance and quality frameworks to ensure reliability and compliance across the data lifecycle.
 
2.3 Alignment with Any Hour Group, LLC's Needs
 
This solution is precisely aligned with Any Hour Group, LLC's strategic objectives and operational context:
 
• Enhances Existing Infrastructure: Builds upon the current data platform, leveraging existing investments while addressing critical limitations.
 
• Supports PE Fund Objectives: Provides the private equity stakeholders with transparent, data-driven insights to monitor portfolio performance and value creation.
 
• Focuses on Churn Reduction: Directly targets the commercial use case of churn, enabling proactive retention strategies that improve revenue stability.
 
• Enables Scalable Growth: Establishes a scalable data foundation that supports ongoing analytics needs beyond the immediate churn focus.
 
• Facilitates Informed Decision-Making: Equips C-suite executives and operational leaders with actionable intelligence to drive customer-centric initiatives.
 
By delivering a tailored, data-driven solution, we will empower Any Hour Group, LLC to transform churn management from a reactive challenge into a strategic advantage.
 
3 Objectives
 
The primary objectives of this Design and Discovery project for Any Hour Group, LLC are as follows:
 
a. Comprehensive Due Diligence Assessment
Conduct a thorough evaluation of the existing data platform infrastructure to identify strengths, gaps, and opportunities related to churn management within the SaaS B2B environment.
 
b. Churn Reduction Strategy Development
Define actionable insights and strategic recommendations aimed at reducing customer churn, leveraging data-driven analysis tailored to the client's commercial use case.
 
c. Data Platform Optimization
Assess and design enhancements to the current data platform to improve data integration, quality, and accessibility, enabling more effective churn analytics and reporting.
 
d. Alignment with Private Equity Objectives
Ensure that all findings and proposed solutions align with the expectations and value creation goals of Any Hour Group, LLC's private equity stakeholders.
 
e. Roadmap for Implementation
Deliver a clear, prioritized roadmap outlining next steps for technology and process improvements, supporting scalable and sustainable churn management capabilities.
 
By achieving these objectives, the project will provide Any Hour Group, LLC with a robust foundation to enhance customer retention, optimize data utilization, and support informed decision-making aligned with their strategic growth ambitions.
 
4 Deliverables
 
Throughout the engagement with Any Hour Group, LLC, the following key deliverables will be provided to ensure comprehensive coverage of the Due Diligence project focused on churn within their SaaS B2B business model:
 
a. Discovery and Design Artifacts
 
• Current State Assessment Report
A detailed analysis of the existing data platform infrastructure, highlighting strengths, gaps, and opportunities related to churn analytics.
 
• Stakeholder Interview Summaries
Documentation of insights gathered from key stakeholders, including Private Equity fund representatives, to align on business objectives and technical requirements.
 
• Churn Use Case Definition Document
A clear articulation of churn-related business and technical use cases, including metrics, KPIs, and success criteria.
 
b. Data Platform Evaluation and Recommendations
 
• Data Architecture Review
An evaluation of the current data platform's architecture with respect to scalability, data quality, and integration capabilities relevant to churn analysis.
 
• Gap Analysis and Roadmap
Identification of critical gaps in data collection, processing, and reporting, accompanied by a prioritized roadmap for enhancements.
 
c. Solution Design Deliverables
 
• Target State Data Platform Design
A comprehensive design blueprint for the enhanced data platform tailored to support churn analytics, including data flows, storage, and processing components.
 
• Technical Specifications Document
Detailed technical requirements and specifications to guide subsequent implementation phases.
 
d. Reporting and Insights Framework
 
• Churn Analytics Reporting Framework
A structured framework outlining the reporting cadence, dashboards, and key insights to be delivered to executive and PE stakeholders.
 
• Sample Dashboards and Visualizations
Prototype dashboards demonstrating actionable churn insights, designed for usability and strategic decision-making.
 
e. Final Engagement Deliverables
 
• Executive Summary Presentation
A concise presentation summarizing findings, recommendations, and next steps, tailored for C-suite and Private Equity audiences.
 
• Comprehensive Engagement Report
A final report consolidating all deliverables, analyses, and strategic recommendations to support informed decision-making.
 
Each deliverable will be developed with a focus on enabling Any Hour Group, LLC to leverage their existing data platform effectively, reduce churn, and maximize value for their Private Equity stakeholders. Regular checkpoints and reviews will be scheduled to ensure alignment and incorporate feedback throughout the engagement lifecycle.
 
5 Approach :
 
Any Hour Group, LLC's engagement is designed to address the unique challenges and opportunities inherent in their SaaS-based, B2B business model, with a specific focus on churn reduction through a robust data platform. Recognizing the complexity of the existing data infrastructure and the criticality of aligning with private equity stakeholders' expectations, our approach is meticulously tailored to deliver actionable insights and strategic value. This engagement leverages a phased methodology that balances thorough discovery with pragmatic design, ensuring that solutions are both innovative and implementable within the defined timeline.
 
Phase 1: Design & Discovery, Duration: 6 weeks, Timeline: Week 1 to Week 6
Summary:
This initial phase focuses on gaining a comprehensive understanding of Any Hour Group, LLC's current data landscape, business objectives, and churn-related challenges. It establishes the foundation for a data platform that supports precise churn analytics and decision-making.  
 
Activities:  
 
• Conduct stakeholder interviews to capture business needs and PE fund expectations  
 
• Assess existing data infrastructure and identify integration points  
 
• Map current churn metrics and data flows to uncover gaps and opportunities  
 
• Define key performance indicators (KPIs) aligned with commercial and technical use cases  
 
• Develop a high-level design blueprint for the data platform tailored to churn analysis  
 
• Validate findings and design approach with client leadership and technical teams
 
This structured approach ensures that the engagement is grounded in a deep understanding of Any Hour Group, LLC's operational realities and strategic priorities, enabling the delivery of a data platform that drives measurable improvements in customer retention and business performance.
 
6 Outcomes :
 
The engagement with Any Hour Group, LLC is designed to deliver measurable business impact through a comprehensive design and discovery process focused on churn reduction within their SaaS B2B model. Leveraging their existing data platform infrastructure, this project will enable enhanced data-driven decision-making capabilities critical to private equity stakeholders and executive leadership.
 
Expected Results
 
• Comprehensive Churn Insights: Development of a robust data framework to identify key drivers of customer churn, enabling targeted retention strategies.
 
• Optimized Data Platform Utilization: Enhancement of the current data platform to support scalable analytics and reporting tailored to churn management.
 
• Strategic Alignment: Clear articulation of business and technical requirements that align with Any Hour Group's growth objectives and PE fund expectations.
 
• Risk Mitigation: Early identification of potential churn risks through data-driven discovery, reducing revenue leakage and improving customer lifetime value.
 
• Actionable Recommendations: Delivery of prioritized, actionable insights and design options to inform subsequent phases of solution development.
 
7 Business Impact
 
• Increased Customer Retention: By addressing churn proactively, Any Hour Group can expect improved customer loyalty and reduced attrition rates.
 
• Revenue Growth: Enhanced retention directly contributes to sustained revenue streams and improved profitability.
 
• Data-Driven Culture: Strengthening the data platform fosters a culture of analytics-led decision-making across the organization.
 
• Investment Confidence: Providing transparent, data-backed insights supports the PE fund's oversight and strategic investment decisions.
 
• Scalable Foundation: Establishing a scalable data architecture that supports future analytics initiatives beyond churn management.
 
This engagement positions Any Hour Group, LLC to transform churn challenges into strategic opportunities, driving long-term value creation and competitive advantage in the US SaaS market.
 
"""

    passage_2 = """
"""
    return passage_1, passage_2