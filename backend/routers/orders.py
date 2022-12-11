from fastapi import APIRouter
from pydantic import BaseModel
from enum import Enum


router = APIRouter(
    tags=["orders"],
    prefix="/api/v1/orders"
)


class Status(str, Enum):
    ORDERED = "ORDERED"
    PAID = "PAID"
    SENT = "SENT"
    IN_TRANSIT = "IN TRANSIT"
    DELIVERED = "DELIVERED"


class Dimensions(BaseModel):
    height: int
    length: int
    width: int
    weight: int


class Size(str, Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
    CUSTOM = "CUSTOM"


class Payment(str, Enum):
    PRZELEWY24 = "PRZELEWY24"
    CASH = "CASH"
    PAYPAL = "PAYPAL"


class Order(BaseModel):
     size: Size = None
     delivery_place: str
     package_value: float
     payment_method: Payment = None
     dimensions: Dimensions = None


@router.get("/")
async def read_orders():
    return []


@router.get("/{order_id}")
async def read_order_by_id(order_id: int):
    return {"order_id": order_id}


@router.post("/")
async def create_order(order: Order):
    return {
        "order_id": "",
        "planned_delivery": "",
        "package_status": ""
    }


@router.patch("/{id}/status")
async def update_order_status_by_id(order_id: int, status: Status):
    return {
        "order_id": order_id,
        "status": status
    }


@router.patch("/{id}/destination")
async def update_order_destination_by_id(order_id: int, destination: str):
    return {
        "order_id": order_id,
        "destination": destination
    }
