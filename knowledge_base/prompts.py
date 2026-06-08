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

5. If a section does NOT contain subsection headings:

- Store the entire section content under the section.
- Return an empty subsection list.

Example:

Example:

{{
    "section_name": "Business Context",
    "content": "...",
    "subsections": []
}}

=====================================================
STRICT CONTENT PRESERVATION RULES
=====================================================

This task is an extraction task, NOT a summarization task.

The objective is to preserve every piece of content from the proposal exactly as it appears.

MANDATORY RULES:

1. Preserve ALL text.

- Do not omit any sentence.
- Do not omit any paragraph.
- Do not omit any heading.
- Do not omit any bullet point.
- Do not omit any numbered item.
- Do not omit any activity list.
- Do not omit any phase description.
- Do not omit any table-like content.
- Do not omit any notes.
- Do not omit any examples.

2. Preserve wording exactly.

- Do NOT rewrite.
- Do NOT paraphrase.
- Do NOT simplify.
- Do NOT improve grammar.
- Do NOT shorten content.
- Do NOT merge sentences.

3. Preserve structure exactly.

If the original content contains:

• bullet points

- bullet points

1. numbered lists

a. alphabetic lists

Phase 1:
Phase 2:

they must remain in the extracted content.

4. Preserve line breaks.

The content field should contain the original formatting as closely as possible.

If the source contains:

Phase 1: Design & Discovery

Activities:

• Conduct stakeholder interviews

• Assess existing infrastructure

then the extracted content must contain the same line breaks and bullets.

5. Preserve complete section content.

Every character belonging to a section or subsection must appear somewhere in the output.

No content may be discarded.

6. Never summarize.

This is NOT a content generation task.

This is NOT a proposal writing task.

This is NOT a compression task.

This is a document structure extraction task.

7. Content Fidelity Check

Before returning the response:

- Verify every section contains all source text assigned to that section.
- Verify every subsection contains all source text assigned to that subsection.
- Verify no bullet points have been removed.
- Verify no numbered items have been removed.
- Verify no activities have been removed.
- Verify no phases have been removed.

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
CRITICAL EXTRACTION REQUIREMENT
=====================================================

The content field must contain the original extracted text.

The content field must NOT contain:

- summaries
- condensed text
- rewritten text
- paraphrased text

The content field must contain verbatim proposal content.

The proposal content should be copied, not regenerated.

=====================================================
GENERIC NAMING RULES
=====================================================

Section names and subsection names must be reusable across multiple proposals.

Do NOT use:

- Client names
- Company names
- Organization names
- Product names
- Brand names
- Customer names
- Personal names
- Project names
- Account names
- Geographic locations when they are client-specific

Examples:

BAD:

- Alignment with Any Hour Group, LLC's Needs
- ABC Corporation Reporting Challenges
- Microsoft Data Strategy
- XYZ Bank Current State Assessment

GOOD:

- Client Requirements Alignment
- Reporting Challenges
- Data Strategy
- Current State Assessment

BAD:

- Any Hour Group Business Objectives
- ABC Manufacturing Future Vision

GOOD:

- Business Objectives
- Future State Vision

If a heading contains a client name or company name:

1. Preserve the original content exactly.
2. Replace only the heading with a generalized business-oriented heading.
3. Use terminology commonly found in consulting proposals and enterprise knowledge bases.

Examples:

Original Heading:
"Alignment with Any Hour Group, LLC's Needs"

Return:
"Client Requirements Alignment"

Original Heading:
"ABC Corporation Reporting Challenges"

Return:
"Reporting Challenges"

Original Heading:
"Microsoft Data Platform Strategy"

Return:
"Data Platform Strategy"

Original Heading:
"XYZ Bank Business Objectives"

Return:
"Business Objectives"

The generated section and subsection names should be reusable across different clients while preserving the original content.


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

These are examples only.

Create section names that best match the content.

4. Within each section:

- Identify distinct business concepts.
- Create meaningful subsection names.
- Assign content to the most appropriate subsection.

5. If a section contains only a single business concept:

Return:

Example:

{{
    "section_name": "Business Context",
    "content": "...",
    "subsections": []
}}

Do NOT create unnecessary subsection headings.

=====================================================
SECTION NAMING RULES
=====================================================

Section names should:

- Represent major proposal themes.
- Follow consulting and proposal terminology.
- Improve future retrieval quality.
- Be meaningful when viewed independently.

Avoid generic names such as:

- Introduction
- Overview
- Details
- Information
- Content
- Miscellaneous

=====================================================
SUBSECTION NAMING RULES
=====================================================

Subsection names should:

- Represent a specific business concept.
- Improve semantic retrieval.
- Use proposal terminology.
- Be meaningful independently.

Examples:

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

Use these as guidance only.

=====================================================
CONTENT RULES
=====================================================

- Preserve original content exactly.
- Do not summarize.
- Do not rewrite.
- Do not paraphrase.
- Do not hallucinate information.
- Split content logically.
- Keep related content together.
- Create multiple subsections only when necessary.

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