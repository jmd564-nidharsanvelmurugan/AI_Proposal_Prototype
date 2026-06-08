import psycopg2
import json
from sentence_transformers import SentenceTransformer

# =====================================================
# Embedding Model
# =====================================================

model = SentenceTransformer("BAAI/bge-large-en-v1.5")

def generate_embedding(text: str):
    return model.encode(text, normalize_embeddings=True).tolist()

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
# Schema Builders
# =====================================================

def build_parent_schema(document_id: str, parent_id: str, result, passage: str):
    return {
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

def build_child_schemas(document_id: str, result):
    child_schemas = []
    for idx, subsection in enumerate(result.subsections, start=1):
        child_id = f"CHILD_EXEC_{idx:03d}"
        embedding = generate_embedding(subsection.subsection_passage)
        
        child_schemas.append({
            "id": child_id,
            "section": result.section,
            "subsection": subsection.subsection_name,
            "chunk_type": "child",
            "actual_text_data": subsection.subsection_passage,
            "vector_embedding": embedding
        })
    return child_schemas

# =====================================================
# Database Inserters
# =====================================================

def insert_parent_chunk(cursor, conn, parent_schema):
    cursor.execute(
        """
        INSERT INTO parent_chunks (
            document_id, id, business_offering, solution, region,
            project_type, commercial_use_case, technical_use_case,
            business_model, existing_infra, pe_relationship,
            section, chunk_type, actual_text_data, child_chunks
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
    print("✓ Parent chunk inserted successfully.")

def insert_child_chunks(cursor, conn, child_schemas):
    cursor.execute("""
        SELECT COALESCE(MAX(CAST(SUBSTRING(id FROM '[0-9]+$') AS INTEGER)), 0)
        FROM child_chunks
    """)
    start_id = cursor.fetchone()[0] + 1
    
    for idx, child in enumerate(child_schemas, start=start_id):
        child_id = f"CHILD_EXEC_{idx:03d}"
        cursor.execute(
            """
            INSERT INTO child_chunks (
                document_id, id, section, subsection, actual_text_data, embedding
            ) VALUES (%s, %s, %s, %s, %s, %s)
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
    print(f"✓ {len(child_schemas)} child chunks inserted successfully.")