from typing import Annotated, Optional
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages


class SupportState(TypedDict):
    messages: Annotated[list, add_messages]

    route: Optional[list[str]]

    faq_context: Optional[str]

    customer_data: Optional[dict]

    order_data: Optional[dict]

    workflow: list[str]

    last_order_id: Optional[str]

    last_customer_id: Optional[str]
