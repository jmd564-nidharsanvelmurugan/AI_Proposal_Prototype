from sentence_transformers import SentenceTransformer
import psycopg2

# Load model
model = SentenceTransformer("BAAI/bge-large-en-v1.5")

# Query
query = "Banking reporting"

# Generate query embedding
query_embedding = model.encode(query).tolist()

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="proposal_retrieval",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

# Vector Search
cur.execute("""
SELECT
    id,
    subsection,
    actual_text_data,
    embedding <=> %s::vector AS distance
FROM child_chunks
ORDER BY embedding <=> %s::vector
LIMIT 5;
""", (
    str(query_embedding),
    str(query_embedding)
))

results = cur.fetchall()

print("\nTop 5 Results:\n")

for row in results:
    chunk_id, subsection, text, distance = row

    print(f"Chunk ID   : {chunk_id}")
    print(f"Subsection : {subsection}")
    print(f"Distance   : {distance:.4f}")
    print(f"Text       : {text}")
    print("-" * 80)

cur.close()
conn.close()






#  check for the other best similarity metrics