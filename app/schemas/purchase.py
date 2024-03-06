from typing import List, Optional
from pydantic import BaseModel
from app.schemas.products import ProductSchema
# Pydantic Schema for Purchase


class PurchaseSchema(BaseModel):
    user_id: int
    product_id: int
    quantity: int


class PurchaseResponse(BaseModel):
    user_id: int
    products_purchased: ProductSchema
    quantity: int
    total_spent: int
    change: List[int]
