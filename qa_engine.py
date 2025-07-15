import os
import google.generativeai as genai
from sentence_transformers import SentenceTransformer, util

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Chunking function
def chunk_text(text, chunk_size=500):
    words = text.split()
    return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

# Get top k relevant chunks using cosine similarity
def get_top_k_chunks(text, query, k=3):
    chunks = chunk_text(text)
    chunk_embeddings = embedding_model.encode(chunks, convert_to_tensor=True)
    query_embedding = embedding_model.encode(query, convert_to_tensor=True)

    cosine_scores = util.pytorch_cos_sim(query_embedding, chunk_embeddings)[0]
    top_indices = cosine_scores.argsort(descending=True)[:k]
    
    top_chunks = [chunks[i] for i in top_indices]
    return top_chunks

# Ask Gemini using top chunks as context
def get_answer_from_gemini(chunks, question):
    context = "\n\n".join(chunks)
    prompt = f"""You are a helpful assistant. Use the context below to answer the user's question.

Context:
{context}

Question:
{question}

Answer:"""
    response = model.generate_content(prompt)
    return response.text.strip()
