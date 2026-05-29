import psycopg2
import re


k = 1
query = "financial reporting"

query_tokens = set(
    re.findall(r'\w+', query.lower())
)

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="proposal_retrieval",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

cur.execute("""
SELECT
    id,
    subsection,
    actual_text_data
FROM child_chunks
""")

rows = cur.fetchall()

results = []

for row in rows:

    chunk_id = row[0]
    subsection = row[1]
    text = row[2]

    chunk_tokens = set(
        re.findall(r'\w+', text.lower())
    )

    matched_words = query_tokens.intersection(
        chunk_tokens
    )

    match_count = len(matched_words)

    # Keep only matches
    if match_count > k:

        results.append({
            "chunk_id": chunk_id,
            "subsection": subsection,
            "text": text,
            "match_count": match_count,
            "matched_words": sorted(list(matched_words))
        })

# Highest match count first
results.sort(
    key=lambda x: x["match_count"],
    reverse=True
)

print("\nKeyword Matching Results\n")

for r in results:

    print(f"Chunk ID      : {r['chunk_id']}")
    print(f"Subsection    : {r['subsection']}")
    print(f"Match Count   : {r['match_count']}")
    print(f"Matched Words : {r['matched_words']}")
    print(f"Text          : {r['text']}")
    print("-" * 100)

cur.close()
conn.close()