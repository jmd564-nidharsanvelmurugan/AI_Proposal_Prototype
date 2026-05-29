import psycopg2
import json

# User Inputs
filters = {
    "solution": "Data Advisory",
    "region": "US",
    "section": "Executive Overview"
}

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="proposal_retrieval",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

query = """
SELECT
    id,
    document_id,
    section,
    solution,
    region,
    child_chunks
FROM parent_chunks
WHERE solution = %s
AND region = %s
AND section = %s
"""

cur.execute(
    query,
    (
        filters["solution"],
        filters["region"],
        filters["section"]
    )
)

parents = cur.fetchall()

print("\nMatching Parent Chunks\n")

all_child_ids = []

for row in parents:

    parent_id = row[0]
    document_id = row[1]
    section = row[2]
    solution = row[3]
    region = row[4]
    child_chunks = row[5]

    print(f"Parent ID  : {parent_id}")
    print(f"Document   : {document_id}")
    print(f"Section    : {section}")
    print(f"Solution   : {solution}")
    print(f"Region     : {region}")

    print("\nChild Chunks:")

    for child in child_chunks:

        print(
            f"  {child['id']} - {child['subsection']}"
        )

        all_child_ids.append(
            child["id"]
        )

    print("-" * 80)

print("\nCollected Child IDs:")
print(all_child_ids)

cur.close()
conn.close()