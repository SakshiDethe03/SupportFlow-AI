import os
from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from app.tools import (
    search_faq,
    get_customer,
    lookup_order,
    create_ticket,
)

tools = [search_faq, get_customer, lookup_order, create_ticket]

tools = tools

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
).bind_tools(tools)
