from app.llm import llm
from app.prompts import SUPERVISOR_PROMPT


def supervisor(state):
    messages = state["messages"]

    history = "\n".join(
        [
            f"{'User' if m.type == 'human' else 'Assistant'}: {m.content}"
            for m in messages[-6:]  # Last 6 messages
        ]
    )

    response = llm.invoke(
        f"""
{SUPERVISOR_PROMPT}

Conversation:
{history}

Decide which agent(s) should handle the latest user request.
Return ONLY agent names separated by commas.
"""
    )

    routes = [r.strip().upper() for r in response.content.split(",") if r.strip()]

    print("\n🧠 Supervisor Agent")
    print("Conversation:")
    print(history)
    print(f"Decision: {routes}")

    workflow = []

    if routes:
        workflow.append(f"🧠 Supervisor → Routed to {routes[0]} Agent")
    else:
        workflow.append("🧠 Supervisor → No suitable agent found")

    return {
        "route": routes,
        "workflow": workflow,
    }
