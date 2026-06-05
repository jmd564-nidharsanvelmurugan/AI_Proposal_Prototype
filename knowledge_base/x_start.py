from config import structured_llm, get_prompt, get_passages
from db_operations import (
    get_db_connection, build_parent_schema, build_child_schemas,
    insert_parent_chunk, insert_child_chunks
)
import json

# =====================================================
# Helper Functions for Output
# =====================================================

def pretty_print_metadata(result):
    print("\n" + "=" * 100)
    print("EXTRACTED METADATA")
    print("=" * 100)
    
    print("\nSolution:")
    print(result.solution)
    
    print("\nRegion:")
    print(result.region)
    
    print("\nSection:")
    print(result.section)
    
    print("\nSubsections:\n")
    
    for subsection in result.subsections:
        print("-" * 80)
        print("Subsection:", subsection.subsection_name)
        print()
        print(subsection.subsection_passage)
        print()
    
    print("\n" + "=" * 100)
    print("JSON OUTPUT")
    print("=" * 100)
    print(result.model_dump_json(indent=4))

def print_schemas(parent_schema, child_schemas):
    print("\n" + "=" * 100)
    print("POSTGRES DB SCHEMA")
    print("=" * 100)
    
    print("\n")
    print("=" * 100)
    print("PARENT CHUNK")
    print("=" * 100)
    print(json.dumps(parent_schema, indent=4))
    
    print("\n")
    print("=" * 100)
    print("CHILD CHUNKS")
    print("=" * 100)
    print(json.dumps(child_schemas, indent=4))

# =====================================================
# Main Execution
# =====================================================

def main():
    # Get user choice
    option = int(input(
        """
1 -> Passage already contains subsection headings
2 -> Passage contains no subsection headings

Enter Choice:
"""
    ))
    
    # Setup
    main_section = "Executive Overview"
    passage_1, passage_2 = get_passages()
    passage = passage_1 if option == 1 else passage_2
    
    # Get prompt and create chain
    prompt = get_prompt(option)
    chain = prompt | structured_llm
    
    # Invoke LLM
    print("\n🔄 Processing with LLM...")
    result = chain.invoke({
        "main_section": main_section,
        "passage": passage
    })
    
    # Display results
    pretty_print_metadata(result)
    
    # Build schemas
    document_id = "PROP001"
    parent_id = "PARENT_EXEC_009"
    
    parent_schema = build_parent_schema(document_id, parent_id, result, passage)
    child_schemas = build_child_schemas(document_id, result)
    
    # Link child chunks to parent
    for child in child_schemas:
        parent_schema["child_chunks"].append({
            "id": child["id"],
            "subsection": child["subsection"]
        })
    
    # Print schemas
    print_schemas(parent_schema, child_schemas)
    
    # Insert into database
    print("\n" + "=" * 100)
    print("DATABASE INSERTION")
    print("=" * 100)
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        insert_parent_chunk(cursor, conn, parent_schema)
        insert_child_chunks(cursor, conn, child_schemas)
        
        cursor.close()
        conn.close()
        
        print("\n✅ All data successfully stored in PostgreSQL!")
        
    except Exception as e:
        print(f"\n❌ Database error: {e}")

if __name__ == "__main__":
    main()