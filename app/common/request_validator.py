from app.schemas.products import ProductSchema
from app.schemas.deposit import DepositSchema
from app.schemas.purchase import PurchaseSchema
from app.services import products as product_services
from app.services import users as user_services
from sqlalchemy.orm import Session
from app.database.connection import get_db
from fastapi import HTTPException, status, Depends


def owner_only(func):
    def wrapper(id, product: ProductSchema, db: Session = Depends(get_db)):
        existing_product = product_services.get_one_product(id=id, db=db)

        if existing_product.seller_id != product.seller_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Sorry!! Owner only can perform this action")

        return func(id=id, product=product, db=db)

    return wrapper


def buyer_only(func):
    def wrapper(deposit: DepositSchema, db: Session = Depends(get_db)):
        user_details = user_services.get_user_by_id(id=deposit.user_id, db=db)

        if user_details.role != "buyer":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Sorry!! Buyer only can perform this action")

        return func(deposit=deposit, db=db)

    return wrapper


def buyer_only_purchase(func):
    def wrapper(purchase: PurchaseSchema, db: Session = Depends(get_db)):
        user_details = user_services.get_user_by_id(id=purchase.user_id, db=db)

        if user_details.role != "buyer":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Sorry!! Buyer only can perform this action")

        return func(purchase=purchase, db=db)

    return wrapper
