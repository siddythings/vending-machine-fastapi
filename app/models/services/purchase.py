from sqlalchemy.orm import Session
from app.schemas.purchase import PurchaseSchema
from app.models.purchase import Purchase
from fastapi import HTTPException, status


class PurchaseModelService:
    def __init__(self, db: Session):
        self.db = db

    def record_purchase(self, purchase: PurchaseSchema):
        db_purchase = Purchase(
            user_id=purchase.user_id,
            product_id=purchase.product_id,
            quantity=purchase.quantity
        )
        self.db.add(db_purchase)
        self.db.commit()
        self.db.refresh(db_purchase)
        return db_purchase
