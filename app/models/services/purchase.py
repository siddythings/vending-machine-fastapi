from sqlalchemy.orm import Session
from app.schemas.products import ProductSchema
from app.models.products import Product


class ProductModelService:
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: ProductSchema):
        db_product = Product(
            name=product.name,
            price=product.price,
            seller_id=product.seller_id
        )
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product
