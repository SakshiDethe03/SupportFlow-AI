from langchain_core.messages import AIMessage

from app.llm import llm


def responder(state):

    question = state["messages"][-1].content

    context = f"""
FAQ Context:
{state.get("faq_context")}

Customer:
{state.get("customer_data")}

Order:
{state.get("order_data")}
"""

    prompt = f"""
You are an AI Customer Support Assistant.

You are an AI Customer Support Assistant.

Rules:
- If the user greets you (Hi, Hello, Hey, Good Morning, etc.), greet them back warmly.
- If the user asks who you are, introduce yourself as an AI Customer Support Assistant.
- For customer support questions, answer ONLY using the provided context.
- Never make up information.
- If the required information is not available in the context, politely say you don't know and ask the user for more details if appropriate.
- Keep responses concise and professional.

Context:

{context}

User Question:

{question}
"""

    response = llm.invoke(prompt)

    workflow = state["workflow"]

    workflow.append("💬 Response Agent → Generated final response")

    return {"messages": [AIMessage(content=response.content)], "workflow": workflow}
