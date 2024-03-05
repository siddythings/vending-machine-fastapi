from fastapi import APIRouter, Depends, status
from app.schemas.products import ProductSchema
from app.database.connection import get_db
from sqlalchemy.orm import Session
from app.services.products import create_product, get_all_products
from typing import List

product_router = APIRouter(tags=["products"])


@product_router.post("/create_product", status_code=status.HTTP_201_CREATED, response_model=ProductSchema)
def create(product: ProductSchema, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)


@product_router.get("/list/all", status_code=status.HTTP_200_OK, response_model=List[ProductSchema])
def get(db: Session = Depends(get_db)):
    return get_all_products(db)
