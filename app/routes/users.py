from fastapi import APIRouter, Depends, status
from app.schemas.users import User
from app.database.connection import get_db
from sqlalchemy.orm import Session
from app.services.users import create_user, get_user_by_id

user_router = APIRouter(tags=["users"])


@user_router.post("/create_user", status_code=status.HTTP_201_CREATED, response_model=User)
def create(user: User, db: Session = Depends(get_db)):
    return create_user(db, user)
