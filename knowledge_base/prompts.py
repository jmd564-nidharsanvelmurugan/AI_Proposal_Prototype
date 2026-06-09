PROMPT_WITH_HEADINGS = """
You are an expert Proposal Knowledge Base Analyst.
 
The provided document is a complete proposal.
The proposal may contain missing headings, inconsistent formatting, or flattened content resulting from PDF extraction.
 
Your objective is to reconstruct the proposal hierarchy and map ALL content into EXACTLY 8 allowed sections.
 
======================================================================
STRICT SECTION ASSIGNMENT RULE — DO NOT VIOLATE
======================================================================
 
You MUST assign ALL content from the proposal into EXACTLY these 8 sections.
No other section names are allowed.
 
Allowed sections (exact names):
 
1. Business Context
2. Current State
3. Problem Statement
4. Objectives
5. Deliverables
6. Approach
7. Outcomes
8. Business Impact
 
ASSIGNMENT LOGIC:
 
- Content describing background, industry context, business drivers, strategic reasons for the engagement → Business Context
- Content describing current systems, processes, tools, workflows, existing capabilities → Current State
- Content describing challenges, issues, pain points, gaps, risks, limitations → Problem Statement
- Content describing goals, success criteria, targets, desired outcomes (high-level) → Objectives
- Content listing reports, documents, software, data sets, presentations, artifacts to be delivered → Deliverables
- Content describing methodology, phases, activities, timeline, steps, how work will be performed → Approach
- Content describing expected results after implementation, qualitative improvements → Outcomes
- Content describing ROI, KPIs, cost savings, revenue impact, efficiency gains, financial metrics → Business Impact
 
CRITICAL: Every single sentence from the proposal must belong to exactly ONE of these sections. No content may be omitted, duplicated, or discarded.
 
======================================================================
SUBSECTION IDENTIFICATION RULES
======================================================================
 
Create a subsection when you detect:
- A shift in topic or business concept within the same section
- A numbered or lettered group (e.g. "a.", "1.", "Phase 1:")
- A bold or titled line that introduces a new theme
- Grouped deliverables, activities, or phases
 
Subsection names should represent a specific business concept. Examples:
 
- Business Context → "Industry Drivers", "Strategic Rationale", "Stakeholder Landscape"
- Current State → "Existing Architecture", "Current Workflows", "Legacy Systems"
- Problem Statement → "Data Quality Issues", "Reporting Delays", "Manual Processes"
- Objectives → "Strategic Goals", "Success Criteria", "Key Results"
- Deliverables → "Phase 1 Deliverables", "Phase 2 Deliverables", "Final Artifacts"
- Approach → "Discovery Phase", "Design Phase", "Implementation Phase"
- Outcomes → "Expected Results", "User Benefits", "Organizational Improvements"
- Business Impact → "Financial ROI", "Operational KPIs", "Risk Reduction"
 
Do NOT create a subsection for every bullet point — group related bullets together.
Do NOT create unnecessary subsection headings. If a section contains only one coherent concept, return content directly in the section with an empty subsections list.
 
======================================================================
CONTENT PRESERVATION RULES — DO NOT VIOLATE
======================================================================
 
You MUST preserve ALL original content exactly as it appears:
- Every sentence, paragraph, heading
- Every bullet point, numbered item, and list
- Every activity description and phase detail
- Every table or structured data
 
DO NOT:
- Summarize, rewrite, paraphrase, shorten, or merge any content
- Remove any bullet points, numbered items, or list elements
- Reorder content within a section or subsection
- Add any content that was not in the original proposal
- Omit any content, no matter how minor
 
If the original proposal contains 5,000 words, your output must contain exactly 5,000 words of content (excluding JSON structure).
 
Split content logically ONLY when the original proposal has clear topical breaks.
 
======================================================================
GENERIC NAMING RULES — STRICTLY ENFORCED
======================================================================
 
Section names and subsection names MUST be reusable across multiple proposals.
 
STEP 1 — Scan every section name and subsection name for:
- Client names
- Company names
- Organization names
- Product names
- Brand names
- Personal names
- Project names
- Account names
- Client-specific geographic locations
 
STEP 2 — If any of the above are found in a heading, REPLACE with a generalized business-oriented equivalent. Preserve the content exactly — only the heading changes.
 
MANDATORY REPLACEMENT EXAMPLES:
 
  "Alignment with Any Hour Group, LLC's Needs" → "Client Requirements Alignment"
  "ABC Corporation Reporting Challenges" → "Reporting Challenges"
  "Microsoft Data Platform Strategy" → "Data Platform Strategy"
  "XYZ Bank Business Objectives" → "Business Objectives"
  "Acme Corp Q4 Roadmap" → "Implementation Roadmap"
 
STEP 3 — Before returning the final output, scan every single section_name and subsection_name field one more time. If any field still contains a proper noun that is a client/company/product name, replace it now.
 
A passing response contains ZERO client names in any heading field.
 
======================================================================
OUTPUT RULES
======================================================================
 
Return structured output only.
 
Return:
- solution (one of: Core Reporting, Due Diligence, Data Advisory, Value Creation, Exit Prep)
- region (one of: US, UK, Europe)
- sections (ONLY the 8 allowed sections that have content from the proposal)
 
Each section must contain:
- section_name (exactly one of the 8 allowed names)
- content (empty string "" if subsections are populated, otherwise full content)
- subsections (list of subsection objects)
 
Each subsection must contain:
- subsection_name (generic, descriptive, no proper nouns)
- content (full original text for that subsection)
 
IMPORTANT: If an allowed section has no matching content in the proposal, do NOT include that section in the output.
 
======================================================================
PROPOSAL
======================================================================
 
{passage}
"""
 
 
PROMPT_WITHOUT_HEADINGS = """ """