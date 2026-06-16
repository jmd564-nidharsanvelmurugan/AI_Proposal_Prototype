# src/nodes/assembly_node.py
import os
import json
from datetime import datetime
from docx import Document
from docx.shared import Inches, Pt
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
    
    # Get client name
    questionnaire = state.get("questionnaire", {})
    client_name = get_client_name(questionnaire)
    
    try:
        # Create document
        doc = Document()
        
        # Set page margins
        for section in doc.sections:
            section.top_margin = Inches(1)
            section.bottom_margin = Inches(1)
            section.left_margin = Inches(1)
            section.right_margin = Inches(1)
        
        # Add Title
        p = doc.add_paragraph()
        run = p.add_run("AI Proposal Tool")
        run.font.size = Pt(24)
        run.font.bold = True
        p.paragraph_format.space_after = 12
        
        p = doc.add_paragraph()
        run = p.add_run(f"{client_name} - Proposal")
        run.font.size = Pt(14)
        p.paragraph_format.space_after = 6
        
        p = doc.add_paragraph()
        run = p.add_run(f"Generated: {datetime.now().strftime('%B %d, %Y')}")
        run.font.size = Pt(10)
        p.paragraph_format.space_after = 24
        
        doc.add_paragraph("=" * 60)
        doc.add_paragraph()
        
        # Section order and display names
        section_order = [
            ("business_context", "Business Context"),
            ("overview", "Overview"),
            ("understanding", "Understanding"),
            ("objectives", "Objectives"),
            ("deliverables", "Deliverables"),
            ("approach", "Approach"),
            ("outcomes", "Outcomes"),
            ("business_impact", "Business Impact")
        ]
        
        # Process each section - JUST FETCH AND PASTE
        for section_key, section_title in section_order:
            print(f"\n📄 Processing: {section_title}")
            
            # Get content from state
            section_data = state.get(section_key)
            if not section_data or not isinstance(section_data, dict):
                print(f"   ⚠️ No data for {section_title}, skipping...")
                continue
            
            content = section_data.get("content", "")
            if not content:
                print(f"   ⚠️ Empty content for {section_title}, skipping...")
                continue
            
            print(f"   ✅ Adding content: {len(content)} characters")
            
            # Add section heading
            p = doc.add_paragraph()
            run = p.add_run(section_title)
            run.font.size = Pt(16)
            run.font.bold = True
            p.paragraph_format.space_before = 24
            p.paragraph_format.space_after = 12
            
            # JUST PASTE THE CONTENT AS-IS
            p = doc.add_paragraph(content)
            p.paragraph_format.space_after = 24
            
            # Add separator
            doc.add_paragraph("-" * 60)
            doc.add_paragraph()
        
        # Generate filename
        filename = generate_proposal_filename(state)
        
        # Create x_results folder
        os.makedirs("x_results", exist_ok=True)
        
        # Save document
        word_path = f"x_results/{filename}.docx"
        doc.save(word_path)
        print(f"\n✅ Word document saved to: {word_path}")
        
        # Generate summary
        summary = generate_proposal_summary(state)
        
        # Store in state
        state["proposal"] = {
            "filename": filename,
            "word_path": word_path,
            "summary": summary,
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