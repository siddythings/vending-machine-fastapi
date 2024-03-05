from fastapi import APIRouter, Depends, status
from app.schemas.products import ProductSchema
from app.database.connection import get_db
from sqlalchemy.orm import Session
from app.services import products as product_services
from typing import List

product_router = APIRouter(tags=["products"])


@product_router.post("/create_product", status_code=status.HTTP_201_CREATED, response_model=ProductSchema)
def create(product: ProductSchema, db: Session = Depends(get_db)):
    return product_services.create_product(db=db, product=product)


@product_router.get("/list/all", status_code=status.HTTP_200_OK, response_model=List[ProductSchema])
def get(db: Session = Depends(get_db)):
    return product_services.get_all_products(db)


@product_router.get("/get/{id}", status_code=status.HTTP_200_OK, response_model=ProductSchema)
def get_product(id, db: Session = Depends(get_db)):
    return product_services.get_one_product(db=db, id=id)
