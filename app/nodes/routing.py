def route_intent(state):

    intent = state["intent"]

    if "refund" in intent:
        return "refund"

    if "billing" in intent:
        return "billing"

    if "technical" in intent:
        return "technical"

    return "general"
