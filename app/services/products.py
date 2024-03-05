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


def get_one_product(id, db: Session):
    product = db.query(Product).filter_by(
        id=id
    ).one_or_none()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product Not Found"
        )
    return product
