import re


def keyword_search(
    query,
    chunks
):

    query_tokens = set(
        re.findall(
            r"\w+",
            query.lower()
        )
    )

    results = []

    for chunk in chunks:

        chunk_tokens = set(
            re.findall(
                r"\w+",
                chunk["text"].lower()
            )
        )

        matched_words = (
            query_tokens.intersection(
                chunk_tokens
            )
        )

        match_count = len(
            matched_words
        )

        if match_count > 1:

            results.append({

                "chunk_id":
                    chunk["chunk_id"],

                "matched_words":
                    sorted(
                        list(
                            matched_words
                        )
                    ),

                "keyword_score":
                    match_count,

                "text":
                    chunk["text"],

                "embedding":
                    chunk["embedding"]

            })

    results.sort(
        key=lambda x:
            x["keyword_score"],
        reverse=True
    )
    print("@@@@@@@@@@@@@")
    print("Keyword result")
    print(results)
    print("@@@@@@@@@@@@@")

    return results