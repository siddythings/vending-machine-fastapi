from app.schemas.products import ProductSchema
from app.services import products as product_services
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
