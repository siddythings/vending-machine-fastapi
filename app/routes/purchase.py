from fastapi import APIRouter, Depends, status
from app.schemas.purchase import PurchaseSchema, PurchaseResponse
from app.database.connection import get_db
from sqlalchemy.orm import Session
from app.services import purchase as purchase_services
from typing import List
from app.common import request_validator

purchase_router = APIRouter(tags=["buy"])


@purchase_router.post("/", status_code=status.HTTP_200_OK, response_model=PurchaseResponse)
@request_validator.buyer_only_purchase
def create(purchase, db: Session = Depends(get_db)):
    return purchase_services.PurchaseService(db=db).purchase_product(purchase=purchase)
