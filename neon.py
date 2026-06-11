import pandas as pd
import psycopg
from pgvector.psycopg import register_vector


CONN_STR = (
    "postgresql://neondb_owner:npg_newiIELXDz02@ep-snowy-resonance-aor957h7-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

df = pd.read_csv(
    r"C:\Users\PragatheeshIndiran\Downloads\child_chunks_202606111320.csv"
)

with psycopg.connect(CONN_STR) as conn:
    register_vector(conn)

    with conn.cursor() as cur:

        for _, row in df.iterrows():

            cur.execute(
                """
                INSERT INTO child_chunk (
                    id,
                    document_id,
                    section,
                    subsection,
                    actual_text_data,
                    embedding,
                    created_at
                )
                VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s::vector,
                    %s
                )
                ON CONFLICT (id) DO NOTHING
                """,
                (
                    row["id"],
                    row["document_id"],
                    row["section"],
                    row["subsection"],
                    row["actual_text_data"],
                    row["embedding"],
                    row["created_at"],
                ),
            )

    conn.commit()

print("Child chunks uploaded successfully!")