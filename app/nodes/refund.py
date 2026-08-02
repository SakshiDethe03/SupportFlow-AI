from app.tools import search_faq


def refund_agent(state):

    faq = search_faq("refund")

    return {"retrieved_docs": [faq]}
