# BYOD RAG AI Chatbot 

A Bring Your Own Document (BYOD) Retrieval-Augmented Generation (RAG) chatbot built using Python, FAISS, Sentence Transformers, and Streamlit.

This application allows users to upload their own documents (PDF/TXT) and ask questions. The system retrieves relevant context from the uploaded documents and generates accurate answers using a language model.

---

## Features

* Upload and process PDF and TXT documents
* Semantic search using vector embeddings
* Context-aware responses using RAG
* Fast similarity search with FAISS
* Interactive web interface using Streamlit
* Lightweight implementation without LangChain

---

 How It Works

1. Document Upload
   Users upload PDF or TXT files.

2. Text Extraction and Chunking
   Documents are split into smaller chunks for efficient retrieval.

3. Embedding Generation
   Each chunk is converted into vector representations using Sentence Transformers.

4. Vector Storage
   Embeddings are stored in a FAISS index for fast similarity search.

5. Query Processing
   The user submits a question, and the system retrieves the most relevant chunks.

6. Answer Generation
   The language model generates a response based only on the retrieved context.

---

 Project Structure

```
byod-rag-no-langchain/
│
├── app.py
├── config.py
├── requirements.txt
│
├── data/
│   └── documents/
│
├── embeddings/
│   ├── faiss_index.bin
│   └── text_chunks.pkl
│
└── src/
    ├── document_loader.py
    ├── text_chunker.py
    ├── embeddings.py
    ├── vector_store.py
    └── rag_pipeline.py
```

---

Installation

### 1. Clone the repository

```bash
git clone https://github.com/mehaklaha/byod-chatbot.git
cd byod-chatbot
```

2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

---
 Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_api_key_here
```

---
 Run the Application

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

 Deployment (Streamlit Cloud)

1. Push the project to GitHub
2. Open Streamlit Cloud
3. Deploy your repository
4. Add the OPENAI_API_KEY in Secrets
5. Launch the application

---

 Tech Stack

* Python
* Streamlit
* FAISS
* Sentence Transformers
* OpenAI API
* PyMuPDF

---

 Use Cases

* Academic research assistant
* Document-based question answering system
* Knowledge base chatbot
* Personal document assistant

---

 Limitations

* Requires an OpenAI API key
* Performance depends on chunking and retrieval quality
* Not optimized for very large datasets

---

 Future Improvements

* Add conversational memory
* Support additional file formats such as DOCX and CSV
* Integrate offline language models
* Improve user interface and experience
* Add source citation highlighting



