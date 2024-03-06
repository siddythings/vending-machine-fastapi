from app.schemas.deposit import DepositSchema
from app.schemas.products import ProductSchema
from app.schemas.purchase import PurchaseSchema, PurchaseResponse
from app.models.services.deposit import DepositModelService
from app.models.services.product import ProductModelService
from app.models.services.purchase import PurchaseModelService
from sqlalchemy.orm import Session
from app.common import constants
from fastapi import HTTPException, status


class PurchaseService:
    def __init__(self, db: Session) -> None:
        self.deposit_model_service = DepositModelService(db=db)
        self.product_model_service = ProductModelService(db=db)
        self.purchase_model_service = PurchaseModelService(db=db)

    def purchase_product(self, purchase: PurchaseSchema):
        product = self.product_model_service.get_product_by_id(
            id=purchase.product_id)
        user_deposit_balance = DepositSchema.from_orm(
            self.user_current_deposit(purchase=purchase))

        total_cost = product.price * purchase.quantity

        if total_cost > user_deposit_balance.amount:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient funds")
        user_deposit_balance.amount -= total_cost
        purchase = self.purchase_model_service.record_purchase(
            purchase=purchase)

        self.update_deposit_amount(user_deposit_balance)

        return PurchaseResponse(
            user_id=purchase.user_id,
            total_spent=total_cost,
            products_purchased=ProductSchema.from_orm(product),
            quantity=purchase.quantity,
            change=self.return_change(user_deposit_balance.amount)
        )

    def return_change(self, balance):
        change = []
        balance -= balance % 5

        while balance > 0:
            for coin in constants.ACCEPTABLE_COINS:
                if balance % coin == 0:
                    change.append(coin)
                    balance -= coin
                    break
        return sorted(change, reverse=True)

    def user_current_deposit(self, purchase: PurchaseSchema):
        return self.deposit_model_service.get(
            user_id=purchase.user_id)

    def update_deposit_amount(self, deposit: DepositSchema):
        return self.deposit_model_service.create_or_update(deposit=deposit)
