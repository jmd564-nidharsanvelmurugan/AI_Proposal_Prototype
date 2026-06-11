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
# Extract Approach Questions from Questionnaire
# =====================================================

def extract_approach_questions(questionnaire) -> str:
    """Extract only Approach category questions."""
    
    approach_text = "APPROACH QUESTIONNAIRE:\n\n"
    
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
    for category in categories:
        if category.get("category_name") == "Approach":
            questions = category.get("questions", [])
            if not questions:
                approach_text += "No approach questions found.\n"
            else:
                for question in questions:
                    q_id = question.get("id", "")
                    q_text = question.get("question", "")
                    q_answer = question.get("answer", "")
                    approach_text += f"Q{q_id}: {q_text}\nAnswer: {q_answer}\n\n"
            found = True
            break
    
    if not found:
        # Try to find Approach by category_id=6
        for category in categories:
            if category.get("category_id") == 6:
                for question in category.get("questions", []):
                    q_id = question.get("id", "")
                    q_text = question.get("question", "")
                    q_answer = question.get("answer", "")
                    approach_text += f"Q{q_id}: {q_text}\nAnswer: {q_answer}\n\n"
                found = True
                break
    
    if not found:
        return "NO_QUESTIONNAIRE_DATA"
    
    return approach_text


# =====================================================
# Extract Tech Stack Information from Questionnaire
# =====================================================

def extract_tech_stack(questionnaire) -> dict:
    """
    Extract technology stack information from questionnaire.
    Returns dict with systems, platforms, and tools.
    """
    
    tech_stack = {
        "systems": [],
        "data_platforms": [],
        "reporting_tools": [],
        "databases": [],
        "integrations_needed": []
    }
    
    if isinstance(questionnaire, dict):
        categories = questionnaire.get("categories", [])
    elif isinstance(questionnaire, list):
        categories = questionnaire
    else:
        return tech_stack
    
    for category in categories:
        questions = category.get("questions", [])
        
        for question in questions:
            q_text = question.get("question", "").lower()
            q_answer = question.get("answer", "")
            
            # Extract systems/platforms
            if "system" in q_text or "platform" in q_text:
                if q_answer and q_answer != "Not mentioned in document.":
                    tech_stack["systems"].append(q_answer)
            
            # Extract data platforms (Fabric, Synapse, Snowflake, etc.)
            if "data platform" in q_text or "cloud/platform" in q_text:
                if q_answer and q_answer != "Not mentioned in document.":
                    tech_stack["data_platforms"].append(q_answer)
            
            # Extract reporting/BI tools
            if "reporting" in q_text or "analytics tool" in q_text or "bi" in q_text:
                if q_answer and q_answer != "Not mentioned in document.":
                    tech_stack["reporting_tools"].append(q_answer)
            
            # Extract databases
            if "database" in q_text or "data source" in q_text:
                if q_answer and q_answer != "Not mentioned in document.":
                    tech_stack["databases"].append(q_answer)
            
            # Extract integrations needed
            if "integration" in q_text:
                if q_answer and q_answer != "Not mentioned in document.":
                    tech_stack["integrations_needed"].append(q_answer)
    
    # Clean up duplicates
    for key in tech_stack:
        tech_stack[key] = list(set(tech_stack[key]))
    
    return tech_stack


# =====================================================
# Check if Data Platform is Required
# =====================================================

def check_data_platform_required(questionnaire) -> bool:
    """
    Check if the project requires a data platform based on questionnaire.
    """
    if isinstance(questionnaire, dict):
        categories = questionnaire.get("categories", [])
    elif isinstance(questionnaire, list):
        categories = questionnaire
    else:
        return False
    
    data_platform_keywords = [
        "data platform", "data warehouse", "data lake", "fabric", 
        "synapse", "snowflake", "bigquery", "redshift", "data model",
        "data pipeline", "etl", "elt", "data infrastructure"
    ]
    
    for category in categories:
        questions = category.get("questions", [])
        
        for question in questions:
            q_text = question.get("question", "").lower()
            q_answer = question.get("answer", "").lower()
            
            for keyword in data_platform_keywords:
                if keyword in q_text or keyword in q_answer:
                    return True
    
    return False


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
    
    if not result or result.strip() == "":
        return "NO_KNOWLEDGE_AVAILABLE"
    
    return result


# =====================================================
# Approach Generation Prompt
# =====================================================
approach_prompt = ChatPromptTemplate.from_template(
"""
You are a senior consulting proposal writer specializing in the Approach section.

CLIENT QUESTIONNAIRE (Approach Section Only)
--------------------------------------------------
{questionnaire}

BUSINESS CONTEXT
--------------------------------------------------
{business_context}

PROBLEM STATEMENT
--------------------------------------------------
{problem_statement}

OBJECTIVES
--------------------------------------------------
{objectives}

DELIVERABLES (What needs to be delivered)
--------------------------------------------------
{deliverables}

METADATA
--------------------------------------------------
{metadata}

TECH STACK INFORMATION (if available)
--------------------------------------------------
{tech_stack}

RETRIEVED KNOWLEDGE (Supporting Evidence Only)
--------------------------------------------------
{knowledge}

================================================================================
INSTRUCTIONS FOR APPROACH SECTION
================================================================================

1. Generate content ONLY for the Approach section (methodology, phasing, activities, timeline).

2. Use the CLIENT QUESTIONNAIRE (Approach section) as the PRIMARY source.

================================================================================
SECTION INTEGRATION RULES
================================================================================

For BUSINESS CONTEXT, PROBLEM STATEMENT, OBJECTIVES, and DELIVERABLES:

   a) If the section contains actual content (not "[TO BE GENERATED..." or empty):
      - INTEGRATE it directly into the approach
      - Explain HOW the approach addresses the specific problems
      - Explain HOW the approach achieves the stated objectives
      - Explain HOW the approach delivers the required deliverables
      - DO NOT add placeholder markers like "[TO BE ENRICHED]"
   
   b) If the section is empty or contains "[TO BE GENERATED...":
      - Do not force integration
      - Generate approach based on questionnaire and knowledge only

================================================================================
STRUCTURE REQUIREMENTS
================================================================================

STRUCTURE the approach logically into phases. Choose the format based on timeline:

   Option A (If timeline is 1-4 weeks): Use Week-by-week breakdown
   Option B (If timeline is 4+ weeks): Use Phase-based breakdown (e.g., Phase 1, Phase 2)

For EACH PHASE include:
   - Phase/Week name (e.g., "Week 1: Mobilization & Discovery" or "Phase 1: Assessment")
   - Duration (extract from questionnaire timeline if available)
   - Key activities and workshops (be specific, not vague)
   - Stakeholders involved (e.g., executive sponsors, business users, technical teams)
   - Outputs/deliverables from this phase

================================================================================
TECH STACK HANDLING (CRITICAL)
================================================================================

   a) Check if DATA PLATFORM is required:
      - Look at TECH STACK INFORMATION section
      - Look for keywords in questionnaire: "Fabric", "Synapse", "Snowflake", "BigQuery", "Redshift", "Databricks", "data platform", "data warehouse", "data lake"
      
      If YES:
      - Use TECH STACK INFORMATION as the PRIMARY source
      - Extract specific platform names (Microsoft Fabric, Azure Synapse, Snowflake, etc.)
      - Mention how the approach leverages and integrates with these existing platforms
      - Include specific activities like "Assess current Fabric data models", "Design Synapse pipelines"
   
   b) If DATA PLATFORM is NOT required:
      - Use RETRIEVED KNOWLEDGE as the secondary source
      - Look for similar approaches from past proposals
      - Extract methodology patterns from knowledge

   c) If no tech stack in questionnaire AND no knowledge available:
      - Use standard best-practice approach
      - Do not invent specific platform names
      - Use generic terms like "data platform" or "reporting solution"

================================================================================
FLOW & FEASIBILITY
================================================================================

7. Include a clear flow showing: Understanding → Designing → Building → Delivering

8. Address FEASIBILITY considerations:
   - Data quality assessment and remediation
   - System access requirements and dependencies
   - Data governance and ownership
   - Integration challenges and solutions

================================================================================
OUTPUT FORMAT REQUIREMENTS
================================================================================

9. Use professional, proposal-ready consulting language.

10. Use bullet points for activities and workshops.

11. Include a summary table at the end:

   | Phase/Week | Duration | Key Activities | Key Outputs |
   |------------|----------|----------------|--------------|
   | Week 1: Mobilization | 1 week | Kick-off, access setup | Project plan |
   | Week 2-3: Design | 2 weeks | Workshops, mock-ups | KPI book, mock-ups |
   | Week 4: Planning | 1 week | Roadmap, estimation | Implementation plan |

================================================================================
CRITICAL RULES (DO NOT VIOLATE)
================================================================================

- If RETRIEVED KNOWLEDGE is "NO_KNOWLEDGE_AVAILABLE" and no tech stack, generate using questionnaire only
- Always generate content - never return empty
- NEVER add placeholders like "[TO BE ENRICHED]" when actual content is provided
- Be specific about activities - NOT "conduct workshops" but "conduct KPI definition workshop with marketing and finance teams"
- Use the timeline from questionnaire (look for Q6.6, Q7.6, or timeline answers)
- Extract stakeholder names from questionnaire (e.g., Jason Carver, Lee Equity Partners)
- Reference specific deliverables by name (KPI Book, Data Model, Power BI mock-ups, etc.)

================================================================================
EXAMPLE OUTPUT STRUCTURE
================================================================================

## 3. Approach

### Phase/Week 1: [Name]
**Duration:** [X weeks/days]

**Key Activities:**
- [Specific activity 1]
- [Specific activity 2]
- [Specific activity 3]

**Stakeholders Involved:**
- [Stakeholder 1]: [Role]
- [Stakeholder 2]: [Role]

**Outputs:**
- [Output 1]
- [Output 2]

### Phase/Week 2: [Name]
... (repeat for each phase)

### Summary Table
[Table with phases, duration, activities, outputs]

================================================================================
CONTENT:
================================================================================
"""
)

approach_chain = approach_prompt | llm


# =====================================================
# Generate Approach Section Content
# =====================================================

def generate_approach_content(
    questionnaire,
    metadata: dict,
    retrieved_chunks: dict,
    business_context: str = "",
    problem_statement: str = "",
    objectives: str = "",
    deliverables: str = ""
) -> str:
    """
    Generate Approach section content.
    
    Args:
        questionnaire: Full questionnaire JSON or extracted text
        metadata: Metadata dictionary
        retrieved_chunks: Dictionary from get_filtered_chunks_for_section
        business_context: Generated Business Context content (can be empty)
        problem_statement: Generated Problem Statement content (can be empty)
        objectives: Generated Objectives content (can be empty)
        deliverables: Generated Deliverables content (can be empty)
    
    Returns:
        Generated Approach content as string
    """
    
    print("\n" + "=" * 60)
    print("GENERATING APPROACH SECTION CONTENT")
    print("=" * 60)
    
    # Step 1: Extract Approach questions
    print("\n📋 Step 1: Extracting Approach questions...")
    approach_qs = extract_approach_questions(questionnaire)
    
    if approach_qs == "NO_QUESTIONNAIRE_DATA":
        print("⚠️ No Approach section found in questionnaire!")
        approach_qs = "No specific approach details were listed in the questionnaire."
    
    # Step 2: Extract tech stack
    print("\n🔧 Step 2: Extracting tech stack information...")
    tech_stack = extract_tech_stack(questionnaire)
    data_platform_required = check_data_platform_required(questionnaire)
    
    print(f"   Data platform required: {'✅ Yes' if data_platform_required else '❌ No'}")
    print(f"   Systems found: {tech_stack['systems'][:3] if tech_stack['systems'] else 'None'}")
    print(f"   Data platforms: {tech_stack['data_platforms'][:3] if tech_stack['data_platforms'] else 'None'}")
    
    # Step 3: Check available sections
    has_business_context = business_context and business_context.strip() != "" and "[TO BE GENERATED" not in business_context
    has_problem_statement = problem_statement and problem_statement.strip() != "" and "[TO BE GENERATED" not in problem_statement
    has_objectives = objectives and objectives.strip() != "" and "[TO BE GENERATED" not in objectives
    has_deliverables = deliverables and deliverables.strip() != "" and "[TO BE GENERATED" not in deliverables
    
    print(f"\n📊 Available Sections:")
    print(f"   - Business Context: {'✅' if has_business_context else '❌ Empty'}")
    print(f"   - Problem Statement: {'✅' if has_problem_statement else '❌ Empty'}")
    print(f"   - Objectives: {'✅' if has_objectives else '❌ Empty'}")
    print(f"   - Deliverables: {'✅' if has_deliverables else '❌ Empty'}")
    
    # Step 4: Format knowledge based on data platform requirement
    print("\n📚 Step 3: Formatting retrieved knowledge...")
    
    if data_platform_required and tech_stack and any(tech_stack.values()):
        # Use tech stack as primary source
        knowledge_text = "TECH STACK FOUND IN QUESTIONNAIRE (Primary Source):\n\n"
        knowledge_text += json.dumps(tech_stack, indent=2)
        print(f"   Using TECH STACK as primary source ({sum(len(v) for v in tech_stack.values())} items)")
    else:
        # Use retrieved chunks as fallback
        knowledge_text = format_knowledge_for_prompt(retrieved_chunks)
        print(f"   Knowledge available: {'✅' if knowledge_text != 'NO_KNOWLEDGE_AVAILABLE' else '❌ No'}")
        print(f"   Source: Retrieved from past proposals")
    
    # Step 5: Prepare context strings with placeholders if needed
    business_context_str = business_context if has_business_context else "[TO BE GENERATED - Business Context will provide industry and client context]"
    problem_statement_str = problem_statement if has_problem_statement else "[TO BE GENERATED - Problem Statement will help prioritize approach]"
    objectives_str = objectives if has_objectives else "[TO BE GENERATED - Objectives will define what approach must achieve]"
    deliverables_str = deliverables if has_deliverables else "[TO BE GENERATED - Deliverables will define what needs to be produced]"
    
    # Step 6: Generate content
    print("\n🤖 Step 4: Generating approach content...")
    
    try:
        response = approach_chain.invoke(
            {
                "questionnaire": approach_qs,
                "business_context": business_context_str,
                "problem_statement": problem_statement_str,
                "objectives": objectives_str,
                "deliverables": deliverables_str,
                "metadata": json.dumps(metadata, indent=2),
                "tech_stack": json.dumps(tech_stack, indent=2) if any(tech_stack.values()) else "NO_TECH_STACK_FOUND",
                "knowledge": knowledge_text
            }
        )
        
        content = response.content.strip()
        
        if not content or content == "" or "NO_CHUNKS_AVAILABLE" in content:
            print("⚠️ Generated content is empty. Using fallback...")
            content = generate_fallback_approach(questionnaire, metadata, tech_stack)
        
        print(f"\n✅ Approach content generated ({len(content)} characters)")
        
        preview = content[:400] + "..." if len(content) > 400 else content
        print(f"\n📄 Preview:\n{preview}")
        
        return content
        
    except Exception as e:
        print(f"❌ Error generating content: {e}")
        return generate_fallback_approach(questionnaire, metadata, tech_stack)


# =====================================================
# Fallback Generator (when LLM fails)
# =====================================================

def generate_fallback_approach(questionnaire, metadata, tech_stack) -> str:
    """Generate basic approach when LLM fails."""
    
    approach_text = "## 3. Approach\n\n"
    
    # Extract timeline if available
    timeline = "4 weeks"
    approach_text += f"This {timeline} approach is structured into four key phases:\n\n"
    
    # Phase 1: Mobilization
    approach_text += "### Phase 1: Mobilization & Discovery (Week 1)\n\n"
    approach_text += "**Activities:**\n"
    approach_text += "- Kick-off workshop with key stakeholders\n"
    approach_text += "- Current state reporting landscape analysis\n"
    approach_text += "- Stakeholder interviews (sales, finance, operations)\n"
    approach_text += "- System access and data extraction setup\n\n"
    approach_text += "**Outputs:**\n"
    approach_text += "- Project kick-off deck\n"
    approach_text += "- Current state assessment\n"
    approach_text += "- Data access matrix\n\n"
    
    # Phase 2: Design
    approach_text += "### Phase 2: Requirements & Design (Week 2-3)\n\n"
    approach_text += "**Activities:**\n"
    approach_text += "- Requirements gathering workshops\n"
    approach_text += "- KPI definition and alignment sessions\n"
    
    # Add tech stack specific content
    if tech_stack.get("data_platforms"):
        platforms = ", ".join(tech_stack["data_platforms"][:3])
        approach_text += f"- Data platform assessment (existing {platforms})\n"
        approach_text += f"- Architecture design leveraging {platforms}\n"
    else:
        approach_text += "- Data model and architecture design\n"
    
    approach_text += "- Dashboard mock-up creation\n"
    approach_text += "- Data quality and gap assessment\n\n"
    
    approach_text += "**Outputs:**\n"
    approach_text += "- KPI definition book\n"
    approach_text += "- Data model design\n"
    approach_text += "- Dashboard mock-ups\n"
    approach_text += "- Gap assessment report\n\n"
    
    # Phase 3: Planning
    approach_text += "### Phase 3: Planning & Roadmap (Week 4)\n\n"
    approach_text += "**Activities:**\n"
    approach_text += "- Implementation planning sessions\n"
    
    if tech_stack.get("integrations_needed"):
        integrations = ", ".join(tech_stack["integrations_needed"][:3])
        approach_text += f"- Integration planning for {integrations}\n"
    
    approach_text += "- Resource and cost estimation\n"
    approach_text += "- Risk assessment and mitigation planning\n"
    approach_text += "- Governance framework design\n\n"
    
    approach_text += "**Outputs:**\n"
    approach_text += "- Implementation roadmap\n"
    approach_text += "- Cost estimate and resource plan\n"
    approach_text += "- Risk register\n"
    approach_text += "- Governance framework\n\n"
    
    # Stakeholder involvement
    approach_text += "### Stakeholder Involvement\n\n"
    approach_text += "| Stakeholder | Role | Involvement |\n"
    approach_text += "|-------------|------|-------------|\n"
    approach_text += "| Executive Sponsors | Strategic direction | Weekly steerco |\n"
    approach_text += "| Business Users | Requirements | Workshops, reviews |\n"
    approach_text += "| Technical Teams | Implementation | Architecture, data access |\n"
    approach_text += "| Data Owners | Source systems | Deep-dive sessions |\n\n"
    
    # Success criteria
    approach_text += "### Success Criteria\n\n"
    approach_text += "The approach will be considered successful when:\n"
    approach_text += "1. All stakeholders are aligned on requirements and KPI definitions\n"
    approach_text += "2. Data quality gaps are identified and prioritized\n"
    approach_text += "3. Architecture design is approved by technical team\n"
    approach_text += "4. Implementation plan with cost estimates is delivered\n"
    approach_text += "5. Governance framework is established\n"
    
    return approach_text