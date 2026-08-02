from langsmith.evaluation._runner import DATA_T
import json
from pathlib import Path
from langchain_core.tools import tool
from app.rag.retriever import retriever

DATA_DIR = Path(__file__).parent.parent / "data"


def load_json(filename):
    with open(DATA_DIR / filename) as f:
        return json.load(f)


customers = load_json("customers.json")
orders = load_json("orders.json")
faq = load_json("faq.json")


@tool
def get_customer(customer_id: str):
    """The agent should use this tool to get customer information by customer ID."""
    for customer in customers:
        if customer["customer_id"] == customer_id:
            return customer

    return {"error": "Customer not found"}


@tool
def lookup_order(order_id: str):
    """The agent should use this tool to look up an order by order ID."""
    for order in orders:
        if order["order_id"] == order_id:
            return order

    return {"error": "Order not found"}


@tool
def search_faq(query: str) -> str:
    """
    Search the company FAQ knowledge base.
    """

    docs = retriever.invoke(query)

    if not docs:
        return "No relevant documents found"

    results = []

    for i, doc in enumerate(docs, start=1):
        results.append(
            f"""
            Result {i}
            {doc.page_content}
            """
        )

        return f"\n".join(results)


@tool
def create_ticket(issue: str):
    """Create a support ticket for the customer."""
    return {"ticket_id": "TICKET-1001", "status": "Created", "issue": issue}
