from app.tools import search_faq


def billing_agent(state):
    query = state["messages"][-1].content

    faq = search_faq(query)

    return {"retrieved_docs": [faq]}
