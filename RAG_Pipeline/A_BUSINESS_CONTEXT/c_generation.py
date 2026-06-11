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


# only business context questionairees alone 


prompt = ChatPromptTemplate.from_template(
"""
You are a senior consulting proposal writer specializing in Business Context sections.

CLIENT QUESTIONNAIRE 
--------------------------------------------------
{questionnaire}


METADATA
--------------------------------------------------
{metadata}

SECTION
--------------------------------------------------
{section}

RETRIEVED KNOWLEDGE
--------------------------------------------------
{knowledge}

Instructions for BUSINESS CONTEXT section:

1. Generate content ONLY for the Business Context section.
2. Use the CLIENT QUESTIONNAIRE (Business Context section) as the primary source of truth.
3. Ignore questions from other sections (Overview, Understanding, Objectives, etc.).
4. Use the retrieved knowledge only as supporting evidence and examples.
5. Cover these key areas naturally within a single cohesive narrative.
6. Do not create subsection headings, bullet points, or numbered lists.
7. Maintain professional, proposal-ready consulting language.
8. Write in paragraphs with natural flow between topics.
9. Highlight the client's challenges, opportunities, and strategic needs.
10. Ensure content aligns with the provided metadata and questionnaire.
11. Do not invent facts, assumptions, or details not supported by the questionnaire or retrieved knowledge.

CRITICAL RULE:
- If the RETRIEVED KNOWLEDGE section is empty, contains no chunks, contains only blank values, or contains no meaningful information, return exactly:

NO_CHUNKS_AVAILABLE

- Do not generate any proposal content when this condition is met.

CONTENT:
"""
)


chain = prompt | llm


def generate_business_context_content(
    questionnaire: str,
    metadata: dict,
    retrieved_chunks: dict
) -> str:
    """
    Generate Business Context section content from retrieved chunks.
    
    Supports both:
    - Subsection-based chunks (multiple keys)
    - Semantic query filtered chunks (single "semantic_filtered" key)
    - All chunks mode (single "all_chunks" key)
    """
    
    print("\n" + "=" * 60)
    print("GENERATING BUSINESS CONTEXT CONTENT")
    print("=" * 60)
    
    # Check if there are any chunks
    has_chunks = False
    for subsection_name, chunks in retrieved_chunks.items():
        if chunks and len(chunks) > 0:
            has_chunks = True
            break
    
    if not has_chunks:
        print("⚠️ No chunks available. Returning empty content.")
        return ""
    
    # Determine the type of chunks we have
    chunk_type = "unknown"
    if "semantic_filtered" in retrieved_chunks:
        chunk_type = "semantic"
    elif "all_chunks" in retrieved_chunks:
        chunk_type = "all"
    else:
        chunk_type = "subsection"
    
    print(f"📋 Detected chunk type: {chunk_type}")
    
    # Prepare knowledge from retrieved chunks
    knowledge_parts = []
    
    if chunk_type == "semantic":
        # Semantic query filtered chunks - all under one key with similarity scores
        chunks = retrieved_chunks.get("semantic_filtered", [])
        if chunks:
            knowledge_parts.append(f"""
=== Most Relevant Retrieved Knowledge (Ranked by Relevance) ===

Retrieved Knowledge:
{chr(10).join(f"[Relevance: {c.get('similarity_score', 0):.3f}] {c.get('text', '')[:800]}..." if len(c.get('text', '')) > 800 else f"[Relevance: {c.get('similarity_score', 0):.3f}] {c.get('text', '')}" for c in chunks[:5])}
""")
    
    elif chunk_type == "all":
        # All chunks mode - everything grouped together
        chunks = retrieved_chunks.get("all_chunks", [])
        if chunks:
            knowledge_parts.append(f"""
=== All Retrieved Knowledge ===

{chr(10).join(f"- {c.get('text', '')[:500]}..." if len(c.get('text', '')) > 500 else f"- {c.get('text', '')}" for c in chunks[:8])}
""")
    
    else:
        # Subsection-based chunks
        for subsection_name, chunks in retrieved_chunks.items():
            if not chunks:
                continue
            
            chunk_texts = []
            for chunk in chunks:
                text = (
                    chunk.get("text") or 
                    chunk.get("content") or 
                    chunk.get("actual_text_data") or 
                    chunk.get("chunk_text") or 
                    ""
                )
                if text:
                    chunk_texts.append(text)
            
            if chunk_texts:
                knowledge_parts.append(f"""
=== {subsection_name} ===

Retrieved Knowledge:
{chr(10).join(f"- {t[:500]}..." if len(t) > 500 else f"- {t}" for t in chunk_texts[:3])}
""")
    
    knowledge_text = "\n\n".join(knowledge_parts) if knowledge_parts else "NO_KNOWLEDGE_AVAILABLE"
    
    print(f"📝 Preparing content with {len(knowledge_parts)} knowledge sections")
    
    # Generate content
    response = chain.invoke(
        {
            "questionnaire": questionnaire,
            "metadata": json.dumps(metadata, indent=2),
            "section": "Business Context",
            "knowledge": knowledge_text
        }
    )
    
    content = response.content.strip()
    
    if content == "NO_CHUNKS_AVAILABLE":
        print("⚠️ No chunks available for generation. Returning empty.")
        return ""
    
    print("✅ Business Context content generated successfully")
    return content