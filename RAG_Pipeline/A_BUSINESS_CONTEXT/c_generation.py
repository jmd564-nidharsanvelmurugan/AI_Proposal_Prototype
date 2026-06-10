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

SUBSECTION KNOWLEDGE
--------------------------------------------------
{knowledge}

Instructions for BUSINESS CONTEXT section:

1. Generate content ONLY for the Business Context section.
2. Use the CLIENT QUESTIONNAIRE as the primary source of truth.
3. Use the retrieved knowledge only as supporting evidence and examples.
4. Cover these key areas naturally within a single cohesive narrative:
   - Industry landscape and market trends affecting the client
   - The client's current business situation and strategic position
   - Key stakeholders and their roles in the engagement
   - Business drivers and rationale for this engagement
5. Do not create subsection headings, bullet points, or numbered lists.
6. Maintain professional, proposal-ready consulting language.
7. Write in paragraphs with natural flow between topics.
8. Highlight the client's challenges, opportunities, and strategic needs.
9. Ensure content aligns with the provided metadata and questionnaire.
10. Do not invent facts, assumptions, or details not supported by the questionnaire or retrieved knowledge.

CRITICAL RULE:
- If the SUBSECTION KNOWLEDGE section is empty, contains no chunks, contains only blank values, or contains no meaningful information, return exactly:

NO_CHUNKS_AVAILABLE

- Do not generate any proposal content when this condition is met.
- Do not return explanations, apologies, notes, or additional text.

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
    
    Args:
        questionnaire: Client questionnaire text
        metadata: Metadata dictionary with solution, region, etc.
        retrieved_chunks: Dictionary of retrieved chunks per subsection
                         (from get_filtered_chunks_for_section)
    
    Returns:
        Generated Business Context content as string
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
    
    # Prepare knowledge from retrieved chunks
    knowledge_parts = []
    
    for subsection_name, chunks in retrieved_chunks.items():
        if not chunks:
            continue
            
        chunk_texts = []
        for chunk in chunks:
            # Extract text from chunk
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
    
    print(f"📝 Preparing content with {len(knowledge_parts)} subsections of knowledge")
    
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