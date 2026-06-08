from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2
)

prompt = ChatPromptTemplate.from_template(
"""
You are a senior consulting proposal writer.

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

Instructions:

1. Generate content for the ENTIRE section.
2. Use the CLIENT QUESTIONNAIRE as the primary source of truth.
3. Use the retrieved knowledge only as supporting evidence.
4. Cover all subsection topics naturally within a single cohesive narrative.
5. Do not create subsection headings, bullet points, or numbered lists unless explicitly required by the context.
6. Maintain professional, proposal-ready consulting language.
7. Highlight the client's current challenges, business opportunities, proposed approach, and expected outcomes where relevant.
8. Ensure the content is aligned with the provided metadata and questionnaire.
9. Do not invent facts, assumptions, technologies, requirements, or business details that are not supported by the questionnaire or retrieved knowledge.
10. Return only the final section content without any preamble or explanation.

CRITICAL RULE:
- If the SUBSECTION KNOWLEDGE section is empty, contains no chunks, contains only blank values, or contains no meaningful information, return exactly:

NO_CHUNKS_AVAILABLE

- Do not generate any proposal content when this condition is met.
- Do not return explanations, apologies, notes, or additional text.

CONTENT:
"""
)

chain = prompt | llm


def generate_content(
    questionnaire: str,
    section: str,
    sub_sections: dict,
    metadata : dict
):

    knowledge = []

    for subsection_name, chunks in sub_sections.items():

        chunk_text = []

        for chunk in chunks:

            text = (
                chunk.get("content")
                or chunk.get("chunk_text")
                or chunk.get("text")
                or ""
            )

            chunk_text.append(text)

        knowledge.append(
            f"""
Subsection: {subsection_name}

Knowledge:
{chr(10).join(chunk_text)}
"""
        )

    response = chain.invoke(
        {
            "questionnaire": questionnaire,
            "metadata":metadata,
            "section": section,
            "knowledge": "\n\n".join(knowledge)
        }
    )

    content = response.content.strip()

    if content == "NO_CHUNKS_AVAILABLE":
        return ""

    return content  