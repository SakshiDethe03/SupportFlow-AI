def router(state):

    routes = state["route"]

    if "ORDER" in routes:
        return "order"

    if "CUSTOMER" in routes:
        return "customer"

    return "faq"
