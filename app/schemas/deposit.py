from typing import List, Optional
from pydantic import BaseModel


# Pydantic Schema for Deposit
class DepositSchema(BaseModel):
    id: Optional[int] = None
    user_id: int
    amount: Optional[int] = 0

    class Config:
        orm_mode = True
        from_attributes = True
        model_validate = True


class ResetDeposit(BaseModel):
    user_id: int
    details: str
