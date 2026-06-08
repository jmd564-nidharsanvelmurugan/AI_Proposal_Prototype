from config import structured_llm, get_prompt, get_passages
from db_operations import (
    get_db_connection,
    build_parent_schema,
    build_child_schemas,
    insert_parent_chunk,
    insert_child_chunks
)
from config import SubSection

import json


# =====================================================
# Helper Functions
# =====================================================

def pretty_print_metadata(result):

    print("\n" + "=" * 100)
    print("EXTRACTED METADATA")
    print("=" * 100)

    print(f"\nSolution : {result.solution}")
    print(f"Region   : {result.region}")

    for section in result.sections:

        print("\n" + "=" * 80)
        print(f"SECTION : {section.section_name}")
        print("=" * 80)

        if section.content:
            print(section.content)

        for subsection in section.subsections:

            print(f"\nSubsection : {subsection.subsection_name}")
            print("-" * 60)

            print(subsection.content)

    # =====================================================
    # Save JSON
    # =====================================================

    file_name = "proposal_kb.json"

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(
            result.model_dump_json(
                indent=4
            )
        )

    print("\n" + "=" * 100)
    print("JSON SAVED")
    print("=" * 100)
    print(f"Saved to: {file_name}")


def print_schemas(parent_chunks, child_chunks):

    print("\n" + "=" * 100)
    print("PARENT CHUNKS")
    print("=" * 100)

    print(
        json.dumps(
            parent_chunks,
            indent=4
        )
    )

    print("\n" + "=" * 100)
    print("CHILD CHUNKS")
    print("=" * 100)

    print(
        json.dumps(
            child_chunks,
            indent=4
        )
    )


# =====================================================
# Main
# =====================================================

def main():

    option = int(input(
        """
1 -> Document contains headings
2 -> Document does not contain headings

Enter Choice:
"""
    ))

    passage_1, passage_2 = get_passages()

    passage = passage_1 if option == 1 else passage_2

    prompt = get_prompt(option)

    chain = prompt | structured_llm

    print("\n🔄 Processing Proposal...")

    result = chain.invoke({
        "passage": passage
    })

    pretty_print_metadata(result)


    

    # =================================================
    # Build Parent + Child Schemas
    # =================================================

    document_id = "PROP001"

    parent_chunks = []
    child_chunks = []

    parent_counter = 1
    child_counter = 1

    for section in result.sections:

        parent_id = f"PARENT_SEC_{parent_counter:03d}"

        # ==========================================
        # Handle sections without subsections
        # ==========================================

        if not section.subsections:

         section.subsections = [
         SubSection(
            subsection_name=section.section_name,
            content=section.content
         )
        ]

        # ==========================================
        # Parent text
        # ==========================================

        section_text = "\n\n".join([
            subsection.content
            for subsection in section.subsections
        ])

        parent_schema = build_parent_schema(
    document_id=document_id,
    parent_id=parent_id,
    solution=result.solution,
    region=result.region,
    section_name=section.section_name,
    section_text=section_text
)

        # ==========================================
        # Children
        # ==========================================

        current_childs = build_child_schemas(
    document_id=document_id,
    section_name=section.section_name,
    subsections=section.subsections
)

        for child in current_childs:

            child["id"] = (
                f"CHILD_SEC_{child_counter:03d}"
            )

            parent_schema["child_chunks"].append({
                "id": child["id"],
                "subsection": child["subsection"]
            })

            child_counter += 1

        parent_chunks.append(parent_schema)
        child_chunks.extend(current_childs)

        parent_counter += 1

    # =================================================
    # Print
    # =================================================

    print_schemas(
        parent_chunks,
        child_chunks
    )

    # =================================================
    # Insert
    # =================================================

    print("\n" + "=" * 100)
    print("DATABASE INSERTION")
    print("=" * 100)

    try:

        conn = get_db_connection()
        cursor = conn.cursor()

        for parent in parent_chunks:
            insert_parent_chunk(
                cursor,
                conn,
                parent
            )

        insert_child_chunks(
            cursor,
            conn,
            child_chunks
        )

        cursor.close()
        conn.close()

        print("\n✅ All chunks stored successfully")

    except Exception as e:

        print(f"\n❌ Database Error : {e}")


if __name__ == "__main__":
    main()