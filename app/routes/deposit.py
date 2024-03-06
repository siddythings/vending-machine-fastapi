from fastapi import APIRouter, Depends, status
from app.schemas.deposit import DepositSchema
from app.database.connection import get_db
from sqlalchemy.orm import Session
from app.services import deposit as deposit_services
from typing import List
from app.common import request_validator
deposit_router = APIRouter(tags=["deposit"])


@deposit_router.post("/", status_code=status.HTTP_200_OK, response_model=DepositSchema)
@request_validator.buyer_only
def create(deposit, db: Session = Depends(get_db)):
    return deposit_services.DepositService(db=db).deposit_money(deposit=deposit)
