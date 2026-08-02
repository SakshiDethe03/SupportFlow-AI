import sys
from pathlib import Path

if sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")


from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag.loader import load_faq_documents

# Store the vector database in the project root
CHROMA_DB_PATH = Path(__file__).parent.parent.parent / "chroma_db"


import shutil

def ingest_documents():

    # Clean existing vector DB directory if present
    if CHROMA_DB_PATH.exists():
        shutil.rmtree(CHROMA_DB_PATH)

    # Load FAQ Documents
    documents = load_faq_documents()


    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)

    chunks = splitter.split_documents(documents)

    # use embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create Chroma DB
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DB_PATH),
    )

    print(f"✅ Indexed {len(chunks)} chunks into Chroma DB.")


if __name__ == "__main__":
    ingest_documents()
