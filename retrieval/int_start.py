from .a_metadata_filter import get_candidate_chunks
from .b_subsection_filter import subsection_filter
from .b_keyword_search import keyword_search
from .b_vector_search import vector_search
from .c_hybrid_merger import hybrid_merge
from .e_mmr_dedup import mmr_dedup
from .g_generation import generate_content

# ---------------------------------------------------
# Iterate through generated template
# ---------------------------------------------------

all_results = {}

all_generated = []
response_exmaple = {
    "metadata": {
        "business_offering": "Financial Services",
        "solution": "Data Advisory",
        "region": "US",
        "project_type": "Design and Discovery",
        "commercial_use_case": "Operational Reporting",
        "technical_use_case": "Data Platform",
        "business_model": "B2B",
        "existing_infra": "Yes",
        "pe_relationship": "No"
    },
    "sections": [
        {
            "section": "Executive Overview",
            "subsections": [
                {
                    "subsection": "Financial Services Industry Overview",
                    "query": "Centralized financial reporting and analytics modernization with Azure and Power BI"
                },
                {
                    "subsection": "Retail Banking Business Model",
                    "query": "Centralized executive reporting and analytics modernization with Azure and Power BI"
                },
                {
                    "subsection": "Commercial Lending Market Trends",
                    "query": "Executive visibility and reporting modernization with Power BI and Azure"
                }
            ]
        },
        {
            "section": "Overview",
            "subsections": [
                {
                    "subsection": "Current State of Finance and Operations Teams",
                    "query": "Centralized reporting and analytics modernization for finance and operations"       
                },
                {
                    "subsection": "Overview of Existing SQL Server and Salesforce Systems",
                    "query": "Executive Reporting Modernization with SQL Server and Salesforce Integration"       
                },
                {
                    "subsection": "Challenges with Manual Report Preparation and KPI Consolidation",
                    "query": "Executive reporting modernization with Power BI and SQL Server integration"
                }
            ]
        },
        {
            "section": "Understanding",
            "subsections": [
                {
                    "subsection": "Leadership Visibility into Business Performance",
                    "query": "Executive visibility into financial performance with Power BI and SQL Server"       
                },
                {
                    "subsection": "Inconsistent KPIs and Manual Reporting Pain Points",
                    "query": "Executive visibility and KPI reporting modernization with Power BI"
                },
                {
                    "subsection": "Process Inefficiencies in Report Generation and Distribution",
                    "query": "Centralized reporting and KPI monitoring with Power BI and SQL Server"
                }
            ]
        },
        {
            "section": "Objectives",
            "subsections": [
                {
                    "subsection": "Centralized Enterprise Reporting Platform Vision",
                    "query": "Centralized reporting platform with Azure and Salesforce integration"
                },
                {
                    "subsection": "Automating Executive Reporting and KPI Distribution Processes",
                    "query": "Automated executive reporting and KPI distribution with Power BI analytics"
                },
                {
                    "subsection": "Enhancing Leadership Insights with Revenue Trends and Operational Performance",
                    "query": "Centralized executive reporting and analytics with Azure and Power BI"
                }
            ]
        },
        {
            "section": "Deliverables",
            "subsections": [
                {
                    "subsection": "Discovery Report and Solution Architecture Expectations",
                    "query": "Centralized executive reporting and analytics modernization with Azure and Power BI"
                },
                {
                    "subsection": "Wireframes and Roadmap Development",
                    "query": "Centralized executive reporting and analytics modernization with Azure and Power BI"
                },
                {
                    "subsection": "Technical Detail and POC Requirements",
                    "query": "Centralized executive reporting and analytics modernization with Azure and Power BI"
                }
            ]
        },
        {
            "section": "Approach",
            "subsections": [
                {
                    "subsection": "Batch and Near Real-Time Processing Considerations",
                    "query": "Centralized reporting and analytics modernization with Azure and Power BI"
                },
                {
                    "subsection": "APIs and Required Reports for Executive KPI Dashboard",
                    "query": "Executive KPI dashboard with real-time SQL Server and Salesforce integration"       
                },
                {
                    "subsection": "Approval Workflows and Executive KPI Alerts",
                    "query": "Executive KPI alerts and approval workflows automation"
                }
            ]
        },
        {
            "section": "Outcomes",
            "subsections": [
                {
                    "subsection": "Expected Business Outcomes and Improved Decision-Making",
                    "query": "Centralized executive reporting and analytics modernization with Azure and Power BI"
                },
                {
                    "subsection": "KPIs for Reporting Cycle Time and Dashboard Adoption",
                    "query": "Executive reporting modernization with Power BI and Azure integration"
                },
                {
                    "subsection": "Risks and Success Criteria for Reporting Cycle Reduction",
                    "query": "Executive visibility and reporting cycle reduction with Power BI analytics"
                }
            ]
        }
    ]
}




def iterateor(response_iter , reponse_type = 2 , questionnaire = ""):

 response = {}

 if reponse_type == 1:
    response = response_iter
 else:
    response = response_exmaple

 for section in response["sections"]:

    section_name = section["section"]

    print("\n" + "=" * 80)
    print(f"SECTION : {section_name}")
    print("=" * 80)

    all_results[section_name] = {}

    for subsection in section["subsections"]:

        subsection_name = subsection["subsection"]
        query = subsection["query"]

        # print(f"\nSubsection : {subsection_name}")
        # print(f"Query      : {query}")

        request = {
            "solution": response["metadata"]["solution"],
            "region": response["metadata"]["region"],
            "section": section_name,
            "subsection": subsection_name,
            "query": query
        }

        print("REQUEST*** :" , request)

        # -----------------------------------
        # STEP 1
        # Metadata Filter
        # -----------------------------------

        child_ids = (get_candidate_chunks(
            request
        ))

        print(
    "\nCandidate Child IDs:\n"
)

        print(
    child_ids
)

        # -----------------------------------
        # STEP 2
        # Semantic subsection filter
        # -----------------------------------
#         search_type = int(
#     input(
#         """
# Choose Subsection Filter Type

# 1 -> Semantic Search
# 2 -> Keyword Search

# Enter Choice:
# """
#     )
# )
        chunks = subsection_filter(
            subsection_name,
            child_ids,
            search_type=1
        )

        print(
            f"Subsection Matches: {len(chunks)}"
        )

        # -----------------------------------
        # STEP 3
        # Keyword Search
        # -----------------------------------

        keyword_results = keyword_search(
            query,
            chunks
        )

        # -----------------------------------
        # STEP 4
        # Vector Search
        # -----------------------------------

        vector_results = vector_search(
            query,
            chunks
        )

        # -----------------------------------
        # STEP 5
        # Hybrid Merge
        # -----------------------------------

        hybrid_results = hybrid_merge(
            keyword_results,
            vector_results
        )

        # -----------------------------------
        # STEP 6
        # MMR Dedup
        # -----------------------------------

        final_results = mmr_dedup(
            hybrid_results
        )

        # print(
        #     f"Final Results: {len(final_results)}"
        # )

        for chunk in final_results:
            print(chunk["chunk_id"],
            "|",
            chunk["similarity"],
            "|",
            chunk["text"])

        # generated_subsection = 

        all_results[section_name][subsection_name] = final_results

    section_wise = {
    "section": section_name,
    "sub_sections": all_results[section_name]
   }
   


    

    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(section_wise)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    
    
    print("Generated Content : ")
    generated_section = generate_content(
    questionnaire=questionnaire,
    section=section_name,
    sub_sections=all_results[section_name],
    metadata=response_iter["metadata"]
    )



    all_generated.append({
    "section": section_name,
    "generated_content": generated_section
})
    

    text = input("continue - c/quit  SECTION - q")

    if text == "q":
      return all_generated
    

 return all_generated
    

    