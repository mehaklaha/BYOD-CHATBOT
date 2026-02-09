import numpy as np
import openai
from config import OPENAI_API_KEY
from sentence_transformers import SentenceTransformer

client = openai.OpenAI(api_key=OPENAI_API_KEY)
model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_context(query, index, texts, k=3):
    query_vec = model.encode([query])
    distances, indices = index.search(np.array(query_vec), k)
    return [texts[i] for i in indices[0]]

def generate_answer(query, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""
    Answer the question using ONLY the context below.

    Context:
    {context}

    Question:
    {query}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content
