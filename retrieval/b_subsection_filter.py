import psycopg2
import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer(
    "BAAI/bge-large-en-v1.5"
)


def subsection_filter(
    subsection_query,
    child_ids,
    search_type=1,
    top_k=10
):
    """
    search_type:
        1 -> Semantic Search
        2 -> Keyword Search
    """

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
        actual_text_data,
        embedding
    FROM child_chunks
    WHERE id = ANY(%s)
    """, (
        child_ids,
    ))

    rows = cur.fetchall()

    results = []

    # ==========================
    # SEMANTIC SEARCH
    # ==========================
    if search_type == 1:

        query_emb = model.encode(
            subsection_query
        )

        for row in rows:

            similarity = cosine_similarity(
                [query_emb],
                [model.encode(row[1])]
            )[0][0]

            results.append({

                "chunk_id": row[0],

                "subsection": row[1],

                "text": row[2],

                "embedding": row[3],

                "subsection_score":
                    float(similarity)

            })

        results.sort(
            key=lambda x:
            x["subsection_score"],
            reverse=True
        )

    # ==========================
    # KEYWORD SEARCH
    # ==========================
    elif search_type == 2:

        query_tokens = set(
            re.findall(
                r"\w+",
                subsection_query.lower()
            )
        )

        for row in rows:

            subsection_tokens = set(
                re.findall(
                    r"\w+",
                    row[1].lower()
                )
            )

            matched_words = (
                query_tokens.intersection(
                    subsection_tokens
                )
            )

            match_count = len(
                matched_words
            )

            if match_count > 0:

                results.append({

                    "chunk_id": row[0],

                    "subsection": row[1],

                    "text": row[2],

                    "embedding": row[3],

                    "subsection_score":
                        match_count,

                    "matched_words":
                        sorted(
                            list(matched_words)
                        )

                })

        results.sort(
            key=lambda x:
            x["subsection_score"],
            reverse=True
        )
    # print(results)

    cur.close()
    conn.close()

    return results[:top_k]