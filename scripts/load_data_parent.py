import json
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="proposal_retrieval",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

with open("../data/parent_chunks.json", "r") as f:
    parents = json.load(f)

for p in parents:

    metadata = p["metadata_keywords"]

    cur.execute("""
        INSERT INTO parent_chunks (
            id,
            document_id,
            section,

            business_offering,
            solution,
            region,
            project_type,
            commercial_use_case,
            technical_use_case,
            business_model,
            existing_infra,
            pe_relationship,

            actual_text_data,

            child_chunks,

            chunk_type
        )
        VALUES (
            %s,%s,%s,
            %s,%s,%s,%s,%s,%s,%s,%s,%s,
            %s,%s,%s
        )
    """, (
        p["id"],
        p["document_id"],
        p["section"],

        metadata["business_offering"],
        metadata["solution"],
        metadata["region"],
        metadata["project_type"],
        metadata["commercial_use_case"],
        metadata["technical_use_case"],
        metadata["business_model"],
        metadata["existing_infra"],
        metadata["pe_relationship"],

        p["actual_text_data"],

        json.dumps(p["child_chunks"]),

        p["chunk_type"]
    ))

conn.commit()

cur.close()
conn.close()

print("Parent chunks loaded successfully")