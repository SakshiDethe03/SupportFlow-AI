import streamlit as st
from langchain_core.messages import HumanMessage

from app.graph import graph

# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title="SupportFlow AI",
    page_icon="🤖",
    layout="wide",
)

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.title("🤖 SupportFlow AI")

    st.info(
        """
### 🚀 Project

A Multi-Agent Customer Support System powered by LangGraph.

It intelligently routes user queries to specialized agents.
"""
    )

    st.markdown("### 🛠 Tech Stack")

    st.success("✓ LangGraph")
    st.success("✓ LangChain")
    st.success("✓ ChromaDB (RAG)")
    st.success("✓ SQLite")
    st.success("✓ Streamlit")

    with st.expander("🏗 System Architecture"):
        st.image("assets/architecture-diagram.png", use_container_width=True)

    st.markdown("### 💡 Sample Questions")

    st.code(
        """
How long does a refund take?

Where is order 5002?

Customer ID is 1001

What is my current plan?

What is its status?
"""
    )

    st.markdown("---")

    if st.button("🗑 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.workflow = []
        st.rerun()

# ---------------- Header ---------------- #

st.title("🤖 SupportFlow AI")
st.caption("Multi-Agent Customer Support System powered by LangGraph")

col1, col2, col3 = st.columns(3)

col1.metric("Specialized Agents", "3")
col2.metric("Knowledge Base", "ChromaDB")
col3.metric("Database", "SQLite")

# ---------------- Session State ---------------- #

config = {"configurable": {"thread_id": "streamlit"}}

if "messages" not in st.session_state:
    st.session_state.messages = []

if "workflow" not in st.session_state:
    st.session_state.workflow = []

# ---------------- Chat ---------------- #

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask a customer support question..."):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    result = graph.invoke(
        {"messages": [HumanMessage(content=prompt)]},
        config=config,
    )

    answer = result["messages"][-1].content

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    st.session_state.workflow = result.get("workflow", [])

    with st.chat_message("assistant"):
        st.markdown(answer)

# ---------------- Workflow ---------------- #

if st.session_state.workflow:

    st.success(f"🤖 Active Workflow: {st.session_state.workflow[0]}")

    with st.expander("🔄 View Agent Workflow", expanded=False):

        for step in st.session_state.workflow:
            st.write(step)

# ---------------- Footer ---------------- #

st.divider()

st.caption("Built with ❤️ using LangGraph • LangChain • ChromaDB • SQLite • Streamlit")
