from sqlalchemy.orm import Session
from app.schemas.products import ProductSchema
from app.models.products import Product
from fastapi import HTTPException, status
from app.common import constants


class ProductModelService:
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: ProductSchema):
        if product.price not in constants.ACCEPTABLE_COINS:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Please Select valid Coin e.g 200, 100, 25, 10, 5")

        db_product = Product(
            name=product.name,
            price=product.price,
            seller_id=product.seller_id
        )
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def get_product_by_id(self, id):
        product = self.db.query(Product).filter_by(
            id=id
        ).one_or_none()
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Product Not Found"
            )
        return product
