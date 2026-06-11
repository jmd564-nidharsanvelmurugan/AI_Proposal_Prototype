from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import json
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2
)


# =====================================================
# Extract Deliverables Questions from Questionnaire
# =====================================================

def extract_deliverables_questions(questionnaire) -> str:
    """Extract only Deliverables category questions."""
    
    deliverables_text = "DELIVERABLES QUESTIONNAIRE:\n\n"
    
    # Handle different input types
    if isinstance(questionnaire, dict):
        categories = questionnaire.get("categories", [])
    elif isinstance(questionnaire, list):
        categories = questionnaire
    elif isinstance(questionnaire, str):
        # If it's already a string, check if it's empty
        if not questionnaire or questionnaire.strip() == "":
            return "NO_QUESTIONNAIRE_DATA"
        return questionnaire
    else:
        return str(questionnaire) if questionnaire else "NO_QUESTIONNAIRE_DATA"
    
    found = False
    for category in categories:
        if category.get("category_name") == "Deliverables":
            questions = category.get("questions", [])
            if not questions:
                deliverables_text += "No deliverable questions found.\n"
            else:
                for question in questions:
                    q_id = question.get("id", "")
                    q_text = question.get("question", "")
                    q_answer = question.get("answer", "")
                    deliverables_text += f"Q{q_id}: {q_text}\nAnswer: {q_answer}\n\n"
            found = True
            break
    
    if not found:
        # Try to find Deliverables by category_id=5
        for category in categories:
            if category.get("category_id") == 5:
                for question in category.get("questions", []):
                    q_id = question.get("id", "")
                    q_text = question.get("question", "")
                    q_answer = question.get("answer", "")
                    deliverables_text += f"Q{q_id}: {q_text}\nAnswer: {q_answer}\n\n"
                found = True
                break
    
    if not found:
        return "NO_QUESTIONNAIRE_DATA"
    
    return deliverables_text


# =====================================================
# Format Knowledge for Prompt
# =====================================================

def format_knowledge_for_prompt(retrieved_chunks: dict) -> str:
    """Convert retrieved chunks into structured knowledge text."""
    
    if not retrieved_chunks:
        return "NO_KNOWLEDGE_AVAILABLE"
    
    # Check if there are any chunks with content
    has_chunks = False
    for chunks in retrieved_chunks.values():
        if chunks and len(chunks) > 0:
            # Check if chunks have actual text content
            for chunk in chunks:
                if chunk.get("text") or chunk.get("actual_text_data"):
                    has_chunks = True
                    break
        if has_chunks:
            break
    
    if not has_chunks:
        return "NO_KNOWLEDGE_AVAILABLE"
    
    knowledge_parts = []
    
    # Determine chunk type
    chunk_type = "unknown"
    if "semantic_filtered" in retrieved_chunks:
        chunk_type = "semantic"
    elif "all_chunks" in retrieved_chunks:
        chunk_type = "all"
    else:
        chunk_type = "subsection"
    
    if chunk_type == "semantic":
        chunks = retrieved_chunks.get("semantic_filtered", [])
        if chunks:
            knowledge_items = []
            for c in chunks[:5]:
                text = c.get('text', '') or c.get('actual_text_data', '')
                score = c.get('similarity_score', 0)
                if text:
                    if len(text) > 800:
                        text = text[:800] + "..."
                    knowledge_items.append(f"[Relevance: {score:.3f}] {text}")
            
            if knowledge_items:
                knowledge_parts.append("=== Most Relevant Retrieved Knowledge ===\n")
                knowledge_parts.extend(knowledge_items)
    
    elif chunk_type == "all":
        chunks = retrieved_chunks.get("all_chunks", [])
        if chunks:
            knowledge_items = []
            for c in chunks[:8]:
                text = c.get('text', '') or c.get('actual_text_data', '')
                if text:
                    if len(text) > 500:
                        text = text[:500] + "..."
                    knowledge_items.append(f"- {text}")
            
            if knowledge_items:
                knowledge_parts.append("=== All Retrieved Knowledge ===\n")
                knowledge_parts.extend(knowledge_items)
    
    else:
        # Subsection-based chunks
        for subsection_name, chunks in retrieved_chunks.items():
            if not chunks:
                continue
            
            chunk_texts = []
            for chunk in chunks[:3]:
                text = (
                    chunk.get("text") or 
                    chunk.get("content") or 
                    chunk.get("actual_text_data") or 
                    ""
                )
                if text:
                    if len(text) > 500:
                        text = text[:500] + "..."
                    chunk_texts.append(f"- {text}")
            
            if chunk_texts:
                knowledge_parts.append(f"\n=== {subsection_name} ===\n")
                knowledge_parts.extend(chunk_texts)
    
    result = "\n".join(knowledge_parts) if knowledge_parts else "NO_KNOWLEDGE_AVAILABLE"
    
    # Final safety check - don't return empty
    if not result or result.strip() == "":
        return "NO_KNOWLEDGE_AVAILABLE"
    
    return result


# =====================================================
# Deliverables Generation Prompt
# =====================================================

prompt = ChatPromptTemplate.from_template(
"""
You are a senior consulting proposal writer specializing in the Deliverables section.

CLIENT QUESTIONNAIRE (Deliverables Section Only)
--------------------------------------------------
{questionnaire}

BUSINESS CONTEXT (For Context - May be Empty)
--------------------------------------------------
{business_context}

PROBLEM STATEMENT (For Context - May be Empty)
--------------------------------------------------
{problem_statement}

OBJECTIVES (For Context - May be Empty)
--------------------------------------------------
{objectives}

METADATA
--------------------------------------------------
{metadata}

RETRIEVED KNOWLEDGE (Supporting Evidence Only)
--------------------------------------------------
{knowledge}

INSTRUCTIONS FOR DELIVERABLES SECTION:

1. Generate content ONLY for the Deliverables section.
2. Use the CLIENT QUESTIONNAIRE (Deliverables section) as the PRIMARY source.
3. Use BUSINESS CONTEXT, PROBLEM STATEMENT, and OBJECTIVES to enrich deliverables when available.
4. If any of these sections are empty or contain placeholders, generate using available information.
5. Use retrieved knowledge only as supporting evidence and examples.
6. Structure the deliverables logically (e.g., Assessment → Design → Planning)
7. Include these components for each deliverable where applicable:
   - Deliverable name and description
   - Format (PowerPoint, Excel, Word, etc.)
   - Key components or sections
   - [TO BE ENRICHED] marker for elements that would benefit from missing sections

8. Include a summary table with:
   - Deliverable name
   - Format
   - Due (infer from questionnaire timeline if available)

9. Do not invent facts not supported by the inputs.

10. Maintain professional, proposal-ready consulting language.

CRITICAL RULES:
- If RETRIEVED KNOWLEDGE is "NO_KNOWLEDGE_AVAILABLE", generate using only questionnaire and other sections.
- Always generate content - never return empty.
- Use placeholders like [TO BE ENRICHED with Problem Statement] where other sections would add value.

CONTENT:
"""
)

chain = prompt | llm


def generate_deliverables_content(
    questionnaire,
    metadata: dict,
    retrieved_chunks: dict,
    business_context: str = "",
    problem_statement: str = "",
    objectives: str = ""
) -> str:
    """
    Generate Deliverables section content.
    
    Args:
        questionnaire: Full questionnaire JSON or extracted text
        metadata: Metadata dictionary
        retrieved_chunks: Dictionary from get_filtered_chunks_for_section
        business_context: Generated Business Context content (can be empty)
        problem_statement: Generated Problem Statement content (can be empty)
        objectives: Generated Objectives content (can be empty)
    
    Returns:
        Generated Deliverables content as string
    """
    
    print("\n" + "=" * 60)
    print("GENERATING DELIVERABLES SECTION CONTENT")
    print("=" * 60)
    
    # Step 1: Extract Deliverables questions
    print("\n📋 Step 1: Extracting Deliverables questions...")
    deliverables_qs = extract_deliverables_questions(questionnaire)
    
    if deliverables_qs == "NO_QUESTIONNAIRE_DATA":
        print("⚠️ No Deliverables section found in questionnaire!")
        deliverables_qs = "No specific deliverables were listed in the questionnaire."
    
    # Step 2: Check available sections
    has_business_context = business_context and business_context.strip() != "" and "[TO BE GENERATED" not in business_context
    has_problem_statement = problem_statement and problem_statement.strip() != "" and "[TO BE GENERATED" not in problem_statement
    has_objectives = objectives and objectives.strip() != "" and "[TO BE GENERATED" not in objectives
    
    print(f"\n📊 Available Sections:")
    print(f"   - Business Context: {'✅' if has_business_context else '❌ Empty'}")
    print(f"   - Problem Statement: {'✅' if has_problem_statement else '❌ Empty'}")
    print(f"   - Objectives: {'✅' if has_objectives else '❌ Empty'}")
    
    # Step 3: Format knowledge
    print("\n📚 Step 2: Formatting retrieved knowledge...")
    knowledge_text = format_knowledge_for_prompt(retrieved_chunks)
    print(f"   Knowledge available: {'✅' if knowledge_text != 'NO_KNOWLEDGE_AVAILABLE' else '❌ No'}")
    
    # Step 4: Prepare context strings
    business_context_str = business_context if has_business_context else "[TO BE GENERATED - Business Context will provide industry and client context]"
    problem_statement_str = problem_statement if has_problem_statement else "[TO BE GENERATED - Problem Statement will help prioritize deliverables]"
    objectives_str = objectives if has_objectives else "[TO BE GENERATED - Objectives will define what deliverables must achieve]"
    
    # Step 5: Generate content
    print("\n🤖 Step 3: Generating deliverables content...")
    
    try:
        response = chain.invoke(
            {
                "questionnaire": deliverables_qs,
                "business_context": business_context_str,
                "problem_statement": problem_statement_str,
                "objectives": objectives_str,
                "metadata": json.dumps(metadata, indent=2),
                "knowledge": knowledge_text
            }
        )
        
        content = response.content.strip()
        
        # Check if content is valid
        if not content or content == "" or "NO_CHUNKS_AVAILABLE" in content:
            print("⚠️ Generated content is empty. Using fallback...")
            content = generate_fallback_deliverables(questionnaire, metadata)
        
        print(f"\n✅ Deliverables content generated ({len(content)} characters)")
        
        # Preview
        preview = content[:400] + "..." if len(content) > 400 else content
        print(f"\n📄 Preview:\n{preview}")
        
        return content
        
    except Exception as e:
        print(f"❌ Error generating content: {e}")
        return generate_fallback_deliverables(questionnaire, metadata)


# =====================================================
# Fallback Generator (when LLM fails)
# =====================================================

def generate_fallback_deliverables(questionnaire, metadata) -> str:
    """Generate basic deliverables when LLM fails."""
    
    deliverables_text = "## 4. Deliverables\n\n"
    
    # Extract basic deliverables from questionnaire
    deliverables_qs = extract_deliverables_questions(questionnaire)
    
    if "KPI Book" in deliverables_qs or "KPI" in deliverables_qs:
        deliverables_text += "### Assessment Deliverables\n\n"
        deliverables_text += "**KPI Definition Book**\n"
        deliverables_text += "- List of agreed KPIs with calculation logic\n"
        deliverables_text += "- Data requirements per KPI\n"
        deliverables_text += "- Owner and benchmark recommendations\n"
        deliverables_text += "- Format: PowerPoint + Excel\n\n"
    
    if "Data Model" in deliverables_qs:
        deliverables_text += "### Design Deliverables\n\n"
        deliverables_text += "**Data Model Design**\n"
        deliverables_text += "- Conceptual and logical data models\n"
        deliverables_text += "- Entity relationship diagrams\n"
        deliverables_text += "- Source-to-target mapping\n"
        deliverables_text += "- Format: PowerPoint + Draw.io\n\n"
    
    if "Power BI mock-ups" in deliverables_qs or "mock-ups" in deliverables_qs:
        deliverables_text += "**Power BI Mock-ups**\n"
        deliverables_text += "- 8 dashboard views as specified\n"
        deliverables_text += "- L2A and CAC visualizations\n"
        deliverables_text += "- Format: PBIX + PDF\n\n"
    
    if "Gap Assessment" in deliverables_qs:
        deliverables_text += "**Data Gap Assessment**\n"
        deliverables_text += "- Current vs required data coverage\n"
        deliverables_text += "- Data quality evaluation\n"
        deliverables_text += "- Architecture suitability review\n"
        deliverables_text += "- Format: PowerPoint\n\n"
    
    if "Technical Approach" in deliverables_qs:
        deliverables_text += "### Planning Deliverables\n\n"
        deliverables_text += "**Technical Approach Document**\n"
        deliverables_text += "- QuickBooks integration design\n"
        deliverables_text += "- Pipeline architecture\n"
        deliverables_text += "- Transformation logic\n"
        deliverables_text += "- Format: PowerPoint + Word\n\n"
    
    if "Implementation Plan" in deliverables_qs or "Roadmap" in deliverables_qs:
        deliverables_text += "**Implementation Roadmap**\n"
        deliverables_text += "- Phased plan (8-12 weeks)\n"
        deliverables_text += "- Resource estimates\n"
        deliverables_text += "- Cost estimates\n"
        deliverables_text += "- Format: PowerPoint + Excel\n\n"
    
    deliverables_text += "\n### Deliverables Summary\n\n"
    deliverables_text += "| Deliverable | Format | Due |\n"
    deliverables_text += "|-------------|--------|-----|\n"
    deliverables_text += "| KPI Definition Book | PPT + Excel | Week 2 |\n"
    deliverables_text += "| Data Model Design | PPT + Draw.io | Week 2 |\n"
    deliverables_text += "| Power BI Mock-ups | PBIX + PDF | Week 3 |\n"
    deliverables_text += "| Data Gap Assessment | PPT | Week 1 |\n"
    deliverables_text += "| Technical Approach | PPT + Word | Week 3 |\n"
    deliverables_text += "| Implementation Roadmap | PPT + Excel | Week 3 |\n"
    
    return deliverables_text


# =====================================================
# Example Usage (for testing)
# =====================================================

if __name__ == "__main__":
    print("Testing c_generation.py")
    
    # Test questionnaire
    test_questionnaire = {
        "categories": [
            {
                "category_id": 5,
                "category_name": "Deliverables",
                "questions": [
                    {"id": "5.1", "question": "What deliverables are expected?", "answer": "KPI Book, Data Model, Gap Assessment"}
                ]
            }
        ]
    }
    
    test_metadata = {
        "business_offering": "Professional Services",
        "solution": "Data Advisory",
        "region": "UK"
    }
    
    # Test extraction
    extracted = extract_deliverables_questions(test_questionnaire)
    print(f"\n✅ Extracted: {extracted[:200]}...")
    
    print("\n✅ Module loaded successfully. Ready to use.")