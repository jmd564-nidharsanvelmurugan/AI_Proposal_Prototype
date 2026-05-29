from a_metadata_filter import get_candidate_chunks

from b_subsection_filter import subsection_filter

from b_keyword_search import keyword_search

from b_vector_search import vector_search

from c_hybrid_merger import hybrid_merge

from e_mmr_dedup import mmr_dedup


request = {

    "solution":
        "Data Advisory",

    "region":
        "US",

    "section":
        "Executive Overview",

    "subsection":
        "Business Context",

    "query":
        "Banking reporting"
}


# -----------------------------------
# STEP 1
# Metadata Filter
# -----------------------------------

child_ids = (
    get_candidate_chunks(
        request
    )
)

print(
    "\nCandidate Child IDs:\n"
)

print(
    child_ids
)

# -----------------------------------
# STEP 2
# Subsection Filter
# -----------------------------------

chunks = (
    subsection_filter(
        request["subsection"],
        child_ids
    )
)

print(
    "\nSubsection Filter Results:\n"
)

for c in chunks:

    print(
        c["chunk_id"],
        "|",
        c["subsection"]
    )

# -----------------------------------
# STEP 3
# Keyword Search
# -----------------------------------

keyword_results = (
    keyword_search(
        request["query"],
        chunks
    )
)

# -----------------------------------
# STEP 4
# Vector Search
# -----------------------------------

vector_results = (
    vector_search(
        request["query"],
        chunks
    )
)

# -----------------------------------
# STEP 5
# Display Both
# -----------------------------------

both_keyword_vector = hybrid_merge(
    keyword_results,
    vector_results
)


mmr_result = mmr_dedup(
    both_keyword_vector
)

print("\nMMR RESULTS\n")

for chunk in mmr_result:

    print(
        chunk["chunk_id"],
        "|",
        chunk["similarity"]
    )