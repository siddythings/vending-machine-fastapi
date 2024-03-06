from sqlalchemy.orm import Session
from app.schemas.deposit import DepositSchema
from app.models.deposit import Deposit
from sqlalchemy import func
from fastapi import HTTPException, status


class DepositModelService:
    def __init__(self, db: Session):
        self.db = db

    def get(self, user_id):
        depost = self.db.query(Deposit).filter_by(
            user_id=user_id).one_or_none()
        if not depost:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Deposit Not Found Please add first!!"
            )
        return depost

    def create(self, deposit: DepositSchema):
        db_deposit = Deposit(
            user_id=deposit.user_id,
            amount=deposit.amount
        )
        self.db.add(db_deposit)
        self.db.commit()
        self.db.refresh(db_deposit)
        return db_deposit

    def update(self, deposit: DepositSchema):
        update_query = {
            Deposit.amount: deposit.amount
        }
        self.db.query(Deposit).filter_by(
            user_id=deposit.user_id).update(update_query)
        self.db.commit()
        return self.db.query(Deposit).filter_by(user_id=deposit.user_id).one()

    def delete(self, id):
        self.db.query(Deposit).filter_by(id=id).delete()
        self.db.commit()

    def delete_all_deposits_by_user_id(self, user_id):
        self.db.query(Deposit).filter_by(user_id=user_id).delete()
        self.db.commit()

    def get_user_current_deposit(self, user_id):
        total_amount = self.db.query(
            func.sum(Deposit.amount)).filter_by(user_id=user_id).scalar()
        return total_amount or 0

    def create_or_update(self, deposit):
        current_deposit = self.get(user_id=deposit.user_id)
        if current_deposit:
            return self.update(deposit=deposit)
        return self.create(deposit=deposit)
