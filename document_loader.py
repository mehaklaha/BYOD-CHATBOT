import os
import fitz  # PyMuPDF

def load_documents(folder_path):
    texts = []

    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)

        if file.endswith(".pdf"):
            doc = fitz.open(path)
            text = ""
            for page in doc:
                text += page.get_text()
            texts.append(text)

        elif file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                texts.append(f.read())

    return texts
