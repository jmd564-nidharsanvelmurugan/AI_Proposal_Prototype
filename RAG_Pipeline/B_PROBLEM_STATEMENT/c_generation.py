from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import json
import os
from langchain_openai import AzureChatOpenAI

load_dotenv()

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_deployment=os.getenv("gpt-5"),
    api_version="2024-02-15-preview",
    temperature=0,
)


prompt = ChatPromptTemplate.from_template("""
You are a senior consulting proposal writer specializing in Problem Statement sections.

CLIENT QUESTIONNAIRE (All sections – use especially the problem‑related questions)
--------------------------------------------------
{questionnaire}

METADATA
--------------------------------------------------
{metadata}

SECTION
--------------------------------------------------
{section}

RETRIEVED KNOWLEDGE (Supporting evidence, industry benchmarks, common pain points)
--------------------------------------------------
{knowledge}

INSTRUCTIONS FOR PROBLEM STATEMENT SECTION:

1. Write a **single, cohesive narrative** (2‑4 paragraphs) that describes the **current problems** the client is facing.
2. Use the CLIENT QUESTIONNAIRE as your **primary source of truth** for problems, pain points, and challenges.
3. Use the retrieved knowledge **only as supporting evidence** (e.g., industry‑wide trends, typical consequences).
4. Do **NOT** mention solutions, deliverables, or what should be done.
5. Do **NOT** create subsection headings, bullet points, or numbered lists.
6. Organize the narrative naturally:
   - Start with the **context** of the problems (systems, processes, data).
   - Then describe **specific pain points** (manual work, delays, inaccuracies, integration gaps).
   - Finally explain the **consequences** (business impact, risk, missed opportunities).
7. Maintain professional, proposal‑ready consulting language.
8. Write in plain paragraphs with a logical flow.
9. Highlight the **urgency** and **severity** of the problems (but stay factual).
10. Do **not** invent facts not supported by the questionnaire or knowledge.

CRITICAL RULES:
- If RETRIEVED KNOWLEDGE is empty or "NO_KNOWLEDGE_AVAILABLE", still generate the problem statement using ONLY the questionnaire.
- Never return "NO_CHUNKS_AVAILABLE". Always produce content if the questionnaire contains any problem descriptions.
- If the questionnaire lacks sufficient problem information, state that clearly (e.g., "The client has not provided detailed problem descriptions...").

CONTENT:
""")

chain = prompt | llm


def generate_problem_statement_content(
    questionnaire: str,
    metadata: dict,
    retrieved_chunks: dict
) -> str:
    """
    Generate Problem Statement content from retrieved chunks and questionnaire.
    """
    print("\n" + "=" * 60)
    print("GENERATING PROBLEM STATEMENT CONTENT")
    print("=" * 60)

    # Check if we have any knowledge chunks
    has_chunks = any(chunks for chunks in retrieved_chunks.values() if chunks)

    # Prepare knowledge text
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
                    # Truncate for prompt size
                    if len(text) > 800:
                        text = text[:800] + "..."
                    texts.append(text)
            if texts:
                knowledge_parts.append(f"=== {sub_name} ===\n" + "\n".join(f"  • {t}" for t in texts[:3]))
        knowledge_text = "\n\n".join(knowledge_parts) if knowledge_parts else "NO_KNOWLEDGE_AVAILABLE"
    else:
        knowledge_text = "NO_KNOWLEDGE_AVAILABLE"

    print(f"📚 Knowledge prepared: {'has chunks' if has_chunks else 'no chunks'}")

    # Generate content
    response = chain.invoke({
        "questionnaire": questionnaire,
        "metadata": json.dumps(metadata, indent=2),
        "section": "Problem Statement",
        "knowledge": knowledge_text
    })

    content = response.content.strip()
    if not content or content == "NO_CHUNKS_AVAILABLE":
        print("⚠️ No content generated – using fallback.")
        # Fallback: generate from questionnaire only
        fallback = chain.invoke({
            "questionnaire": questionnaire,
            "metadata": json.dumps(metadata, indent=2),
            "section": "Problem Statement",
            "knowledge": "NO_KNOWLEDGE_AVAILABLE"
        })
        content = fallback.content.strip()

    print(f"✅ Problem Statement generated ({len(content)} characters)")
    preview = content[:300] + "..." if len(content) > 300 else content
    print(f"\n📄 Preview:\n{preview}")
    return content