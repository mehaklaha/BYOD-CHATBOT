import faiss
import numpy as np
import pickle
import os
from config import FAISS_INDEX_PATH

def create_faiss_index(embeddings, texts):
    os.makedirs("embeddings", exist_ok=True)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    faiss.write_index(index, FAISS_INDEX_PATH)

    with open("embeddings/text_chunks.pkl", "wb") as f:
        pickle.dump(texts, f)

def load_faiss_index():
    index = faiss.read_index(FAISS_INDEX_PATH)
    with open("embeddings/text_chunks.pkl", "rb") as f:
        texts = pickle.load(f)
    return index, texts
