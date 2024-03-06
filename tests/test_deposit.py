import string
import random
import pytest
import os
from fastapi import status
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def generate_random_string():
    alphanumeric_characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(
        alphanumeric_characters) for _ in range(7))
    return random_string


OWNER_USER_ID = 1
BUYER_USER_ID = 2

user1 = generate_random_string()
user2 = generate_random_string()

initial_username_buyer = user2
initial_role_buyer = "buyer"


def test_create_buyer_user(request):
    response = client.post(
        "/user/create_user",
        json={
            "username": initial_username_buyer,
            "role": initial_role_buyer
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["username"] == user2
    assert response.json()["role"] == "buyer"
    request.config.cache.set("buyer_user_id", response.json()["id"])


@pytest.mark.dependency()
def test_create_deposit(request):
    buyer_id = request.config.cache.get("buyer_user_id", None)
    response = client.post(
        "/deposit",
        json={
            "user_id": buyer_id,
            "amount": 100
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["amount"] == 100
    assert response.json()["user_id"] == buyer_id
    request.config.cache.set("user_id", response.json()["user_id"])


@pytest.mark.dependency()
def test_create_deposit_invalid_amount(request):
    buyer_id = request.config.cache.get("buyer_user_id", None)
    response = client.post(
        "/deposit",
        json={
            "user_id": buyer_id,
            "amount": 99
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.dependency(depends=["test_create_deposit"])
def test_get_deposit_detail(request):
    buyer_id = request.config.cache.get("buyer_user_id", None)
    response = client.get(f"/deposit/{buyer_id}")
    assert response.status_code == status.HTTP_200_OK
