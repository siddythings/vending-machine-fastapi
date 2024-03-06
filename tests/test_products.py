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


product1 = generate_random_string()
product2 = generate_random_string()


def test_create_product(request):
    response = client.post(
        "/product/create_product",
        json={
            "name": product1,
            "price": 5,
            "seller_id": 1
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["name"] == product1
    assert response.json()["price"] == 5
    assert response.json()["seller_id"] == 1
    request.config.cache.set("product_id", response.json()["id"])


def test_create_product2(request):
    response = client.post(
        "/product/create_product",
        json={
            "name": product1,
            "price": 25,
            "seller_id": 1
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["name"] == product1
    assert response.json()["price"] == 25
    assert response.json()["seller_id"] == 1
    request.config.cache.set("product_id", response.json()["id"])


def test_create_product_with_invalid_amount(request):
    response = client.post(
        "/product/create_product",
        json={
            "name": product1,
            "price": 13,
            "seller_id": 1
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.dependency(depends=[
    "test_create_product"
])
def test_get_all_products():
    response = client.get("/product/list/all")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() is not None


@pytest.mark.dependency(depends=["test_create_product"])
def test_get_one_product(request):
    product_id = request.config.cache.get("product_id", None)
    response = client.get(f"/product/{product_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == product_id
    assert response.json()["name"] == product1


@pytest.mark.dependency(depends=[
    "test_create_product"
    "test_get_one_product"
])
def test_put_product(request):
    product_id = request.config.cache.get("product_id", None)
    temp_name = generate_random_string()
    response = client.put(
        f"/product/update/{product_id}",
        json={
            "name": temp_name,
            "price": 200,
            "seller_id": 1
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == product_id
    assert response.json()["name"] == temp_name
