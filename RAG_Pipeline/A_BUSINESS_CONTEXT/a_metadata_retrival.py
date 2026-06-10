import psycopg2
import json
from typing import List, Dict, Any, Optional
from pydantic import BaseModel


# =====================================================
# Schema Definitions
# =====================================================

class ProposalProperties(BaseModel):
    business_offering: List[str]
    solution: List[str]
    region: List[str]
    project_type: List[str]
    commercial_use_case: List[str]
    technical_use_case: List[str]
    business_model: List[str]
    existing_infra: List[str]
    pe_relationship: List[str]


class ProposalMetadataSchema(BaseModel):
    document_id: str
    properties: ProposalProperties


class ScoredProposals(BaseModel):
    proposal: ProposalMetadataSchema
    score: float


# =====================================================
# Weighted Scoring Function
# =====================================================

def get_n_matching_proposals(
    user_input: Dict[str, Any], 
    proposals: List[ProposalMetadataSchema], 
    N: int = 5
) -> List[ScoredProposals]:
    """
    Find top N matching proposals based on weighted scoring.
    """
    weights = {
        "solution": 5,
        "business_offering": 4,
        "commercial_use_case": 4,
        "project_type": 3,
        "existing_infra": 2,
        "business_model": 1,
        "region": 1,
    }
 
    def calc_partial_score(user_vals: List[str], prop_vals: Optional[List[str]], weight: int) -> float:
        if not user_vals or not prop_vals:
            return 0.0
        matches = [val for val in user_vals if val in prop_vals]
        return (len(matches) / len(user_vals)) * weight
 
    scored_proposals: List[ScoredProposals] = []
 
    for proposal in proposals:
        score = 0
        props = proposal.properties
        if not props:
            continue
 
        score += calc_partial_score(user_input.get("solution", []), props.solution, weights["solution"])
        score += calc_partial_score(user_input.get("business_offering", []), props.business_offering, weights["business_offering"])
        score += calc_partial_score(user_input.get("commercial_use_case", []), props.commercial_use_case, weights["commercial_use_case"])
        score += calc_partial_score(user_input.get("project_type", []), props.project_type, weights["project_type"])
        score += calc_partial_score(user_input.get("business_model", []), props.business_model, weights["business_model"])
 
        # Exact match for radio-type inputs
        if user_input.get("existing_infra") and user_input["existing_infra"][0] in (props.existing_infra or []):
            score += weights["existing_infra"]
 
        if user_input.get("region") and user_input["region"][0] in (props.region or []):
            score += weights["region"]
 
        scored_proposals.append(ScoredProposals(
            proposal=proposal,
            score=score
        ))
 
    # Sort proposals by score descending
    scored_proposals.sort(key=lambda x: x.score, reverse=True)
 
    # Return top N (with ties)
    top_n: List[ScoredProposals] = []
    last_score = None
    for item in scored_proposals:
        if len(top_n) < N or item.score == last_score:
            top_n.append(item)
            last_score = item.score
        else:
            break
 
    return top_n


# =====================================================
# Fetch All Proposals from Database
# =====================================================

def fetch_all_proposals() -> List[ProposalMetadataSchema]:
    """
    Fetch all proposals from the database.
    """
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="proposal_retrieval",
        user="postgres",
        password="postgres"
    )
    
    cur = conn.cursor()
    
    cur.execute("""
        SELECT 
            document_id,
            business_offering,
            solution,
            region,
            project_type,
            commercial_use_case,
            technical_use_case,
            business_model,
            existing_infra,
            pe_relationship
        FROM proposals
        ORDER BY created_at DESC
    """)
    
    rows = cur.fetchall()
    
    proposals = []
    
    for row in rows:
        proposal = ProposalMetadataSchema(
            document_id=row[0],
            properties=ProposalProperties(
                business_offering=[row[1]] if row[1] else [],
                solution=[s.strip() for s in row[2].split(',')] if row[2] else [],
                region=[row[3]] if row[3] else [],
                project_type=[row[4]] if row[4] else [],
                commercial_use_case=[c.strip() for c in row[5].split(',')] if row[5] else [],
                technical_use_case=[row[6]] if row[6] else [],
                business_model=[b.strip() for b in row[7].split(',')] if row[7] else [],
                existing_infra=[row[8]] if row[8] else [],
                pe_relationship=[row[9]] if row[9] else []
            )
        )
        proposals.append(proposal)
    
    cur.close()
    conn.close()
    
    return proposals


# =====================================================
# Main Function: Get Top N Matching Proposals
# =====================================================

def get_top_matching_proposals(
    user_input: Dict[str, Any],
    top_n: int = 5
) -> List[Dict[str, Any]]:
    """
    Get top N matching proposals based on weighted scoring.
    Only returns proposal metadata, not chunks.
    
    Args:
        user_input: User's selection criteria
        top_n: Number of top matching proposals to return
    
    Returns:
        List of matching proposals with scores
    """
    
    print("\n" + "=" * 80)
    print("METADATA FILTER: Fetching Top Matching Proposals")
    print("=" * 80)
    
    # Fetch all proposals from database
    print("\n📊 Fetching all proposals from database...")
    all_proposals = fetch_all_proposals()
    print(f"✅ Found {len(all_proposals)} proposals in database")
    
    # Calculate weighted scores
    print("\n📊 Calculating weighted scores...")
    print(f"\n📋 User Input Criteria:")
    for key, value in user_input.items():
        print(f"   - {key}: {value}")
    
    top_matches = get_n_matching_proposals(user_input, all_proposals, top_n)
    
    print(f"\n✅ Top {len(top_matches)} matching proposals:")
    
    # Format results
    results = []
    for i, match in enumerate(top_matches, 1):
        proposal_info = {
            "rank": i,
            "document_id": match.proposal.document_id,
            "score": round(match.score, 2),
            "properties": match.proposal.properties.model_dump()
        }
        results.append(proposal_info)
        
        print(f"\n   {i}. Document ID: {match.proposal.document_id}")
        print(f"      Score: {match.score:.2f}")
        print(f"      Solution: {match.proposal.properties.solution}")
        print(f"      Business Offering: {match.proposal.properties.business_offering}")
        print(f"      Region: {match.proposal.properties.region}")
        print(f"      Project Type: {match.proposal.properties.project_type}")
    
    print("\n" + "=" * 80)
    print("✅ METADATA FILTER COMPLETE")
    print("=" * 80)
    
    return results


# =====================================================
# Example Usage
# =====================================================

if __name__ == "__main__":
    # Example user input
    user_input = {
        "solution": ["Data Advisory", "Exit Prep"],
        "business_offering": ["Professional Services"],
        "commercial_use_case": ["Operational Reporting"],
        "project_type": ["Design and Discovery"],
        "existing_infra": ["Yes"],
        "business_model": ["B2B"],
        "region": ["UK"]
    }
    
    # Get top 5 matching proposals
    top_proposals = get_top_matching_proposals(
        user_input=user_input,
        top_n=5
    )
    
    # Save to file
    with open("top_matching_proposals.json", "w", encoding="utf-8") as f:
        json.dump(top_proposals, f, indent=4, ensure_ascii=False)
    
    print("\n📁 Saved to: top_matching_proposals.json")