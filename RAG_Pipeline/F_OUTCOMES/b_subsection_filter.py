import psycopg2
import re
import os
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict, Any, Optional


# =====================================================
# Initialize Embedding Model
# =====================================================

model = SentenceTransformer("BAAI/bge-large-en-v1.5")


# =====================================================
# Helper Functions
# =====================================================

def ensure_results_folder():
    """Ensure the x_results folder exists."""
    if not os.path.exists("x_results"):
        os.makedirs("x_results")
        print("📁 Created 'x_results' folder")


def save_to_json(data: Dict[str, Any], filename: str):
    """Save data to JSON file in x_results folder."""
    ensure_results_folder()
    filepath = os.path.join("x_results", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"✅ Saved to: {filepath}")


# =====================================================
# Semantic Query Filter (No Subsections)
# =====================================================

def get_filtered_chunks_by_semantic_query(
    child_ids: List[str],
    query: str,
    top_k: int = 10
) -> Dict[str, List[Dict[str, Any]]]:
    """
    Filter child chunks using a semantic query (no subsection names).
    Returns chunks with similarity scores based on full text content.
    """
    
    if not child_ids:
        print("⚠️ No child IDs provided. Returning empty list.")
        return {"semantic_filtered": []}
    
    if not query or query.strip() == "":
        print("⚠️ No query provided. Returning empty list.")
        return {"semantic_filtered": []}
    
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            dbname="proposal_retrieval",
            user="postgres",
            password="postgres"
        )
        
        cur = conn.cursor()
        
        # Fetch all child chunks by IDs
        cur.execute("""
            SELECT
                id,
                subsection,
                actual_text_data,
                embedding
            FROM child_chunks
            WHERE id = ANY(%s)
        """, (child_ids,))
        
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Database error: {e}")
        return {"semantic_filtered": []}
    
    if not rows:
        print("⚠️ No child chunks found for the given IDs.")
        return {"semantic_filtered": []}
    
    print(f"📝 Applying semantic query filter: '{query}'")
    
    try:
        # Generate query embedding
        query_emb = model.encode(query)
    except Exception as e:
        print(f"❌ Error encoding query: {e}")
        return {"semantic_filtered": []}
    
    results = []
    
    for row in rows:
        chunk_text = row[2] if row[2] else ""
        subsection_name = row[1] if row[1] else "unknown"
        
        if not chunk_text:
            continue
        
        try:
            chunk_emb = model.encode(chunk_text)
            
            similarity = cosine_similarity(
                [query_emb],
                [chunk_emb]
            )[0][0]
            
            results.append({
                "chunk_id": row[0],
                "subsection": subsection_name,
                "text": chunk_text,
                "similarity_score": float(similarity),
                "match_type": "semantic_query"
            })
        except Exception as e:
            print(f"⚠️ Error processing chunk {row[0]}: {e}")
            continue
    
    results.sort(key=lambda x: x["similarity_score"], reverse=True)
    top_results = results[:top_k]
    
    print(f"✅ Found {len(results)} matching chunks (returning top {len(top_results)})")
    for i, r in enumerate(top_results[:3], 1):
        print(f"   {i}. Score: {r['similarity_score']:.3f} | Subsection: {r['subsection']}")
    
    return {"semantic_filtered": top_results}


# =====================================================
# Subsection Filter (With Subsections)
# =====================================================

def subsection_filter(
    subsection_query: Optional[str],
    child_ids: List[str],
    search_type: int = 1,
    top_k: int = 10
) -> List[Dict[str, Any]]:
    """
    Filter child chunks based on subsection query.
    
    Args:
        subsection_query: The subsection name/query to search for
        child_ids: List of child chunk IDs
        search_type: 1 = Semantic, 2 = Keyword
        top_k: Number of top results to return
    """
    
    if not child_ids:
        print("⚠️ No child IDs provided. Returning empty list.")
        return []
    
    try:
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
                id,
                subsection,
                actual_text_data,
                embedding
            FROM child_chunks
            WHERE id = ANY(%s)
        """, (child_ids,))
        
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Database error: {e}")
        return []
    
    if not rows:
        print("⚠️ No child chunks found for the given IDs.")
        return []
    
    # =====================================================
    # CASE 1: No subsection query - return all chunks as-is
    # =====================================================
    if not subsection_query or subsection_query.strip() == "":
        print(f"📝 No subsection filter applied. Returning all {len(rows)} child chunks.")
        
        results = []
        for row in rows:
            results.append({
                "chunk_id": row[0],
                "subsection": row[1] if row[1] else "unknown",
                "text": row[2],
                "subsection_score": 1.0,
                "match_type": "all_chunks"
            })
        
        return results[:top_k]
    
    # =====================================================
    # CASE 2: Subsection query present - apply filtering
    # =====================================================
    print(f"📝 Applying subsection filter: '{subsection_query}' (type={'semantic' if search_type == 1 else 'keyword'})")
    
    results = []
    
    # ==========================
    # SEMANTIC SEARCH
    # ==========================
    if search_type == 1:
        try:
            query_emb = model.encode(subsection_query)
        except Exception as e:
            print(f"❌ Error encoding query: {e}")
            return []
        
        for row in rows:
            subsection_name = row[1] if row[1] else ""
            
            if not subsection_name:
                continue
            
            try:
                subsection_emb = model.encode(subsection_name)
                
                similarity = cosine_similarity(
                    [query_emb],
                    [subsection_emb]
                )[0][0]
                
                results.append({
                    "chunk_id": row[0],
                    "subsection": subsection_name,
                    "text": row[2],
                    "subsection_score": float(similarity),
                    "match_type": "semantic"
                })
            except Exception as e:
                print(f"⚠️ Error processing chunk {row[0]}: {e}")
                continue
        
        results.sort(key=lambda x: x["subsection_score"], reverse=True)
    
    # ==========================
    # KEYWORD SEARCH
    # ==========================
    elif search_type == 2:
        query_tokens = set(
            re.findall(r"\w+", subsection_query.lower())
        )
        
        for row in rows:
            subsection_name = row[1] if row[1] else ""
            
            if not subsection_name:
                continue
            
            subsection_tokens = set(
                re.findall(r"\w+", subsection_name.lower())
            )
            
            matched_words = query_tokens.intersection(subsection_tokens)
            match_count = len(matched_words)
            
            if match_count > 0:
                results.append({
                    "chunk_id": row[0],
                    "subsection": subsection_name,
                    "text": row[2],
                    "subsection_score": match_count,
                    "matched_words": sorted(list(matched_words)),
                    "match_type": "keyword"
                })
        
        results.sort(key=lambda x: x["subsection_score"], reverse=True)
    
    print(f"✅ Found {len(results)} matching chunks (returning top {min(top_k, len(results))})")
    return results[:top_k]


# =====================================================
# Get Filtered Chunks for Section
# =====================================================

def get_filtered_chunks_for_section(
    child_ids: List[str],
    subsections: List[Dict[str, str]],
    search_type: int = 1,
    top_k_per_subsection: int = 5
) -> Dict[str, List[Dict[str, Any]]]:
    """
    Get filtered chunks for each subsection in a section.
    
    Args:
        child_ids: List of child chunk IDs
        subsections: List of subsections with names and queries
        search_type: 1 -> Semantic, 2 -> Keyword
        top_k_per_subsection: Number of chunks to return per subsection
    
    Returns:
        Dictionary mapping subsection name to list of filtered chunks
    """
    
    results = {}
    
    if not subsections:
        print("⚠️ No subsections provided. Fetching all chunks without filter...")
        all_chunks = subsection_filter(
            subsection_query=None,
            child_ids=child_ids,
            search_type=search_type,
            top_k=top_k_per_subsection * 10
        )
        results["all_chunks"] = all_chunks
        return results
    
    for subsection in subsections:
        subsection_name = subsection.get("subsection", "")
        query = subsection.get("query", subsection_name)
        
        print(f"\n🔍 Filtering for subsection: {subsection_name}")
        
        filtered_chunks = subsection_filter(
            subsection_query=query,
            child_ids=child_ids,
            search_type=search_type,
            top_k=top_k_per_subsection
        )
        
        results[subsection_name] = filtered_chunks
    
    return results


if __name__ == "__main__":
    print("Testing b_subsection_filter.py")
    print("Module loaded successfully. Ready to use.")