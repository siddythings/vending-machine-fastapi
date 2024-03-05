from sqlalchemy.orm import Session
from app.schemas.deposit import DepositSchema
from app.models.deposit import Deposit


class DepositModelService:
    def __init__(self, db: Session):
        self.db = db

    def create(self, deposit: DepositSchema):
        db_deposit = Deposit(
            user_id=deposit.user_id,
            amount=deposit.amount
        )
        self.db.add(db_deposit)
        self.db.commit()
        self.db.refresh(db_deposit)
        return db_deposit

    def update(self, id, deposit: DepositSchema):
        update_query = {
            Deposit.amount: deposit.amount,
            Deposit.user_id: deposit.user_id,
        }
        self.db.query(Deposit).filter_by(id=id).update(update_query)
        self.db.commit()
        return self.db.query(Deposit).filter_by(id=id).one()

    def delete(self, id):
        self.db.query(Deposit).filter_by(id=id).delete()
        self.db.commit()

    def delete_all_deposits_by_user_id(self, user_id):
        self.db.query(Deposit).filter_by(user_id=user_id).delete()
        self.db.commit()
