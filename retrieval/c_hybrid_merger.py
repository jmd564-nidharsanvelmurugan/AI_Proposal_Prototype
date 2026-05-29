def hybrid_merge(
    keyword_results,
    vector_results
):

    merged = {}

    # -----------------------------
    # Keyword Results
    # -----------------------------

    for chunk in keyword_results:

        merged[
            chunk["chunk_id"]
        ] = {

            "chunk_id":
                chunk["chunk_id"],

            "text":
                chunk["text"],

            "embedding":
                chunk["embedding"],

            "matched_words":
                chunk["matched_words"],

            "keyword_score":
                chunk["keyword_score"],

            "distance":
                None,

            "similarity":
                None

        }

    # -----------------------------
    # Vector Results
    # -----------------------------

    for chunk in vector_results:

        if chunk["chunk_id"] not in merged:

            merged[
                chunk["chunk_id"]
            ] = {

                "chunk_id":
                    chunk["chunk_id"],

                "text":
                    chunk["text"],

                "embedding":
                    chunk["embedding"],

                "matched_words":
                    [],

                "keyword_score":
                    0,

                "distance":
                    chunk["distance"],

                "similarity":
                    chunk["similarity"]

            }

        else:

            merged[
                chunk["chunk_id"]
            ]["distance"] = (
                chunk["distance"]
            )

            merged[
                chunk["chunk_id"]
            ]["similarity"] = (
                chunk["similarity"]
            )

    # -----------------------------
    # Convert Dictionary -> List
    # -----------------------------

    results = list(
        merged.values()
    )

    print("\n")
    print("=" * 100)
    print("HYBRID RESULTS")
    print("=" * 100)

    for r in results:

        print(
            f"\nChunk ID       : {r['chunk_id']}"
        )

        print(
            f"Keyword Score  : {r['keyword_score']}"
        )

        print(
            f"Matched Words  : {r['matched_words']}"
        )

        print(
            f"Similarity     : {r['similarity']:.4f}"
        )

        print(
            f"Distance       : {r['distance']:.4f}"
        )

        print(
            f"Text           : {r['text']}"
        )
    

        print("-" * 100)

    return results