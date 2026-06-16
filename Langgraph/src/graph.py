from langgraph.graph import StateGraph, END
from src.state import GraphState
from src.nodes.metadata_node import extract_metadata_node
from src.nodes.retrieval_node import retrieve_proposals_node
from src.nodes.business_context_node import generate_business_context_node
from src.nodes.overview_node import generate_overview_node  # ← ADD THIS

def create_proposal_graph():
    """Create the LangGraph workflow for proposal generation."""
    
    workflow = StateGraph(GraphState)
    
    # Add nodes
    workflow.add_node("extract_metadata", extract_metadata_node)
    workflow.add_node("retrieve_proposals", retrieve_proposals_node)
    workflow.add_node("generate_business_context", generate_business_context_node)
    workflow.add_node("generate_overview", generate_overview_node)  # ← ADD THIS
    
    # Set entry point
    workflow.set_entry_point("extract_metadata")
    
    # Define edges
    workflow.add_edge("extract_metadata", "retrieve_proposals")
    workflow.add_edge("retrieve_proposals", "generate_business_context")
    workflow.add_edge("generate_business_context", "generate_overview")  # ← ADD THIS
    workflow.add_edge("generate_overview", END)  # ← ADD THIS
    
    # Compile
    return workflow.compile()

def run_proposal_generation(questionnaire: dict) -> dict:
    """Run the complete proposal generation workflow."""
    
    import json
    
    # Initialize state
    initial_state = {
        "questionnaire": questionnaire,
        "questionnaire_text": json.dumps(questionnaire),
        "metadata": None,
        "metadata_dict": None,
        "top_proposals": [],
        "document_ids": [],
        "section_chunks": {},
        "section_queries": {},
        "business_context": None,
        "overview": None,  # ← ADD THIS
        "understanding": None,
        "objectives": None,
        "deliverables": None,
        "approach": None,
        "outcomes": None,
        "business_impact": None,
        "current_section_index": 0,
        "sections_completed": [],
        "error": None
    }
    
    # Compile and run
    app = create_proposal_graph()
    final_state = app.invoke(initial_state)
    
    return final_state