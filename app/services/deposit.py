from app.models.deposit import Deposit
from app.schemas.deposit import DepositSchema
from app.models.services.deposit import DepositModelService
from sqlalchemy.orm import Session
from app.common import constants
from fastapi import HTTPException, status


class DepositService:
    def __init__(self, db: Session) -> None:
        self.deposit_model = DepositModelService(db=db)

    def deposit_money(self, deposit: DepositSchema):
        if deposit.amount not in constants.ACCEPTABLE_COINS:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Please Select valid Coin e.g 200, 100, 25, 10, 5")

        return self.deposit_model.create_or_update(deposit=deposit)

    def reset_deposit(self, user_id):
        self.deposit_model.reset_deposit(user_id=user_id)

    def get_deposit(self, user_id):
        depost = self.deposit_model.get(user_id=user_id)
        if not depost:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Deposit Not Found Please add first!!"
            )
        return depost
