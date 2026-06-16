# main.py
import json
import os
from dotenv import load_dotenv
from src.graph import run_proposal_generation

load_dotenv()

def main():
    # Load questionnaire
    questionnaire_file = "data/questionnaire.json"
    
    if not os.path.exists(questionnaire_file):
        print(f"❌ Questionnaire file not found: {questionnaire_file}")
        return
    
    with open(questionnaire_file, "r", encoding="utf-8") as f:
        questionnaire = json.load(f)
    
    print("\n" + "=" * 80)
    print("🚀 STARTING PROPOSAL GENERATION PIPELINE")
    print("=" * 80)
    
    # Run the workflow
    final_state = run_proposal_generation(questionnaire)
    
    # Check for errors
    if final_state.get("error"):
        print(f"\n❌ Error occurred: {final_state['error']}")
    else:
        print("\n" + "=" * 80)
        print("✅ PROPOSAL GENERATION COMPLETE!")
        print("=" * 80)
        
        # Display proposal info
        if final_state.get("proposal"):
            proposal = final_state["proposal"]
            print(f"\n📄 Generated Proposal:")
            print(f"   - Markdown: {proposal.get('markdown_path', 'N/A')}")
            print(f"   - Word Doc: {proposal.get('word_path', 'N/A')}")
            print(f"   - Summary: x_results/proposal_summary.json")
            
            # Display sections completed
            sections = final_state.get("sections_completed", [])
            print(f"\n📋 Sections Completed: {len(sections)}/9")
            for i, section in enumerate(sections, 1):
                print(f"   {i}. {section}")
        else:
            print("\n⚠️ No proposal was assembled. Check for errors.")

if __name__ == "__main__":
    main()