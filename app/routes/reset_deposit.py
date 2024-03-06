from fastapi import APIRouter, Depends, status
from app.schemas.purchase import PurchaseSchema, PurchaseResponse
from app.schemas.deposit import ResetDeposit
from app.database.connection import get_db
from sqlalchemy.orm import Session
from app.services import deposit as deposit_service
from typing import List
from app.common import request_validator

reset_deposit_router = APIRouter(tags=["reset"])


@reset_deposit_router.post("/", status_code=status.HTTP_200_OK, response_model=ResetDeposit)
@request_validator.buyer_only
def reset(deposit, db: Session = Depends(get_db)):
    deposit_service.DepositService(
        db=db).reset_deposit(user_id=deposit.user_id)
    return ResetDeposit(user_id=id, details="Reset Deposit")
