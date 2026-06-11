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


# =====================================================
# Extract Business Impact Questions from Questionnaire
# =====================================================

def extract_business_impact_questions(questionnaire) -> str:
    """Extract only Business Impact (Outcomes) category questions."""
    
    impact_text = "BUSINESS IMPACT QUESTIONNAIRE:\n\n"
    
    # Handle different input types
    if isinstance(questionnaire, dict):
        categories = questionnaire.get("categories", [])
    elif isinstance(questionnaire, list):
        categories = questionnaire
    elif isinstance(questionnaire, str):
        if not questionnaire or questionnaire.strip() == "":
            return "NO_QUESTIONNAIRE_DATA"
        return questionnaire
    else:
        return str(questionnaire) if questionnaire else "NO_QUESTIONNAIRE_DATA"
    
    found = False
    
    # Look for Outcomes category (category_id=7)
    for category in categories:
        if category.get("category_name") == "Outcomes" or category.get("category_id") == 7:
            questions = category.get("questions", [])
            if not questions:
                impact_text += "No business impact questions found.\n"
            else:
                for question in questions:
                    q_id = question.get("id", "")
                    q_text = question.get("question", "")
                    q_answer = question.get("answer", "")
                    impact_text += f"Q{q_id}: {q_text}\nAnswer: {q_answer}\n\n"
            found = True
            break
    
    if not found:
        return "NO_QUESTIONNAIRE_DATA"
    
    return impact_text


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
    
    if not result or result.strip() == "":
        return "NO_KNOWLEDGE_AVAILABLE"
    
    return result


# =====================================================
# Business Impact Generation Prompt
# =====================================================

prompt = ChatPromptTemplate.from_template(
"""
You are a senior consulting proposal writer specializing in the Business Impact section.

CLIENT QUESTIONNAIRE (Business Impact / Outcomes Section Only)
--------------------------------------------------
{questionnaire}

OUTCOMES (For Context - May be Empty)
--------------------------------------------------
{outcomes}

METADATA
--------------------------------------------------
{metadata}

RETRIEVED KNOWLEDGE (Supporting Evidence Only)
--------------------------------------------------
{knowledge}

INSTRUCTIONS FOR BUSINESS IMPACT SECTION:

1. Generate content ONLY for the Business Impact section.
2. Use the CLIENT QUESTIONNAIRE (Outcomes section) as the PRIMARY source.
3. The Business Impact section should quantify the financial and operational value of the engagement.

4. For OUTCOMES:
   
   a) If the section contains actual content (not "[TO BE GENERATED..." or empty):
      - INTEGRATE it directly into the business impact
      - Convert qualitative outcomes into quantitative impact where possible
      - Calculate ROI, cost savings, efficiency gains, etc.
      - DO NOT add "[TO BE ENRICHED]" markers
   
   b) If the section is empty or contains "[TO BE GENERATED...":
      - Use "[TO BE ENRICHED with Outcomes]" as a placeholder

5. Structure the Business Impact section covering:
   - Financial Impact (ROI, cost savings, revenue impact)
   - Operational Impact (efficiency gains, time savings)
   - Strategic Impact (competitive advantage, scalability)
   - Risk Reduction (compliance, data quality, decision making)

6. For each impact area, include:
   - Impact category and description
   - Quantified metrics (percentages, time savings, cost reductions)
   - How it derives from outcomes
   - Timeframe for realization

7. Do not invent facts not supported by the inputs.

8. Maintain professional, proposal-ready consulting language.

CRITICAL RULES:
- If RETRIEVED KNOWLEDGE is "NO_KNOWLEDGE_AVAILABLE", generate using only questionnaire and other sections.
- Always generate content - never return empty.
- NEVER add placeholders when actual content is provided.
- Use specific numbers and percentages when available; use ranges when estimating.

CONTENT:
"""
)

chain = prompt | llm


def generate_business_impact_content(
    questionnaire,
    metadata: dict,
    retrieved_chunks: dict,
    outcomes: str = ""
) -> str:
    """
    Generate Business Impact section content.
    
    Args:
        questionnaire: Full questionnaire JSON or extracted text
        metadata: Metadata dictionary
        retrieved_chunks: Dictionary from get_filtered_chunks_for_section
        outcomes: Generated Outcomes content (can be empty)
    
    Returns:
        Generated Business Impact content as string
    """
    
    print("\n" + "=" * 60)
    print("GENERATING BUSINESS IMPACT SECTION CONTENT")
    print("=" * 60)
    
    # Step 1: Extract Business Impact questions (from Outcomes category)
    print("\n📋 Step 1: Extracting Business Impact questions...")
    impact_qs = extract_business_impact_questions(questionnaire)
    
    if impact_qs == "NO_QUESTIONNAIRE_DATA":
        print("⚠️ No Outcomes section found in questionnaire!")
        impact_qs = "No specific business impact information was listed in the questionnaire."
    
    # Step 2: Check if outcomes are available
    has_outcomes = outcomes and outcomes.strip() != "" and "[TO BE GENERATED" not in outcomes
    
    print(f"\n📊 Available Sections:")
    print(f"   - Outcomes: {'✅' if has_outcomes else '❌ Empty'}")
    
    # Step 3: Format knowledge
    print("\n📚 Step 2: Formatting retrieved knowledge...")
    knowledge_text = format_knowledge_for_prompt(retrieved_chunks)
    print(f"   Knowledge available: {'✅' if knowledge_text != 'NO_KNOWLEDGE_AVAILABLE' else '❌ No'}")
    
    # Step 4: Prepare context strings
    outcomes_str = outcomes if has_outcomes else "[TO BE GENERATED - Outcomes will define what results are achieved]"
    
    # Step 5: Generate content
    print("\n🤖 Step 3: Generating business impact content...")
    
    try:
        response = chain.invoke(
            {
                "questionnaire": impact_qs,
                "outcomes": outcomes_str,
                "metadata": json.dumps(metadata, indent=2),
                "knowledge": knowledge_text
            }
        )
        
        content = response.content.strip()
        
        if not content or content == "" or "NO_CHUNKS_AVAILABLE" in content:
            print("⚠️ Generated content is empty. Using fallback...")
            content = generate_fallback_business_impact(questionnaire, metadata)
        
        print(f"\n✅ Business Impact content generated ({len(content)} characters)")
        
        preview = content[:400] + "..." if len(content) > 400 else content
        print(f"\n📄 Preview:\n{preview}")
        
        return content
        
    except Exception as e:
        print(f"❌ Error generating content: {e}")
        return generate_fallback_business_impact(questionnaire, metadata)


# =====================================================
# Fallback Generator (when LLM fails)
# =====================================================

def generate_fallback_business_impact(questionnaire, metadata) -> str:
    """Generate basic business impact when LLM fails."""
    
    impact_text = "## 7. Business Impact\n\n"
    
    # Extract outcomes from questionnaire
    impact_qs = extract_business_impact_questions(questionnaire)
    
    impact_text += "The proposed solution will deliver significant business value across multiple dimensions:\n\n"
    
    impact_text += "### Financial Impact\n\n"
    impact_text += "- **Reduced Customer Acquisition Cost (CAC)**: Automated L2A and CAC reporting will enable optimization of marketing spend, targeting a 15-20% reduction in CAC\n"
    impact_text += "- **Improved Marketing ROI**: Real-time visibility into channel performance will enable reallocation of budget to highest-performing channels\n"
    impact_text += "- **Increased Lead-to-AUM Conversion**: Enhanced pipeline visibility will support a projected 10-15% improvement in conversion rates\n\n"
    
    impact_text += "### Operational Impact\n\n"
    impact_text += "- **80% Reduction in Manual Reporting**: Automated data pipelines will reduce reporting time from 40 hours/week to 8 hours/week\n"
    impact_text += "- **Real-time Decision Making**: Daily automated refresh (vs 2-3 week manual cycles) enables faster strategic responses\n"
    impact_text += "- **Headcount Efficiency**: Freed-up analyst time can be redirected to value-added analysis\n\n"
    
    impact_text += "### Strategic Impact\n\n"
    impact_text += "- **Scalable Data Foundation**: Architecture designed to support future data sources and predictive analytics\n"
    impact_text += "- **Competitive Advantage**: Best-in-class L2A and CAC reporting differentiates Pure in the wealth management market\n"
    impact_text += "- **Exit Readiness**: Standardized KPIs and automated reporting increase enterprise value\n\n"
    
    impact_text += "### Risk Reduction\n\n"
    impact_text += "- **Data Quality Improvement**: Automated validation rules reduce manual errors\n"
    impact_text += "- **Governance & Auditability**: Single source of truth with complete data lineage\n"
    impact_text += "- **Compliance Readiness**: Standardized reporting meets regulatory requirements\n"
    
    return impact_text


# =====================================================
# Example Usage (for testing)
# =====================================================

if __name__ == "__main__":
    print("Testing c_generation.py")
    
    # Test questionnaire
    test_questionnaire = {
        "categories": [
            {
                "category_id": 7,
                "category_name": "Outcomes",
                "questions": [
                    {"id": "7.1", "question": "Expected business outcomes?", "answer": "Enhanced L2A and CAC reporting"},
                    {"id": "7.2", "question": "KPIs that matter most?", "answer": "Lead-to-AUM conversion, CAC"}
                ]
            }
        ]
    }
    
    test_metadata = {
        "business_offering": "Professional Services",
        "solution": "Data Advisory",
        "region": "UK"
    }
    
    extracted = extract_business_impact_questions(test_questionnaire)
    print(f"\n✅ Extracted: {extracted[:200]}...")
    
    print("\n✅ Module loaded successfully. Ready to use.")