from fastapi import APIRouter, Depends, status
from app.schemas.users import UserSchema
from app.database.connection import get_db
from sqlalchemy.orm import Session
from app.services import users as user_services
from typing import List

user_router = APIRouter(tags=["users"])


@user_router.post("/create_user", status_code=status.HTTP_201_CREATED, response_model=UserSchema)
def create(user: UserSchema, db: Session = Depends(get_db)):
    return user_services.create_user(db, user)


@user_router.get("/{id}", status_code=status.HTTP_200_OK, response_model=UserSchema)
def get(id, db: Session = Depends(get_db)):
    return user_services.get_user_by_id(db, id)


@user_router.get("/list/all", status_code=status.HTTP_200_OK, response_model=List[UserSchema])
def get_all_user(db: Session = Depends(get_db)):
    return user_services.get_all_users(db=db)


@user_router.patch("/update/{id}", status_code=status.HTTP_200_OK, response_model=UserSchema)
def update_product(id, user: UserSchema, db: Session = Depends(get_db)):
    return user_services.user_update(id=id, user=user, db=db)
