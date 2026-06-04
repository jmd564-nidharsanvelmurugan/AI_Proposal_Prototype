from sentence_transformers import SentenceTransformer, util

# Load model
model = SentenceTransformer("BAAI/bge-large-en-v1.5")

# text1 = "Business Context"
# text2 = "Introduction to Client Operations"
# text3 = "Industry Overview"
# text1 = "King "
# text2 = "drainage"
# Generate embeddings

text1= "Client Overview"
text2 = "Business Context"
embedding1 = model.encode(text1, convert_to_tensor=True)
embedding2 = model.encode(text2, convert_to_tensor=True)

# Calculate cosine similarity
similarity = util.cos_sim(embedding1, embedding2)

print(f"Text 1: {text1}")
print(f"Text 2: {text2}")
print(f"Semantic Similarity: {similarity.item():.4f}")