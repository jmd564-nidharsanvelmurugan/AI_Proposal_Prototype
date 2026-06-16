# src/nodes/assembly_node.py
import os
import json
from datetime import datetime
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from typing import Optional, Dict, Any
from src.state import GraphState

# =====================================================
# Helper Functions
# =====================================================
def get_client_name(questionnaire):
    """Safely extract client name."""
    if isinstance(questionnaire, list) and len(questionnaire) > 0:
        questionnaire = questionnaire[0]
    if isinstance(questionnaire, dict):
        return (questionnaire.get("company_name") or 
                questionnaire.get("client_name") or 
                questionnaire.get("organization") or 
                questionnaire.get("company") or 
                "Client")
    return "Client"

# =====================================================
# Main Assembly Functions
# =====================================================

def generate_proposal_filename(state: GraphState) -> str:
    """Generate a filename for the proposal."""
    questionnaire = state.get("questionnaire", {})
    client_name = get_client_name(questionnaire)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    clean_name = "".join(c for c in client_name if c.isalnum() or c in " ._-").strip()
    clean_name = clean_name.replace(" ", "_")
    
    return f"Proposal_{clean_name}_{timestamp}"

def generate_proposal_summary(state: GraphState) -> Dict[str, Any]:
    """Generate a summary of the proposal for tracking."""
    sections_completed = state.get("sections_completed", [])
    total_chunks = 0
    
    section_metrics = {}
    section_order = [
        "business_context", "overview", "understanding", "objectives",
        "deliverables", "approach", "outcomes", "business_impact"
    ]
    
    for section_key in section_order:
        section_data = state.get(section_key)
        if section_data and isinstance(section_data, dict):
            content = section_data.get("content", "")
            section_metrics[section_key] = {
                "chunks_used": section_data.get("chunks_used", 0),
                "has_content": bool(content),
                "content_length": len(content)
            }
            total_chunks += section_data.get("chunks_used", 0)
    
    questionnaire = state.get("questionnaire", {})
    client_name = get_client_name(questionnaire)
    
    summary = {
        "client_name": client_name,
        "generated_date": datetime.now().isoformat(),
        "sections_completed": sections_completed,
        "total_sections": len(sections_completed),
        "total_chunks_used": total_chunks,
        "section_metrics": section_metrics,
        "metadata": state.get("metadata_dict", {})
    }
    
    summary_path = "x_results/proposal_summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    
    print(f"📊 Proposal summary saved to: {summary_path}")
    return summary

# =====================================================
# Main LangGraph Node
# =====================================================

def assemble_proposal_node(state: GraphState) -> GraphState:
    """
    LangGraph node that retrieves each section content from state,
    adds the section name as heading, and pastes the content as-is.
    """
    print("\n" + "=" * 80)
    print("📄 ASSEMBLING: Complete Proposal")
    print("=" * 80)

    # ── JMAN brand colours ────────────────────────────────────────────────────
    NAVY      = RGBColor(0x17, 0x38, 0x45)   # #173845 — headings, title
    PINK      = RGBColor(0xFF, 0x61, 0x96)   # #FF6196 — subheadings, dividers
    DARK      = RGBColor(0x1D, 0x1C, 0x1C)   # #1D1C1C — body text
    GRAY      = RGBColor(0x80, 0x80, 0x80)   # #808080 — metadata

    # ── JMAN inline style helpers ─────────────────────────────────────────────
    def set_run_font(run, size_pt, bold=False, color=None):
        run.font.name = "Arial"
        run.font.size = Pt(size_pt)
        run.font.bold = bold
        if color:
            run.font.color.rgb = color

    def add_pink_divider(doc):
        """Bottom-border paragraph that acts as a pink horizontal rule."""
        p = doc.add_paragraph()
        pPr = p._p.get_or_add_pPr()
        pBdr = OxmlElement("w:pBdr")
        bottom = OxmlElement("w:bottom")
        bottom.set(qn("w:val"), "single")
        bottom.set(qn("w:sz"), "8")          # border thickness
        bottom.set(qn("w:space"), "1")
        bottom.set(qn("w:color"), "FF6196")  # pink
        pBdr.append(bottom)
        pPr.append(pBdr)
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        return p

    def add_spacer(doc, space_pt=8):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(space_pt)
        return p

    def add_h1(doc, text):
        p = doc.add_paragraph()
        run = p.add_run(text)
        set_run_font(run, size_pt=16, bold=True, color=NAVY)
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(8)
        return p

    def add_body(doc, text):
        p = doc.add_paragraph(text)
        for run in p.runs:
            set_run_font(run, size_pt=11, color=DARK)
        p.paragraph_format.space_after = Pt(6)
        return p

    # Get client name
    questionnaire = state.get("questionnaire", {})
    client_name = get_client_name(questionnaire)

    try:
        # ── Create document ───────────────────────────────────────────────────
        doc = Document()

        # Page margins — 1 inch all sides
        for section in doc.sections:
            section.top_margin    = Inches(1)
            section.bottom_margin = Inches(1)
            section.left_margin   = Inches(1)
            section.right_margin  = Inches(1)

        # ── Title block ───────────────────────────────────────────────────────
        # Line 1 — document title
        p = doc.add_paragraph()
        run = p.add_run("AI Proposal Tool")
        set_run_font(run, size_pt=24, bold=True, color=NAVY)
        p.paragraph_format.space_after = Pt(4)

        # Line 2 — subtitle (client name + label)
        p = doc.add_paragraph()
        run = p.add_run(f"{client_name} — Proposal")
        set_run_font(run, size_pt=14, color=PINK)
        p.paragraph_format.space_after = Pt(3)

        # Line 3 — metadata (org | date)
        p = doc.add_paragraph()
        run = p.add_run(f"JMAN Group  |  Generated {datetime.now().strftime('%B %d, %Y')}")
        set_run_font(run, size_pt=10, color=GRAY)
        p.paragraph_format.space_after = Pt(12)

        # Pink divider under title
        add_pink_divider(doc)
        add_spacer(doc)

        # ── Section order and display names ───────────────────────────────────
        section_order = [
            ("business_context", "Business Context"),
            ("overview",         "Overview"),
            ("understanding",    "Understanding"),
            ("objectives",       "Objectives"),
            ("deliverables",     "Deliverables"),
            ("approach",         "Approach"),
            ("outcomes",         "Outcomes"),
            ("business_impact",  "Business Impact"),
        ]

        # ── Process each section — fetch and paste ────────────────────────────
        for section_key, section_title in section_order:
            print(f"\n📄 Processing: {section_title}")

            section_data = state.get(section_key)
            if not section_data or not isinstance(section_data, dict):
                print(f"   ⚠️ No data for {section_title}, skipping...")
                continue

            content = section_data.get("content", "")
            if not content:
                print(f"   ⚠️ Empty content for {section_title}, skipping...")
                continue

            print(f"   ✅ Adding content: {len(content)} characters")

            # H1 section heading — navy, bold, Arial 16pt
            add_h1(doc, section_title)

            # Content — pasted as-is, Arial 11pt dark
            add_body(doc, content)

            # Pink divider + spacer after each section
            add_spacer(doc, space_pt=4)
            add_pink_divider(doc)
            add_spacer(doc)

        # ── Generate filename & save ──────────────────────────────────────────
        filename = generate_proposal_filename(state)

        os.makedirs("x_results", exist_ok=True)

        word_path = f"x_results/{filename}.docx"
        doc.save(word_path)
        print(f"\n✅ Word document saved to: {word_path}")

        # Generate summary
        summary = generate_proposal_summary(state)

        # Store in state
        state["proposal"] = {
            "filename":  filename,
            "word_path": word_path,
            "summary":   summary,
            "timestamp": datetime.now().isoformat()
        }

        print("\n" + "=" * 80)
        print("✅ PROPOSAL ASSEMBLY COMPLETE!")
        print("=" * 80)
        print(f"📄 Word Doc: {word_path}")
        print(f"📊 Summary: x_results/proposal_summary.json")
        print("=" * 80)

    except Exception as e:
        print(f"❌ Error during assembly: {e}")
        import traceback
        traceback.print_exc()
        state["error"] = f"Assembly failed: {str(e)}"

    state["sections_completed"].append("Proposal Assembly")

    return state