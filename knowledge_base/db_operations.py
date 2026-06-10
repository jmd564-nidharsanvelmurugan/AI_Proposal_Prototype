import json
import uuid
import psycopg2
from typing import List, Dict, Any
from sentence_transformers import SentenceTransformer


# =====================================================
# Embedding Model
# =====================================================

model = SentenceTransformer(
    "BAAI/bge-large-en-v1.5"
)


def generate_embedding(text: str) -> List[float]:
    """Generate normalized embedding for text."""
    return model.encode(
        text,
        normalize_embeddings=True
    ).tolist()


# =====================================================
# Database Connection
# =====================================================

def get_db_connection():
    """Create and return database connection."""
    return psycopg2.connect(
        host="localhost",
        port="5432",
        database="proposal_retrieval",
        user="postgres",
        password="postgres"
    )


# =====================================================
# Proposal Builder
# =====================================================

def build_proposal_schema(
    document_id: str,
    business_offering: str,
    solution: str,
    region: str,
    project_type: str,
    commercial_use_case: str,
    technical_use_case: str,
    business_model: str,
    existing_infra: str,
    pe_relationship: str
) -> Dict[str, Any]:
    """
    Build proposal schema for the proposals table.
    """
    return {
        "document_id": document_id,
        "business_offering": business_offering,
        "solution": solution,
        "region": region,
        "project_type": project_type,
        "commercial_use_case": commercial_use_case,
        "technical_use_case": technical_use_case,
        "business_model": business_model,
        "existing_infra": existing_infra,
        "pe_relationship": pe_relationship
    }


def insert_proposal_data(cursor, conn, proposal_schema: Dict[str, Any]) -> None:
    """
    Insert proposal data into the proposals table.
    """
    cursor.execute(
        """
        INSERT INTO proposals
        (
            document_id,
            business_offering,
            solution,
            region,
            project_type,
            commercial_use_case,
            technical_use_case,
            business_model,
            existing_infra,
            pe_relationship
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (document_id) DO NOTHING
        """,
        (
            proposal_schema["document_id"],
            proposal_schema["business_offering"],
            proposal_schema["solution"],
            proposal_schema["region"],
            proposal_schema["project_type"],
            proposal_schema["commercial_use_case"],
            proposal_schema["technical_use_case"],
            proposal_schema["business_model"],
            proposal_schema["existing_infra"],
            proposal_schema["pe_relationship"]
        )
    )
    conn.commit()


# =====================================================
# Parent Builder
# =====================================================

def build_parent_schema(
    document_id: str,
    parent_id: str,
    business_offering: str,
    solution: str,
    region: str,
    project_type: str,
    commercial_use_case: str,
    technical_use_case: str,
    business_model: str,
    existing_infra: str,
    pe_relationship: str,
    section_name: str,
    section_text: str,
    child_chunks: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Build parent chunk schema with flat metadata structure and embedding.
    """
    embedding = generate_embedding(section_text)

    return {
        "document_id": document_id,
        "id": parent_id,
        "business_offering": business_offering,
        "solution": solution,
        "region": region,
        "project_type": project_type,
        "commercial_use_case": commercial_use_case,
        "technical_use_case": technical_use_case,
        "business_model": business_model,
        "existing_infra": existing_infra,
        "pe_relationship": pe_relationship,
        "section": section_name,
        "chunk_type": "parent",
        "actual_text_data": section_text,
        "embedding": embedding,
        "child_chunks": child_chunks
    }


# =====================================================
# Child Builder
# =====================================================

def build_child_schemas(
    document_id: str,
    section_name: str,
    subsections
) -> List[Dict[str, Any]]:
    """
    Build child chunk schemas for each subsection.
    """
    child_schemas = []

    for subsection in subsections:
        # Generate unique ID for each child chunk
        child_id = str(uuid.uuid4())
        
        embedding = generate_embedding(subsection.content)

        child_schemas.append({
            "id": child_id,
            "document_id": document_id,
            "section": section_name,
            "subsection": subsection.subsection_name,
            "subsection_name": subsection.subsection_name,  # For reference
            "actual_text_data": subsection.content,
            "embedding": embedding
        })

    return child_schemas


# =====================================================
# Insert Parent
# =====================================================

def insert_parent_chunk(cursor, conn, parent_schema: Dict[str, Any]) -> None:
    """
    Insert a parent chunk into the database using flat metadata structure.
    """
    cursor.execute(
        """
        INSERT INTO parent_chunks
        (
            id,
            document_id,
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
            embedding,
            child_chunks
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            parent_schema["id"],
            parent_schema["document_id"],
            parent_schema["business_offering"],
            parent_schema["solution"],
            parent_schema["region"],
            parent_schema["project_type"],
            parent_schema["commercial_use_case"],
            parent_schema["technical_use_case"],
            parent_schema["business_model"],
            parent_schema["existing_infra"],
            parent_schema["pe_relationship"],
            parent_schema["section"],
            parent_schema["chunk_type"],
            parent_schema["actual_text_data"],
            parent_schema["embedding"],
            json.dumps(parent_schema["child_chunks"])
        )
    )
    conn.commit()


# =====================================================
# Insert Child
# =====================================================

def insert_child_chunks(cursor, conn, child_schemas: List[Dict[str, Any]]) -> None:
    """
    Insert multiple child chunks into the database.
    """
    for child in child_schemas:
        cursor.execute(
            """
            INSERT INTO child_chunks
            (
                id,
                document_id,
                section,
                subsection,
                actual_text_data,
                embedding
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                child["id"],
                child["document_id"],
                child["section"],
                child["subsection"],
                child["actual_text_data"],
                child["embedding"]
            )
        )
    conn.commit()