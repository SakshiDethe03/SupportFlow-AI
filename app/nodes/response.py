from app.llm import llm


def generate_response(state):

    question = state["messages"][-1].content

    context = state["retrieved_docs"]

    prompt = f"""
    Answer the customer's question.
    
    Question:
    {question}
    
    Context:
    {context}
    
    Give a professional support response.
    """

    answer = llm.invoke(prompt)

    return {"final_response": answer.content}
