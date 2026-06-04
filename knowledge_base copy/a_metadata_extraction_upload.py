from typing import List

from pydantic import BaseModel

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate

import psycopg2

import json

# =====================================================
# Load Environment Variables
# =====================================================

load_dotenv()


# =====================================================
# Schema
# =====================================================

class SubSection(BaseModel):
    subsection_name: str
    subsection_passage: str


class KBMetadata(BaseModel):
    solution: str
    region: str
    section: str
    subsections: List[SubSection]


# =====================================================
# LLM
# =====================================================

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

structured_llm = llm.with_structured_output(
    KBMetadata
)


# =====================================================
# User Choice
# =====================================================

option = int(
    input(
        """
1 -> Passage already contains subsection headings

2 -> Passage contains no subsection headings

Enter Choice:
"""
    )
)


# =====================================================
# Prompt
# =====================================================

if option == 1:
    prompt = ChatPromptTemplate.from_template(
        """
You are an expert proposal knowledge-base analyzer.

The passage already contains subsection headings.

Tasks:

1. Extract Solution.

Allowed Values:
- Core Reporting
- Due Diligence
- Data Advisory
- Value Creation
- Exit Prep

2. Extract Region.

Allowed Values:
- US
- UK
- Europe

3. Use the provided Main Section.

4. Identify all subsection headings.

5. Extract the passage belonging to each subsection.

Rules:

- Do not create new subsection names.
- Use only subsection headings found in the passage.
- Preserve passage text.
- Return structured output only.

Main Section:
{main_section}

Passage:
{passage}
"""
    )
else:
    prompt = ChatPromptTemplate.from_template(
"""
You are an expert Proposal Knowledge Base Analyst.

The provided passage originates from an existing proposal, RFP response, statement of work, consulting deliverable, or enterprise knowledge-base document.

The passage does NOT contain subsection headings.

Your objective is to reconstruct the most appropriate business-oriented subsection structure that would likely have existed if the document had originally been authored using proposal best practices.

Tasks:

1. Extract Solution.

Allowed Values:

* Core Reporting
* Due Diligence
* Data Advisory
* Value Creation
* Exit Prep

2. Extract Region.

Allowed Values:

* US
* UK
* Europe

3. Use the provided Main Section exactly as given.

4. Analyze the passage and identify distinct business concepts, topics, objectives, challenges, requirements, approaches, findings, or recommendations.

5. Generate meaningful business-oriented subsection names.

6. Split the passage into logical subsection passages.

Subsection Naming Guidelines:

Common proposal subsection examples include:

* Client Overview
* Business Context
* Industry Context
* Current State Assessment
* Existing Landscape
* Current Challenges
* Business Drivers
* Strategic Objectives
* Business Objectives
* Reporting Requirements
* Data Challenges
* Governance Considerations
* Stakeholder Considerations
* Solution Overview
* Proposed Approach
* Future State Vision
* Benefits and Value
* Risk Considerations
* Implementation Considerations
* Expected Outcomes

Important:

* The above list is guidance only.
* Do NOT force content into one of these subsection names.
* If the content represents a different business concept, generate a more suitable business-oriented subsection name.
* Always prioritize semantic alignment with the content over matching the example list.

Subsection Naming Rules:

* Every subsection name must represent a clear business concept.
* Every subsection name should be meaningful when viewed independently.
* Use terminology commonly found in consulting proposals, transformation programs, data and analytics engagements, business strategy documents, and enterprise knowledge bases.
* Prefer specific business terminology over generic terminology.
* Generate subsection names that improve future semantic search and retrieval.

Do NOT generate generic subsection names such as:

* Introduction
* Overview
* Details
* Information
* Miscellaneous
* Topic
* Section
* Part
* Notes
* Content

Passage Processing Rules:

* Preserve the original content exactly.
* Do not summarize.
* Do not rewrite.
* Do not paraphrase.
* Do not hallucinate additional content.
* Divide the passage logically based on business meaning.
* Create multiple subsections when multiple business concepts are present.
* Do not merge unrelated business concepts into a single subsection.

Output Rules:

* Return structured output only.
* Return only valid values for Solution and Region.
* Use the provided Main Section exactly as given.

Main Section:
{main_section}

Passage:
{passage}
"""
    )


# =====================================================
# Chain
# =====================================================

metadata_chain = (
    prompt
    | structured_llm
)


# =====================================================
# Inputs
# =====================================================

main_section = "Executive Overview"

passage_1 = """
The client operates across the US market.

The engagement falls under Data Advisory.

Executive Overview

Business Context

The client operates in the financial services
industry and requires improved executive reporting.

Current Challenges

Reporting relies heavily on manual spreadsheet
consolidation and disconnected data sources.

Business Objectives

Create a centralized reporting platform,
improve KPI visibility, and automate reporting.

Strategic Vision

Develop a scalable analytics capability that
supports future growth initiatives.
"""

passage_2 = """
The client operates across the US market.

The engagement falls under Data Advisory.

Executive Overview


The client operates in the financial services
industry and requires improved executive reporting.


Reporting relies heavily on manual spreadsheet
consolidation and disconnected data sources.


Create a centralized reporting platform,
improve KPI visibility, and automate reporting.


Develop a scalable analytics capability that
supports future growth initiatives.
"""


# =====================================================
# Select Passage
# =====================================================

if option == 1:
    passage = passage_1
else:
    passage = passage_2


# =====================================================
# Invoke
# =====================================================

result = metadata_chain.invoke(
    {
        "main_section": main_section,
        "passage": passage
    }
)


# =====================================================
# Pretty Output
# =====================================================

print("\n" + "=" * 100)
print("EXTRACTED METADATA")
print("=" * 100)

print("\nSolution:")
print(result.solution)

print("\nRegion:")
print(result.region)

print("\nSection:")
print(result.section)

print("\nSubsections:\n")

for subsection in result.subsections:
    print("-" * 80)
    print("Subsection:", subsection.subsection_name)
    print()
    print(subsection.subsection_passage)
    print()


# =====================================================
# JSON Output
# =====================================================

print("\n" + "=" * 100)
print("JSON OUTPUT")
print("=" * 100)

print(
    result.model_dump_json(
        indent=4
    )
)

# =====================================================
# Postgres DB Schema
# =====================================================

from sentence_transformers import SentenceTransformer
import json

print("\n" + "=" * 100)
print("POSTGRES DB SCHEMA")
print("=" * 100)

# =====================================================
# Embedding Model
# =====================================================

model = SentenceTransformer(
    "BAAI/bge-large-en-v1.5"
)

# =====================================================
# IDs
# =====================================================

document_id = "PROP001"
parent_id = "PARENT_EXEC_008"

# =====================================================
# Parent Schema
# =====================================================

parent_schema = {
    "document_id": document_id,
    "id": parent_id,
    "metadata_keywords": {
        "business_offering": "",
        "solution": result.solution,
        "region": result.region,
        "project_type": "Design and Discovery",
        "commercial_use_case": "Operational Reporting",
        "technical_use_case": "Data Platform",
        "business_model": "B2B",
        "existing_infra": "Yes",
        "pe_relationship": "PE Portco"
    },
    "section": result.section,
    "chunk_type": "parent",
    "actual_text_data": passage,
    "vector_embedding": [],
    "child_chunks": []
}



# =====================================================
# Child Schema
# =====================================================

child_schema = []

for idx, subsection in enumerate(result.subsections, start=1):
    child_id = f"CHILD_EXEC_{idx:03d}"
    
    embedding = (
        model.encode(
            subsection.subsection_passage,
            normalize_embeddings=True
        ).tolist()
    )
    
    child_chunk = {
        "document_id": document_id,
        "id": child_id,
        "section": result.section,
        "subsection": subsection.subsection_name,
        "chunk_type": "child",
        "actual_text_data": subsection.subsection_passage,
        "vector_embedding": embedding
    }
    
    child_schema.append(child_chunk)
    
    parent_schema["child_chunks"].append(
        {
            "id": child_id,
            "subsection": subsection.subsection_name
        }
    )

# =====================================================
# Print Parent Schema
# =====================================================

print("\n")
print("=" * 100)
print("PARENT CHUNK")
print("=" * 100)

print(
    json.dumps(
        parent_schema,
        indent=4
    )
)

# =====================================================
# Print Child Schema
# =====================================================

print("\n")
print("=" * 100)
print("CHILD CHUNKS")
print("=" * 100)

print(
    json.dumps(
        child_schema,
        indent=4
    )
)





# =====================================================
# PostgreSQL Connection
# =====================================================





conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="proposal_retrieval",
    user="postgres",
    password="postgres"
)

cursor = conn.cursor()

# =====================================================
# Insert Parent Chunk
# =====================================================
cursor.execute(
    """
    INSERT INTO parent_chunks (
        document_id,
        id,
        business_offering,
        solution,
        region,
        project_type,
        commercial_use_case,
        technical_use_case,
        business_model,
        existing_infra,
        pe_relationship,
        section,
        chunk_type,
        actual_text_data,
        child_chunks
    )
    VALUES (
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
    )
    """,
    (
        parent_schema["document_id"],
        parent_schema["id"],

        parent_schema["metadata_keywords"]["business_offering"],
        parent_schema["metadata_keywords"]["solution"],
        parent_schema["metadata_keywords"]["region"],
        parent_schema["metadata_keywords"]["project_type"],
        parent_schema["metadata_keywords"]["commercial_use_case"],
        parent_schema["metadata_keywords"]["technical_use_case"],
        parent_schema["metadata_keywords"]["business_model"],
        parent_schema["metadata_keywords"]["existing_infra"],
        parent_schema["metadata_keywords"]["pe_relationship"],

        parent_schema["section"],
        parent_schema["chunk_type"],
        parent_schema["actual_text_data"],

        json.dumps(parent_schema["child_chunks"])
    )
)

conn.commit()

print("Parent chunk inserted successfully.")

cursor.execute("""
SELECT COALESCE(
    MAX(CAST(SUBSTRING(id FROM '[0-9]+$') AS INTEGER)),
    0
)
FROM child_chunks
""")






start_id = cursor.fetchone()[0] + 1

for idx, child in enumerate(child_schema, start=start_id):

    child_id = f"CHILD_EXEC_{idx:03d}"

    cursor.execute(
        """
        INSERT INTO child_chunks (
            document_id,
            id,
            section,
            subsection,
            actual_text_data,
            embedding
        )
        VALUES (
            %s,%s,%s,%s,%s,%s
        )
        """,
        (
            child["document_id"],
            child_id,
            child["section"],
            child["subsection"],
            child["actual_text_data"],
            child["vector_embedding"]
        )
    )

conn.commit()

print("Child chunks inserted successfully.")