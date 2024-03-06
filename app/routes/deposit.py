from fastapi import APIRouter, Depends, status
from app.schemas.deposit import DepositSchema
from app.database.connection import get_db
from sqlalchemy.orm import Session
from app.services import deposit as deposit_services
from typing import List
from app.common import request_validator
deposit_router = APIRouter(tags=["deposit"])


@deposit_router.post("/", status_code=status.HTTP_201_CREATED, response_model=DepositSchema)
@request_validator.buyer_only
def create(deposit, db: Session = Depends(get_db)):
    return deposit_services.DepositService(db=db).deposit_money(deposit=deposit)


@deposit_router.get("/{id}", status_code=status.HTTP_200_OK, response_model=DepositSchema)
def create(id, db: Session = Depends(get_db)):
    request_validator.buyer_only_with_url_path(id, db=db)
    return deposit_services.DepositService(db=db).get_deposit(user_id=id)
