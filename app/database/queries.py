from app.database.db import get_connection


def get_customer(customer_id: str):
    conn = get_connection()

    customer = conn.execute(
        "SELECT * FROM customers WHERE customer_id = ?",
        (customer_id,),
    ).fetchone()

    conn.close()

    if customer:
        return dict(customer)

    return None


def get_order(order_id: str):
    conn = get_connection()

    order = conn.execute(
        "SELECT * FROM orders WHERE order_id = ?",
        (order_id,),
    ).fetchone()

    conn.close()

    if order:
        return dict(order)

    return None
