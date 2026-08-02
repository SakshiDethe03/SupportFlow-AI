from enum import Enum


class Route(str, Enum):
    FAQ = "FAQ"
    ORDER_STATUS = "ORDER_STATUS"
    CUSTOMER_PROFILE = "CUSTOMER_PROFILE"
    BILLING = "BILLING"
    ESCALATION = "ESCALATION"
