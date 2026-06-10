from config import structured_llm, get_prompt, get_passages
from db_operations import (
    get_db_connection,
    build_parent_schema,
    build_child_schemas,
    build_proposal_schema,
    insert_proposal_data,
    insert_parent_chunk,
    insert_child_chunks
)
from config import SubSection

import json
from datetime import datetime
from uuid import uuid4
import re


# =====================================================
# Helper Functions
# =====================================================

def pretty_print_metadata(result):
    """Print extracted metadata and sections in readable format."""
    
    print("\n" + "=" * 100)
    print("EXTRACTED METADATA")
    print("=" * 100)

    # Updated to show all 9 metadata fields
    print(f"\nBusiness Offering    : {result.business_offering}")
    print(f"Solution             : {result.solution}")
    print(f"Region               : {result.region}")
    print(f"Project Type         : {result.project_type}")
    print(f"Commercial Use Case  : {result.commercial_use_case}")
    print(f"Technical Use Case   : {result.technical_use_case}")
    print(f"Business Model       : {result.business_model}")
    print(f"Existing Infra       : {result.existing_infra_has_data_platform}")
    print(f"PE Relationship      : {result.pe_relationship}")

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
        f.write(result.model_dump_json(indent=4))

    print("\n" + "=" * 100)
    print("JSON SAVED")
    print("=" * 100)
    print(f"Saved to: {file_name}")


def print_schemas(parent_chunks, child_chunks):
    """Print parent and child schemas without embeddings for readability."""
    
    print("\n" + "=" * 100)
    print("PARENT CHUNKS")
    print("=" * 100)

    # Create safe version without embeddings for printing
    safe_parents = []
    for parent in parent_chunks:
        safe_parent = parent.copy()
        safe_parent.pop("embedding", None)
        safe_parents.append(safe_parent)

    print(json.dumps(safe_parents, indent=4, default=str))

    print("\n" + "=" * 100)
    print("CHILD CHUNKS")
    print("=" * 100)

    # Create safe version without embeddings for printing
    safe_children = []
    for child in child_chunks:
        safe_child = child.copy()
        safe_child.pop("embedding", None)
        safe_children.append(safe_child)

    print(json.dumps(safe_children, indent=4, default=str))


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

    document_id = (
        f"PROP_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_"
        f"{uuid4().hex[:6].upper()}"
    )

    parent_chunks = []
    child_chunks = []

    for section in result.sections:

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
        # Create Section Slug
        # ==========================================

        section_slug = re.sub(
            r"[^a-zA-Z0-9]+",
            "_",
            section.section_name.strip()
        ).upper()

        # ==========================================
        # Dynamic Parent ID
        # ==========================================

        parent_id = f"{document_id}_{section_slug}"

        # ==========================================
        # Parent Text
        # ==========================================

        section_text = "\n\n".join(
            subsection.content
            for subsection in section.subsections
        )

        # ==========================================
        # Updated: Build Parent Schema with ALL metadata fields
        # ==========================================

        parent_schema = build_parent_schema(
            document_id=document_id,
            parent_id=parent_id,
            business_offering=result.business_offering,
            solution=result.solution,
            region=result.region,
            project_type=result.project_type,
            commercial_use_case=result.commercial_use_case,
            technical_use_case=result.technical_use_case,
            business_model=result.business_model,
            existing_infra="Yes" if result.existing_infra_has_data_platform else "No",
            pe_relationship=result.pe_relationship,
            section_name=section.section_name,
            section_text=section_text,
            child_chunks=[]
        )

        # ==========================================
        # Children
        # ==========================================

        current_childs = build_child_schemas(
            document_id=document_id,
            section_name=section.section_name,
            subsections=section.subsections
        )

        for idx, child in enumerate(current_childs, start=1):

            child_id = f"{parent_id}_SUB_{idx:03d}"

            child["id"] = child_id
            child["parent_id"] = parent_id

            parent_schema["child_chunks"].append(
                {
                    "id": child_id,
                    "subsection": child["subsection"],
                    "subsection_name": child["subsection_name"]
                }
            )

        parent_chunks.append(parent_schema)
        child_chunks.extend(current_childs)

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

    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert child chunks first (no dependencies)
        insert_child_chunks(
            cursor,
            conn,
            child_chunks
        )

        # Insert parent chunks
        for parent in parent_chunks:
            insert_parent_chunk(
                cursor,
                conn,
                parent
            )

        cursor.close()
        conn.close()

        print(f"\n✅ Successfully stored:")
        print(f"   - {len(parent_chunks)} parent chunks")
        print(f"   - {len(child_chunks)} child chunks")

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"\n❌ Database Error : {e}")
        raise

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    main()