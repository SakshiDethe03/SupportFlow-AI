from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from app.state import SupportState

from app.agents.supervisor import supervisor
from app.agents.router import router

from app.agents.faq_agent import faq_agent
from app.agents.order_agent import order_agent
from app.agents.customer_agent import customer_agent
from app.agents.responder import responder

builder = StateGraph(SupportState)

builder.add_node("supervisor", supervisor)

# Placeholder nodes for now
builder.add_node("faq", faq_agent)
builder.add_node("order", order_agent)
builder.add_node("customer", customer_agent)
builder.add_node("response", responder)

builder.add_edge(START, "supervisor")

builder.add_conditional_edges(
    "supervisor",
    router,
    {
        "faq": "faq",
        "order": "order",
        "customer": "customer",
    },
)

builder.add_edge("faq", "response")
builder.add_edge("order", "response")
builder.add_edge("customer", "response")

builder.add_edge("response", END)

graph = builder.compile(checkpointer=MemorySaver())
