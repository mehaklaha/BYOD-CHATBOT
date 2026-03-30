import streamlit as st
import os
from src.document_loader import load_documents
from src.text_chunker import chunk_text
from src.embeddings import embed_texts
from src.vector_store import create_faiss_index, load_faiss_index
from src.rag_pipeline import retrieve_context, generate_answer
from config import DOCS_PATH

st.title("📄 BYOD RAG Chatbot ")

uploaded_files = st.file_uploader("Upload PDFs/TXT", accept_multiple_files=True)

if uploaded_files:
    os.makedirs(DOCS_PATH, exist_ok=True)

    for file in uploaded_files:
        with open(os.path.join(DOCS_PATH, file.name), "wb") as f:
            f.write(file.read())

    with st.spinner("Processing documents..."):
        raw_texts = load_documents(DOCS_PATH)

        all_chunks = []
        for text in raw_texts:
            all_chunks.extend(chunk_text(text))

        embeddings = embed_texts(all_chunks)
        create_faiss_index(embeddings, all_chunks)

    st.success("Documents indexed!")

if os.path.exists("embeddings/faiss_index.bin"):
    index, texts = load_faiss_index()

    query = st.text_input("Ask a question")

    if query:
        context_chunks = retrieve_context(query, index, texts)
        answer = generate_answer(query, context_chunks)

        st.subheader("Answer")
        st.write(answer)

        with st.expander("Retrieved Context"):
            for chunk in context_chunks:
                st.write(chunk[:500] + "...")
