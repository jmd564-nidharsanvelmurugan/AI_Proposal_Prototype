from langgraph.graph import StateGraph, END
from src.state import GraphState
from src.nodes.metadata_node import extract_metadata_node
from src.nodes.retrieval_node import retrieve_proposals_node
from src.nodes.business_context_node import generate_business_context_node
from src.nodes.overview_node import generate_overview_node
from src.nodes.understanding_node import generate_understanding_node
from src.nodes.objectives_node import generate_objectives_node
from src.nodes.deliverables_node import generate_deliverables_node
from src.nodes.approach_node import generate_approach_node
from src.nodes.outcomes_node import generate_outcomes_node
from src.nodes.business_impact_node import generate_business_impact_node
from src.nodes.assembly_node import assemble_proposal_node  # ← ADD THIS

def create_proposal_graph():
    """Create the LangGraph workflow for proposal generation."""
    
    workflow = StateGraph(GraphState)
    
    # Add nodes
    workflow.add_node("extract_metadata", extract_metadata_node)
    workflow.add_node("retrieve_proposals", retrieve_proposals_node)
    workflow.add_node("generate_business_context", generate_business_context_node)
    workflow.add_node("generate_overview", generate_overview_node)
    workflow.add_node("generate_understanding", generate_understanding_node)
    workflow.add_node("generate_objectives", generate_objectives_node)
    workflow.add_node("generate_deliverables", generate_deliverables_node)
    workflow.add_node("generate_approach", generate_approach_node)
    workflow.add_node("generate_outcomes", generate_outcomes_node)
    workflow.add_node("generate_business_impact", generate_business_impact_node)
    workflow.add_node("assemble_proposal", assemble_proposal_node)  # ← ADD THIS
    
    # Set entry point
    workflow.set_entry_point("extract_metadata")
    
    # Define edges
    workflow.add_edge("extract_metadata", "retrieve_proposals")
    workflow.add_edge("retrieve_proposals", "generate_business_context")
    workflow.add_edge("generate_business_context", "generate_overview")
    workflow.add_edge("generate_overview", "generate_understanding")
    workflow.add_edge("generate_understanding", "generate_objectives")
    workflow.add_edge("generate_objectives", "generate_deliverables")
    workflow.add_edge("generate_deliverables", "generate_approach")
    workflow.add_edge("generate_approach", "generate_outcomes")
    workflow.add_edge("generate_outcomes", "generate_business_impact")
    workflow.add_edge("generate_business_impact", "assemble_proposal")  # ← ADD THIS
    workflow.add_edge("assemble_proposal", END)  # ← ADD THIS
    
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
        "overview": None,
        "understanding": None,
        "objectives": None,
        "deliverables": None,
        "approach": None,
        "outcomes": None,
        "business_impact": None,
        "proposal": None,  # ← ADD THIS
        "current_section_index": 0,
        "sections_completed": [],
        "error": None
    }
    
    # Compile and run
    app = create_proposal_graph()
    final_state = app.invoke(initial_state)
    
    return final_state