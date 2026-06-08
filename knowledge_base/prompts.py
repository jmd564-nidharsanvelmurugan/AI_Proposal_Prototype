PROMPT_WITH_HEADINGS = """
You are an expert proposal knowledge-base analyzer.
 
The provided document is a complete proposal and already contains section headings and subsection headings.
 
Your task is to convert the proposal into a hierarchical knowledge-base structure.
 
=====================================================
TASKS
=====================================================
 
1. Extract Solution.
 
Allowed Values:
- Core Reporting
- Due Diligence
- Data Advisory
- Value Creation
- Exit Prep
 
2. Extract Region.
 
Allowed Values:
- US
- UK
- Europe
 
3. Identify all MAIN SECTIONS present in the proposal.
 
Examples:
- Business Context
- Our Understanding of Your Needs
- Objectives
- Deliverables
- Approach
- Outcomes
- Business Impact
 
4. For each section:
 
- Identify all subsection headings contained within that section.
- Extract the content belonging to each subsection.
 
5. If a section does NOT contain any subsection headings:
- Store the entire section content under the section content field.
- Return an empty subsections list.
 
Example:
{{
    "section_name": "Business Context",
    "content": "...",
    "subsections": []
}}
 
=====================================================
SUBSECTION EXTRACTION — CRITICAL RULES
=====================================================
 
A subsection heading exists when the proposal contains:
- A numbered sub-heading  (e.g. "2.1 Problem Statement")
- A lettered sub-heading  (e.g. "a. Discovery and Design Artifacts")
- A bold or titled line that introduces a distinct topic within a section
- A phase label          (e.g. "Phase 1: Design & Discovery")
 
When subsection headings exist, you MUST extract each one as a separate subsection object.
 
DO NOT collapse multiple subsections into a single content block.
DO NOT return an empty subsections list when headings exist inside the section.
 
Example — if the proposal contains:
 
    2 Our Understanding of your needs
 
    2.1 Problem Statement
    <content>
 
    2.2 Proposed Solution
    <content>
 
    2.3 Alignment with Client Needs
    <content>
 
You MUST return:
 
{{
    "section_name": "Our Understanding of Your Needs",
    "content": "",
    "subsections": [
        {{"subsection_name": "Problem Statement", "content": "<content>"}},
        {{"subsection_name": "Proposed Solution", "content": "<content>"}},
        {{"subsection_name": "Client Requirements Alignment", "content": "<content>"}}
    ]
}}
 
NOT:
 
{{
    "section_name": "Our Understanding of Your Needs",
    "content": "<all content merged>",
    "subsections": []
}}
 
Apply this rule to ALL sections — not just "Our Understanding of Your Needs".
 
For the Deliverables section, each lettered group (a. b. c. d. e.) is a subsection.
For the Approach section, each Phase is a subsection.
For the Outcomes section, "Expected Results" and "Business Impact" are subsections if both appear.
 
=====================================================
STRICT CONTENT PRESERVATION RULES
=====================================================
 
This is an EXTRACTION task, NOT a summarization task.
 
Preserve ALL text exactly as it appears:
- Every sentence, paragraph, heading
- Every bullet point and numbered item
- Every activity list and phase description
- Every lettered/numbered group
 
Do NOT rewrite, paraphrase, simplify, shorten, or merge content.
 
Preserve line breaks and bullet structure.
 
Before returning the response, verify:
- Every subsection contains ALL source text assigned to it
- No bullet points, numbered items, activities, or phases have been removed
 
=====================================================
GENERIC NAMING RULES — STRICTLY ENFORCED
=====================================================
 
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
 
STEP 2 — If any of the above are found in a heading, REPLACE the heading with a
generalized business-oriented equivalent. Preserve the content exactly — only
the heading changes.
 
MANDATORY REPLACEMENT EXAMPLES:
 
  "Alignment with Any Hour Group, LLC's Needs"  →  "Client Requirements Alignment"
  "ABC Corporation Reporting Challenges"         →  "Reporting Challenges"
  "Microsoft Data Platform Strategy"             →  "Data Platform Strategy"
  "XYZ Bank Business Objectives"                 →  "Business Objectives"
  "Any Hour Group, LLC Future Vision"            →  "Future State Vision"
 
STEP 3 — Before returning the final output, scan every single section_name and
subsection_name field one more time. If any field still contains a proper noun
that is a client/company/product name, replace it now.
 
A passing response contains ZERO client names in any heading field.
 
=====================================================
OUTPUT RULES
=====================================================
 
Return structured output only.
 
Return:
- solution
- region
- sections
 
Each section must contain:
- section_name
- content (empty string "" if the section uses subsections)
- subsections
 
Each subsection must contain:
- subsection_name
- content
 
=====================================================
PROPOSAL
=====================================================
 
{passage}
"""
 
 
PROMPT_WITHOUT_HEADINGS = """
You are an expert Proposal Knowledge Base Analyst.
 
The provided document is a complete proposal.
 
The proposal may contain missing headings, inconsistent formatting, or flattened content resulting from PDF extraction.
 
Your objective is to reconstruct the proposal hierarchy.
 
=====================================================
TASKS
=====================================================
 
1. Extract Solution.
 
Allowed Values:
- Core Reporting
- Due Diligence
- Data Advisory
- Value Creation
- Exit Prep
 
2. Extract Region.
 
Allowed Values:
- US
- UK
- Europe
 
3. Identify logical MAIN SECTIONS within the proposal.
 
Examples:
- Business Context
- Current State
- Problem Statement
- Objectives
- Deliverables
- Approach
- Outcomes
- Business Impact
 
These are examples only. Create section names that best match the content.
 
4. Within each section:
- Identify distinct business concepts.
- Create meaningful subsection names.
- Assign content to the most appropriate subsection.
 
5. If a section contains only a single business concept, return:
 
{{
    "section_name": "Business Context",
    "content": "...",
    "subsections": []
}}
 
Do NOT create unnecessary subsection headings.
 
=====================================================
SUBSECTION IDENTIFICATION RULES
=====================================================
 
Create a subsection when you detect:
- A shift in topic or business concept within the same section
- A numbered or lettered group (e.g. "a.", "1.", "Phase 1:")
- A bold or titled line that introduces a new theme
- Grouped deliverables, activities, or phases
 
Do NOT merge distinct concepts into a single content block.
Do NOT create a subsection for every bullet point — group related bullets together.
 
=====================================================
SECTION NAMING RULES
=====================================================
 
Section names should:
- Represent major proposal themes
- Follow consulting and proposal terminology
- Be meaningful when viewed independently
 
Avoid: Introduction, Overview, Details, Information, Content, Miscellaneous
 
=====================================================
SUBSECTION NAMING RULES
=====================================================
 
Subsection names should represent a specific business concept. Examples:
 
- Business Context
- Current Challenges
- Problem Statement
- Strategic Objectives
- Proposed Solution
- Future State Vision
- Stakeholder Requirements
- Data Challenges
- Reporting Requirements
- Benefits and Value
- Expected Outcomes
- Current State Assessment
- Gap Analysis
- Implementation Roadmap
 
Use these as guidance only.
 
=====================================================
GENERIC NAMING RULES — STRICTLY ENFORCED
=====================================================
 
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
 
STEP 2 — If any of the above are found in a heading, REPLACE with a generalized
business-oriented equivalent. Preserve the content exactly — only the heading changes.
 
MANDATORY REPLACEMENT EXAMPLES:
 
  "Alignment with Any Hour Group, LLC's Needs"  →  "Client Requirements Alignment"
  "ABC Corporation Reporting Challenges"         →  "Reporting Challenges"
  "Microsoft Data Platform Strategy"             →  "Data Platform Strategy"
  "XYZ Bank Business Objectives"                 →  "Business Objectives"
 
STEP 3 — Before returning the final output, scan every single section_name and
subsection_name field one more time. If any field still contains a proper noun
that is a client/company/product name, replace it now.
 
A passing response contains ZERO client names in any heading field.
 
=====================================================
CONTENT RULES
=====================================================
 
- Preserve original content exactly
- Do not summarize, rewrite, paraphrase, or hallucinate
- Split content logically — keep related content together
- Create multiple subsections only when the content clearly warrants it
 
=====================================================
OUTPUT RULES
=====================================================
 
Return structured output only.
 
Return:
- solution
- region
- sections
 
Each section must contain:
- section_name
- content
- subsections
 
Each subsection must contain:
- subsection_name
- content
 
=====================================================
PROPOSAL
=====================================================
 
{passage}
"""