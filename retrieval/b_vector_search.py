import ast
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "BAAI/bge-large-en-v1.5"
)

def vector_search(
    query,
    chunks
):

    query_embedding = model.encode(
        query,
        normalize_embeddings=True
    )

    results = []

    for chunk in chunks:

        chunk_embedding = chunk["embedding"]

        # Convert string -> list
        if isinstance(
            chunk_embedding,
            str
        ):
            chunk_embedding = ast.literal_eval(
                chunk_embedding
            )

        similarity = cosine_similarity(
            [query_embedding],
            [chunk_embedding]
        )[0][0]

        distance = 1 - similarity

        results.append({

            "chunk_id":
                chunk["chunk_id"],

            "distance":
                float(distance),

            "text":
                chunk["text"],

            "embedding":
                chunk_embedding,

            "similarity":
                (1 - distance)

        })

    results.sort(
        key=lambda x:
            x["distance"]
    )

    print("@@@@@@@@@@@@@")
    print("Vector result")
    print(results)
    print("@@@@@@@@@@@@@")

    # print(results)

    return results