from app.rag.retriever import retriever


def faq_agent(state):
    question = state["messages"][-1].content

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    workflow = state["workflow"]

    workflow.append(
        f"📚 FAQ Agent → Retrieved {len(docs)} FAQ document(s) from ChromaDB"
    )

    return {"faq_context": context, "workflow": workflow}
