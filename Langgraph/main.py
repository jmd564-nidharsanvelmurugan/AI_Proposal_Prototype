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
        print("Please create data/questionnaire.json with your questionnaire data")
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
        
        # Display generated business context
        if final_state.get("business_context"):
            print("\n📄 Generated Business Context:")
            print("-" * 40)
            print(final_state["business_context"]["content"])
            print("-" * 40)
        
        print(f"\n📁 Check x_results/ folder for outputs")

if __name__ == "__main__":
    main()