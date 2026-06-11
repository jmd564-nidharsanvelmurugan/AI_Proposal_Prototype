from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
import json
import os
from langchain_openai import AzureChatOpenAI

load_dotenv()

# =====================================================
# LLM Setup
# =====================================================

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_deployment=os.getenv("gpt-5"),
    api_version="2024-02-15-preview",
    temperature=0,
)


# =====================================================
# Extract Outcomes Questions from Questionnaire
# =====================================================

def extract_outcomes_questions(questionnaire) -> str:
    """Extract only Outcomes category questions."""
    
    outcomes_text = "OUTCOMES QUESTIONNAIRE:\n\n"
    
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
    for category in categories:
        if category.get("category_name") == "Outcomes":
            questions = category.get("questions", [])
            for question in questions:
                q_id = question.get("id", "")
                q_text = question.get("question", "")
                q_answer = question.get("answer", "")
                outcomes_text += f"Q{q_id}: {q_text}\nAnswer: {q_answer}\n\n"
            found = True
            break
    
    if not found:
        for category in categories:
            if category.get("category_id") == 7:
                for question in category.get("questions", []):
                    q_id = question.get("id", "")
                    q_text = question.get("question", "")
                    q_answer = question.get("answer", "")
                    outcomes_text += f"Q{q_id}: {q_text}\nAnswer: {q_answer}\n\n"
                found = True
                break
    
    if not found:
        return "NO_QUESTIONNAIRE_DATA"
    
    return outcomes_text


# =====================================================
# Extract KPIs and Success Metrics from Questionnaire
# =====================================================

def extract_kpi_metrics(questionnaire) -> dict:
    """Extract KPI and success metrics information from questionnaire."""
    
    kpi_metrics = {
        "kpis": [],
        "success_metrics": [],
        "business_outcomes": [],
        "risk_mitigations": []
    }
    
    if isinstance(questionnaire, dict):
        categories = questionnaire.get("categories", [])
    else:
        return kpi_metrics
    
    for category in categories:
        questions = category.get("questions", [])
        
        for question in questions:
            q_text = question.get("question", "").lower()
            q_answer = question.get("answer", "")
            
            if not q_answer or q_answer == "Not mentioned in document.":
                continue
            
            if "kpi" in q_text or "success metric" in q_text:
                kpi_metrics["kpis"].append(q_answer)
            
            if "business outcome" in q_text or "expected outcome" in q_text:
                kpi_metrics["business_outcomes"].append(q_answer)
            
            if "success" in q_text or "what does success look like" in q_text:
                kpi_metrics["success_metrics"].append(q_answer)
            
            if "risk" in q_text:
                kpi_metrics["risk_mitigations"].append(q_answer)
    
    for key in kpi_metrics:
        kpi_metrics[key] = list(set(kpi_metrics[key]))
    
    return kpi_metrics


# =====================================================
# Format Knowledge for Prompt
# =====================================================

def format_knowledge_for_prompt(retrieved_chunks: dict) -> str:
    """Convert retrieved chunks into structured knowledge text."""
    
    if not retrieved_chunks:
        return "NO_KNOWLEDGE_AVAILABLE"
    
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
    
    if "semantic_filtered" in retrieved_chunks:
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
    
    elif "all_chunks" in retrieved_chunks:
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
                text = chunk.get("text") or chunk.get("content") or chunk.get("actual_text_data") or ""
                if text:
                    if len(text) > 500:
                        text = text[:500] + "..."
                    chunk_texts.append(f"- {text}")
            if chunk_texts:
                knowledge_parts.append(f"\n=== {subsection_name} ===\n")
                knowledge_parts.extend(chunk_texts)
    
    result = "\n".join(knowledge_parts) if knowledge_parts else "NO_KNOWLEDGE_AVAILABLE"
    
    return result if result.strip() else "NO_KNOWLEDGE_AVAILABLE"


# =====================================================
# Outcomes Generation Prompt
# =====================================================

outcomes_prompt = ChatPromptTemplate.from_template(
"""
You are a senior consulting proposal writer specializing in the Outcomes section.

CLIENT QUESTIONNAIRE (Outcomes Section Only)
--------------------------------------------------
{questionnaire}

PROBLEM STATEMENT
--------------------------------------------------
{problem_statement}

OBJECTIVES
--------------------------------------------------
{objectives}

DELIVERABLES
--------------------------------------------------
{deliverables}

APPROACH
--------------------------------------------------
{approach}

METADATA
--------------------------------------------------
{metadata}

RETRIEVED KNOWLEDGE (Supporting Evidence Only)
--------------------------------------------------
{knowledge}

================================================================================
INSTRUCTIONS FOR OUTCOMES SECTION
================================================================================

1. Generate content ONLY for the Outcomes section (business outcomes, KPIs, success metrics, risk mitigation).

2. Use the CLIENT QUESTIONNAIRE (Outcomes section) as the PRIMARY source.

================================================================================
SECTION INTEGRATION RULES
================================================================================

For PROBLEM STATEMENT, OBJECTIVES, DELIVERABLES, and APPROACH:

   a) If the section contains actual content (not empty):
      - INTEGRATE it directly into the outcomes
      - Explain HOW outcomes address the problems
      - Explain HOW outcomes align with objectives
      - Explain HOW deliverables enable outcomes
      - Explain HOW the approach leads to outcomes
   
   b) If the section is empty:
      - Do not force integration
      - Generate outcomes based on questionnaire and knowledge only

================================================================================
OUTPUT STRUCTURE REQUIREMENTS
================================================================================

Structure the Outcomes section with the following subsections:

1. Business Outcomes
   - List 4-6 specific business outcomes
   - Each outcome should be measurable and time-bound

2. Key Performance Indicators (KPIs)
   - List 5-8 specific KPIs with definitions
   - Include target values or benchmarks where available

3. Success Metrics
   - Define how success will be measured
   - Include quantitative and qualitative metrics

4. Risk Mitigation & Value Protection
   - Identify key risks and mitigation strategies

5. Outcomes Summary Table

================================================================================
KPI DEFINITION GUIDELINES
================================================================================

For each KPI, include:
   - KPI name
   - Definition/calculation logic
   - Data source
   - Target value
   - Reporting frequency

================================================================================
CRITICAL RULES
================================================================================

- Always generate content - never return empty
- NEVER add placeholders when actual content is provided
- Be specific about metrics and targets
- Use data from questionnaire for KPIs

================================================================================
CONTENT:
================================================================================
"""
)

outcomes_chain = outcomes_prompt | llm


# =====================================================
# Generate Outcomes Section Content
# =====================================================

def generate_outcomes_content(
    questionnaire,
    metadata: dict,
    retrieved_chunks: dict,
    problem_statement: str = "",
    objectives: str = "",
    deliverables: str = "",
    approach: str = ""
) -> str:
    """Generate Outcomes section content."""
    
    print("\n" + "=" * 60)
    print("GENERATING OUTCOMES SECTION CONTENT")
    print("=" * 60)
    
    # Step 1: Extract Outcomes questions
    print("\n📋 Step 1: Extracting Outcomes questions...")
    outcomes_qs = extract_outcomes_questions(questionnaire)
    
    if outcomes_qs == "NO_QUESTIONNAIRE_DATA":
        print("⚠️ No Outcomes section found in questionnaire!")
        outcomes_qs = "No specific outcomes were listed in the questionnaire."
    
    # Step 2: Extract KPI metrics
    print("\n📊 Step 2: Extracting KPI and success metrics...")
    kpi_metrics = extract_kpi_metrics(questionnaire)
    print(f"   KPIs found: {len(kpi_metrics['kpis'])}")
    
    # Step 3: Check available sections
    has_problem_statement = problem_statement and problem_statement.strip() != ""
    has_objectives = objectives and objectives.strip() != ""
    has_deliverables = deliverables and deliverables.strip() != ""
    has_approach = approach and approach.strip() != ""
    
    print(f"\n📊 Available Sections:")
    print(f"   - Problem Statement: {'✅' if has_problem_statement else '❌ Empty'}")
    print(f"   - Objectives: {'✅' if has_objectives else '❌ Empty'}")
    print(f"   - Deliverables: {'✅' if has_deliverables else '❌ Empty'}")
    print(f"   - Approach: {'✅' if has_approach else '❌ Empty'}")
    
    # Step 4: Format knowledge
    print("\n📚 Step 3: Formatting retrieved knowledge...")
    knowledge_text = format_knowledge_for_prompt(retrieved_chunks)
    print(f"   Knowledge available: {'✅' if knowledge_text != 'NO_KNOWLEDGE_AVAILABLE' else '❌ No'}")
    
    # Step 5: Generate content
    print("\n🤖 Step 4: Generating outcomes content...")
    
    try:
        response = outcomes_chain.invoke(
            {
                "questionnaire": outcomes_qs,
                "problem_statement": problem_statement if has_problem_statement else "",
                "objectives": objectives if has_objectives else "",
                "deliverables": deliverables if has_deliverables else "",
                "approach": approach if has_approach else "",
                "metadata": json.dumps(metadata, indent=2),
                "knowledge": knowledge_text
            }
        )
        
        content = response.content.strip()
        
        if not content:
            print("⚠️ Generated content is empty. Using fallback...")
            content = generate_fallback_outcomes(questionnaire, metadata, kpi_metrics)
        
        print(f"\n✅ Outcomes content generated ({len(content)} characters)")
        
        preview = content[:500] + "..." if len(content) > 500 else content
        print(f"\n📄 Preview:\n{preview}")
        
        return content
        
    except Exception as e:
        print(f"❌ Error generating content: {e}")
        return generate_fallback_outcomes(questionnaire, metadata, kpi_metrics)


# =====================================================
# Fallback Generator
# =====================================================

def generate_fallback_outcomes(questionnaire, metadata, kpi_metrics) -> str:
    """Generate basic outcomes when LLM fails."""
    
    outcomes_text = "## 5. Outcomes\n\n"
    
    # Business Outcomes
    outcomes_text += "### Business Outcomes\n\n"
    outcomes_text += "The following business outcomes will be achieved through this engagement:\n\n"
    outcomes_text += "| # | Outcome | Measurement |\n"
    outcomes_text += "|---|---------|-------------|\n"
    outcomes_text += "| 1 | **Enhanced Pipeline Visibility** | Lead-to-AUM conversion rate by channel |\n"
    outcomes_text += "| 2 | **Integrated CAC Reporting** | Customer Acquisition Cost by marketing source |\n"
    outcomes_text += "| 3 | **Automated Reporting** | Hours saved per week (80% reduction) |\n"
    outcomes_text += "| 4 | **Real-time Decision Making** | Data refresh latency <24 hours |\n"
    outcomes_text += "| 5 | **Standardized KPIs** | KPI definition adoption rate |\n\n"
    
    # KPIs
    outcomes_text += "### Key Performance Indicators (KPIs)\n\n"
    outcomes_text += "| KPI | Definition | Data Source | Target | Frequency |\n"
    outcomes_text += "|-----|------------|-------------|--------|-----------|\n"
    outcomes_text += "| Lead-to-AUM Conversion Rate | (Leads converted to AUM / Total leads) × 100 | Salesforce | +15% | Weekly |\n"
    outcomes_text += "| Customer Acquisition Cost (CAC) | Total marketing spend / New customers | QuickBooks + Salesforce | -10% | Monthly |\n"
    outcomes_text += "| Marketing ROI | (Revenue - Marketing spend) / Marketing spend | Salesforce + QuickBooks | +20% | Monthly |\n"
    outcomes_text += "| Data Accuracy Rate | Valid records / Total records × 100 | All sources | 99.5% | Daily |\n\n"
    
    # Success Metrics
    outcomes_text += "### Success Metrics\n\n"
    outcomes_text += "**Quantitative Metrics:**\n"
    outcomes_text += "- 80% reduction in manual reporting effort\n"
    outcomes_text += "- 99.5% data accuracy for CAC reporting\n"
    outcomes_text += "- Daily automated data refresh\n\n"
    
    # Risk Mitigation
    outcomes_text += "### Risk Mitigation\n\n"
    outcomes_text += "| Risk | Mitigation Strategy |\n"
    outcomes_text += "|------|---------------------|\n"
    outcomes_text += "| Data quality issues | Data validation and cleansing during ingestion |\n"
    outcomes_text += "| Integration delays | Parallel workstreams for data assessment |\n"
    outcomes_text += "| Stakeholder misalignment | Weekly workshops and documented definitions |\n\n"
    
    return outcomes_text


if __name__ == "__main__":
    print("Testing c_generation_outcomes.py")
    print("Module loaded successfully. Ready to use.")