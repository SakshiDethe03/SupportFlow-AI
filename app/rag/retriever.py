from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

CHROMA_DB_PATH = Path(__file__).parent.parent.parent / "chroma_db"

# load the same embedding model used during ingestion
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Connect to the existing Chroma database
vector_store = Chroma(
    persist_directory=str(CHROMA_DB_PATH),
    embedding_function=embeddings,
)

# Create a retriever
# k=3 → Return the best 3 documents.
# fetch_k=10 → Look at the top 10 candidates first.
# lambda_mult=0.7 → Balance relevance and diversity.
retriever = vector_store.as_retriever(
    search_type="mmr", search_kwargs={"k": 3, "fetch_k": 10, "lambda_mult": 0.7}
)
