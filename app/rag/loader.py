import json
from pathlib import Path

from langchain_core.documents import Document

DATA_DIR = Path(__file__).parent.parent.parent / "data"


def load_faq_documents():

    with open(DATA_DIR / "faq.json", "r", encoding="utf-8") as f:
        faq = json.load(f)

    docs = []

    for item in faq:

        docs.append(
            Document(
                page_content=f"Question: {item['question']}\nAnswer: {item['answer']}",
                metadata={"source": "faq", "question": item["question"]},
            )
        )

    return docs
