from app.llm import llm


def agent(state):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}
