import string
import random
import pytest
import os
from fastapi import status
from fastapi.testclient import TestClient
from app.main import app
from app.common import constants
client = TestClient(app)


def generate_random_string():
    alphanumeric_characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(
        alphanumeric_characters) for _ in range(7))
    return random_string


OWNER_USER_ID = 2
BUYER_USER_ID = 3  # Depost 100
PRODUCT_ID_1 = 1  # Price 5
PRODUCT_ID_2 = 2  # Price 200
QUANTITY = 1


@pytest.mark.dependency()
def test_create_deposit(request):
    response = client.post(
        "/deposit",
        json={
            "user_id": BUYER_USER_ID,
            "amount": 100
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["amount"] == 100
    assert response.json()["user_id"] == BUYER_USER_ID
    request.config.cache.set("user_id", response.json()["user_id"])


def test_create_purchase(request):
    response = client.post(
        "/buy",
        json={
            "user_id": BUYER_USER_ID,
            "product_id": PRODUCT_ID_1,
            "quantity": QUANTITY
        },
    )
    print(response, "--------")
    assert response.status_code == status.HTTP_200_OK

    # Product ID check
    assert response.json()["products_purchased"]["id"] == PRODUCT_ID_1

    # Product Amount
    assert response.json()["quantity"] == QUANTITY

    # Purchase Total Spand
    assert response.json()["total_spent"] == response.json()[
        "products_purchased"]["price"] * QUANTITY

    # Buyer ID
    assert response.json()["user_id"] == BUYER_USER_ID

    assert all(value in constants.ACCEPTABLE_COINS
               for value in response.json()["change"])

    request.config.cache.set("user_id", response.json()["user_id"])


def test_insufficient_funds(request):
    response = client.post(
        "/buy",
        json={
            "user_id": BUYER_USER_ID,
            "product_id": PRODUCT_ID_2,
            "quantity": 1
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == "Insufficient funds"


def test_rest_buyer_account(request):
    response = client.post(
        "/reset",
        json={
            "user_id": BUYER_USER_ID,
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["details"] == "Reset Deposit"
