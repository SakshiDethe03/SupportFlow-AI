import re

from app.database.queries import get_customer


def customer_agent(state):

    question = state["messages"][-1].content

    matches = re.findall(r"\b\d{4}\b", question)

    if matches:
        customer_id = matches[-1]
    else:
        customer_id = state.get("last_customer_id")

    customer = None

    if customer_id:
        customer = get_customer(customer_id)

    workflow = state["workflow"]

    if customer:
        workflow.append(
            f"👤 Customer Agent → Retrieved Customer {customer_id} from SQLite"
        )
    else:
        workflow.append("👤 Customer Agent → Customer not found")

    return {
        "customer_data": customer,
        "last_customer_id": customer_id,
        "workflow": workflow,
    }
