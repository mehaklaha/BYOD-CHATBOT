import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader # type: ignore
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split_documents(folder_path):
    documents = []

    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)
            documents.extend(loader.load())

        elif file.endswith(".txt"):
            loader = TextLoader(path)
            documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=100
    )

    return splitter.split_documents(documents)
