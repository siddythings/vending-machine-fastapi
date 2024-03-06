from fastapi import FastAPI, Depends, status
from app.models.users import User
from app.models.products import Product
from app.models.deposit import Deposit
from app.models.purchase import Purchase

from app.routes.users import user_router
from app.routes.products import product_router
from app.routes.deposit import deposit_router
from app.routes.purchase import purchase_router
from app.routes.reset_deposit import reset_deposit_router
from app.schemas.users import UserSchema

app = FastAPI()

app.include_router(router=user_router, prefix="/user")
app.include_router(router=product_router, prefix="/product")
app.include_router(router=deposit_router, prefix="/deposit")
app.include_router(router=purchase_router, prefix="/buy")
app.include_router(router=reset_deposit_router, prefix="/reset")


@app.get("/")
def read_root():
    return {"Hello": "World"}
