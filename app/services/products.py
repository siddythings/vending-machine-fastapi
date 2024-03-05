from app.models.products import Product
from app.schemas.products import ProductSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def create_product(db: Session, product: ProductSchema):
    db_product = Product(
        name=product.name,
        price=product.price,
        seller_id=product.seller_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_all_products(db: Session):
    return db.query(Product).all()
