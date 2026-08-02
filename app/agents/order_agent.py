import re

from app.database.queries import get_order


def order_agent(state):

    # Current user message
    question = state["messages"][-1].content

    # Look for an order ID in the current message
    matches = re.findall(r"\b\d{4}\b", question)

    # If no ID is mentioned, use the remembered one
    if matches:
        order_id = matches[-1]
    else:
        order_id = state.get("last_order_id")

    order = None

    if order_id:
        order = get_order(order_id)

    workflow = state["workflow"]

    if order:
        workflow.append(f"📦 Order Agent → Retrieved Order {order_id} from SQLite")
    else:
        workflow.append("📦 Order Agent → Order not found")

    return {
        "order_data": order,
        "last_order_id": order_id,
        "workflow": workflow,
    }
