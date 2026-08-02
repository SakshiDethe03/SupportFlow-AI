from app.llm import llm
from app.prompts import SUPERVISOR_PROMPT


def supervisor(state):
    question = state["messages"][-1].content

    response = llm.invoke(f"{SUPERVISOR_PROMPT}\n\nUser: {question}")

    routes = [r.strip().upper() for r in response.content.split(",") if r.strip()]

    print("\n🧠 Supervisor Agent")
    print(f"   Decision: {', '.join(routes)}")

    workflow = []

    if routes:
        workflow.append(f"🧠 Supervisor → Routed to {routes[0]} Agent")
    else:
        workflow.append("🧠 Supervisor → No suitable agent found")

    return {
        "route": routes,
        "workflow": workflow,
    }
