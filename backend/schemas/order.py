from typing import Optional

from pydantic import BaseModel


class OrderInfo(BaseModel):
    startpoint: str
    endpoint: str
    wagon_type: Optional[str] = None
    ticket_count: int
    departure_dates: list[str]


class OrderStatus(BaseModel):
    status: str
    order_id: int
