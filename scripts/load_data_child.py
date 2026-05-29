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

with open("../data/child_chunks.json", "r") as f:
    chunks = json.load(f)

for c in chunks:
    cur.execute("""
        INSERT INTO child_chunks (
            id,
            document_id,
            section,
            subsection,
            actual_text_data
        )
        VALUES (%s,%s,%s,%s,%s)
    """, (
        c["id"],
        c["document_id"],
        c["section"],
        c["subsection"],
        c["actual_text_data"]
    ))

conn.commit()
cur.close()
conn.close()