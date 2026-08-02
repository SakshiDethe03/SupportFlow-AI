from langchain_core.messages import HumanMessage

from app.graph import graph

config = {"configurable": {"thread_id": "1"}}

while True:

    query = input("\nYou: ")

    if query.lower() == "exit":
        break

    result = graph.invoke({"messages": [HumanMessage(content=query)]}, config=config)

    print("\n🔄 Workflow")

    for step in result["workflow"]:
        print(step)

    print("\n🤖 Assistant")
    print(result["messages"][-1].content)
