from typing import List, Optional
from pydantic import BaseModel


# Pydantic Schema for Product
class ProductSchema(BaseModel):
    id: Optional[int] = None
    name: str
    price: int
    seller_id: int

    class Config:
        orm_mode = True
        from_attributes = True
