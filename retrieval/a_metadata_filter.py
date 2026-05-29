import psycopg2


def get_candidate_chunks(request):

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="proposal_retrieval",
        user="postgres",
        password="postgres"
    )

    cur = conn.cursor()

    cur.execute("""
    SELECT child_chunks
    FROM parent_chunks
    WHERE solution = %s
      AND region = %s
      AND section = %s
    """, (
        request["solution"],
        request["region"],
        request["section"]
    ))

    rows = cur.fetchall()

    child_ids = []

    for row in rows:

        for child in row[0]:

            child_ids.append(
                child["id"]
            )

    cur.close()
    conn.close()

    return child_ids