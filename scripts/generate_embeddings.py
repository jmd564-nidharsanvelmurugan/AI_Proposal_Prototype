from sentence_transformers import SentenceTransformer
import psycopg2

# Load embedding model
model = SentenceTransformer("BAAI/bge-large-en-v1.5")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="proposal_retrieval",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

# Fetch child chunks
cur.execute("""
    SELECT id, actual_text_data
    FROM child_chunks
""")

rows = cur.fetchall()

for chunk_id, text in rows:

    print(f"Embedding: {chunk_id}")

    embedding = model.encode(text).tolist()

    cur.execute("""
        UPDATE child_chunks
        SET embedding = %s
        WHERE id = %s
    """, (
        embedding,
        chunk_id
    ))

conn.commit()

cur.close()
conn.close()

print("Done")