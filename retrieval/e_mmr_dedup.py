from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import ast


def mmr_dedup(
    candidates,
    top_k=10,
    lambda_mult=0.7
):
    """
    candidates = [
        {
            "chunk_id": "...",
            "text": "...",
            "embedding": [...],
            "similarity": 0.87
        }
    ]
    """

    if not candidates:
        return []

    # --------------------------------
    # Convert embedding strings
    # --------------------------------

    for candidate in candidates:

        if isinstance(
            candidate["embedding"],
            str
        ):

            candidate["embedding"] = (
                ast.literal_eval(
                    candidate["embedding"]
                )
            )

    top_k = min(
        top_k,
        len(candidates)
    )

    # --------------------------------
    # Pick highest relevance chunk
    # --------------------------------

    first = max(
        candidates,
        key=lambda x:
        x["similarity"]
    )

    selected = [first]

    remaining = candidates.copy()

    remaining.remove(first)

    # --------------------------------
    # MMR Selection
    # --------------------------------

    while (
        len(selected) < top_k
        and remaining
    ):

        best_candidate = None

        best_mmr_score = -999999

        for candidate in remaining:

            relevance = candidate[
                "similarity"
            ]

            diversity = max(

                cosine_similarity(

                    np.array(
                        candidate["embedding"]
                    ).reshape(1, -1),

                    np.array(
                        selected_item[
                            "embedding"
                        ]
                    ).reshape(1, -1)

                )[0][0]

                for selected_item in selected

            )

            mmr_score = (

                lambda_mult
                * relevance

                -

                (1 - lambda_mult)
                * diversity

            )

            if (
                mmr_score
                > best_mmr_score
            ):

                best_mmr_score = (
                    mmr_score
                )

                best_candidate = (
                    candidate
                )

        selected.append(
            best_candidate
        )

        remaining.remove(
            best_candidate
        )

    # --------------------------------
    # Return only required fields
    # --------------------------------

    return [

        {
            "chunk_id":
                chunk["chunk_id"],

            "text":
                chunk["text"],

            "similarity":
                round(
                    chunk["similarity"],
                    4
                )
        }

        for chunk in selected

    ]