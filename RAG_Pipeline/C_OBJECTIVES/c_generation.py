from langchain_core.prompts import ChatPromptTemplate
import json

# No LLM initialization here – it will be passed from the main script

def generate_objectives_content(
    questionnaire: str,
    metadata: dict,
    retrieved_chunks: dict,
    llm   # <-- LLM instance passed from main script
) -> str:
    """
    Generate Objectives section content from retrieved chunks and questionnaire.
    """
    print("\n" + "=" * 60)
    print("GENERATING OBJECTIVES CONTENT")
    print("=" * 60)

    # Prepare knowledge text
    has_chunks = any(chunks for chunks in retrieved_chunks.values() if chunks)

    if has_chunks:
        knowledge_parts = []
        for sub_name, chunks in retrieved_chunks.items():
            if not chunks:
                continue
            texts = []
            for chunk in chunks:
                text = (chunk.get("text") or chunk.get("content") or
                        chunk.get("actual_text_data") or chunk.get("chunk_text") or "")
                if text:
                    if len(text) > 800:
                        text = text[:800] + "..."
                    texts.append(text)
            if texts:
                knowledge_parts.append(f"=== {sub_name} ===\n" + "\n".join(f"  • {t}" for t in texts[:3]))
        knowledge_text = "\n\n".join(knowledge_parts) if knowledge_parts else "NO_KNOWLEDGE_AVAILABLE"
    else:
        knowledge_text = "NO_KNOWLEDGE_AVAILABLE"

    print(f"📚 Knowledge prepared: {'has chunks' if has_chunks else 'no chunks'}")

    # Define the prompt for Objectives
    prompt = ChatPromptTemplate.from_template("""
You are a senior consulting proposal writer specializing in Objectives sections.

CLIENT QUESTIONNAIRE (All sections – use especially the future‑state and goal‑related questions)
--------------------------------------------------
{questionnaire}

METADATA
--------------------------------------------------
{metadata}

SECTION
--------------------------------------------------
{section}

RETRIEVED KNOWLEDGE (Supporting evidence, industry benchmarks, best practices)
--------------------------------------------------
{knowledge}

INSTRUCTIONS FOR OBJECTIVES SECTION:

1. Write a **single, cohesive narrative** (2‑4 paragraphs) that describes the **desired future state** the client wants to achieve.
2. Use the CLIENT QUESTIONNAIRE as your **primary source of truth** for goals, success criteria, and desired capabilities.
3. Use the retrieved knowledge **only as supporting evidence** (e.g., industry benchmarks, proven outcomes).
4. Do **NOT** mention deliverables, approach, or implementation details – focus on *what* will be achieved.
5. Do **NOT** create subsection headings, bullet points, or numbered lists.
6. Organise the narrative naturally:
   - Start with the **overarching business goals** (e.g., financial transparency, system harmonisation).
   - Then describe **specific technical objectives** (e.g., integrated data pipelines, modernised platforms).
   - Finally outline **operational / process improvements** (e.g., governed data flows, automation).
7. Maintain professional, proposal‑ready consulting language.
8. Write in plain paragraphs with a logical flow.
9. Highlight the **value** and **strategic importance** of each objective.
10. Do **not** invent facts not supported by the questionnaire or knowledge.

CRITICAL RULES:
- If RETRIEVED KNOWLEDGE is empty or "NO_KNOWLEDGE_AVAILABLE", still generate the objectives using ONLY the questionnaire.
- Never return "NO_CHUNKS_AVAILABLE". Always produce content if the questionnaire contains any goal descriptions.
- If the questionnaire lacks sufficient information, state clearly what the client intends to achieve based on the available data.

CONTENT:
""")

    chain = prompt | llm

    response = chain.invoke({
        "questionnaire": questionnaire,
        "metadata": json.dumps(metadata, indent=2),
        "section": "Objectives",
        "knowledge": knowledge_text
    })

    content = response.content.strip()
    if not content or content == "NO_CHUNKS_AVAILABLE":
        print("⚠️ No content generated – using fallback.")
        fallback = chain.invoke({
            "questionnaire": questionnaire,
            "metadata": json.dumps(metadata, indent=2),
            "section": "Objectives",
            "knowledge": "NO_KNOWLEDGE_AVAILABLE"
        })
        content = fallback.content.strip()

    print(f"✅ Objectives content generated ({len(content)} characters)")
    preview = content[:300] + "..." if len(content) > 300 else content
    print(f"\n📄 Preview:\n{preview}")
    return content