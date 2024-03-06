from typing import List, Optional
from pydantic import BaseModel


# Pydantic Schema for Deposit
class DepositSchema(BaseModel):
    id: Optional[int] = None
    user_id: int
    amount: int

    class Config:
        orm_mode = True
        from_attributes = True
