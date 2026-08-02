from app.llm import llm
from app.prompts import INTENT_PROMPT
from app.tools import search_faq


def classify_intent(state):

    query = state["messages"][-1].content

    prompt = INTENT_PROMPT.format(query=query)

    response = llm.invoke(prompt)

    return {"intent": response.content.strip().lower()}
