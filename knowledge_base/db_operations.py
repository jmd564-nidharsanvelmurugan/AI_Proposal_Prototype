import json
import psycopg2

from sentence_transformers import SentenceTransformer


# =====================================================
# Embedding Model
# =====================================================

model = SentenceTransformer(
    "BAAI/bge-large-en-v1.5"
)


def generate_embedding(text: str):

    return model.encode(
        text,
        normalize_embeddings=True
    ).tolist()


# =====================================================
# Database Connection
# =====================================================

def get_db_connection():

    return psycopg2.connect(
        host="localhost",
        port="5432",
        database="proposal_retrieval",
        user="postgres",
        password="postgres"
    )


# =====================================================
# Parent Builder
# =====================================================

def build_parent_schema(
    document_id: str,
    parent_id: str,
    solution: str,
    region: str,
    section_name: str,
    section_text: str
):

    return {

        "document_id": document_id,

        "id": parent_id,

        "metadata_keywords": {

            "business_offering": "",
            "solution": solution,
            "region": region,

            "project_type":
            "Design and Discovery",

            "commercial_use_case":
            "Operational Reporting",

            "technical_use_case":
            "Data Platform",

            "business_model":
            "B2B",

            "existing_infra":
            "Yes",

            "pe_relationship":
            "PE Portco"
        },

        "section": section_name,

        "chunk_type": "parent",

        "actual_text_data": section_text,

        "vector_embedding": [],

        "child_chunks": []
    }


# =====================================================
# Child Builder
# =====================================================
def build_child_schemas(
    document_id: str,
    section_name: str,
    subsections
):

    child_schemas = []

    for subsection in subsections:

        embedding = generate_embedding(
            subsection.content
        )

        child_schemas.append({
            "document_id": document_id,
            "section": section_name,
            "subsection": subsection.subsection_name,
            "chunk_type": "child",
            "actual_text_data": subsection.content,
            "vector_embedding": embedding
        })

    return child_schemas


# =====================================================
# Insert Parent
# =====================================================

def insert_parent_chunk(
    cursor,
    conn,
    parent_schema
):

    cursor.execute(
        """
        INSERT INTO parent_chunks
        (
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
        VALUES
        (
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s
        )
        """,
        (
            parent_schema["document_id"],
            parent_schema["id"],

            parent_schema["metadata_keywords"]
            ["business_offering"],

            parent_schema["metadata_keywords"]
            ["solution"],

            parent_schema["metadata_keywords"]
            ["region"],

            parent_schema["metadata_keywords"]
            ["project_type"],

            parent_schema["metadata_keywords"]
            ["commercial_use_case"],

            parent_schema["metadata_keywords"]
            ["technical_use_case"],

            parent_schema["metadata_keywords"]
            ["business_model"],

            parent_schema["metadata_keywords"]
            ["existing_infra"],

            parent_schema["metadata_keywords"]
            ["pe_relationship"],

            parent_schema["section"],

            parent_schema["chunk_type"],

            parent_schema["actual_text_data"],

            json.dumps(
                parent_schema["child_chunks"]
            )
        )
    )

    conn.commit()


# =====================================================
# Insert Child
# =====================================================

def insert_child_chunks(
    cursor,
    conn,
    child_schemas
):

    for child in child_schemas:

        cursor.execute(
            """
            INSERT INTO child_chunks
            (
                document_id,
                id,
                section,
                subsection,
                actual_text_data,
                embedding
            )
            VALUES
            (
                %s,%s,%s,%s,%s,%s
            )
            """,
            (
                child["document_id"],
                child["id"],
                child["section"],
                child["subsection"],
                child["actual_text_data"],
                child["vector_embedding"]
            )
        )

    conn.commit()