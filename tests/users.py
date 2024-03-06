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


user1 = generate_random_string()
user2 = generate_random_string()
initial_username_owner = user1
initial_role_owner = "owner"

initial_username_buyer = user2
initial_role_buyer = "buyer"


@pytest.mark.dependency()
def test_create_owner_user(request):
    response = client.post(
        "/user/create_user",
        json={
            "username": initial_username_owner,
            "role": initial_role_owner
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["username"] == user1
    assert response.json()["role"] == "owner"
    request.config.cache.set("user_id", response.json()["id"])


@pytest.mark.dependency()
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
    request.config.cache.set("user_id", response.json()["id"])


@pytest.mark.dependency()
def test_dublicate_user(request):
    response = client.post(
        "/user/create_user",
        json={
            "username": initial_username_buyer,
            "role": initial_role_buyer
        },
    )
    assert response.status_code == status.HTTP_409_CONFLICT


@pytest.mark.dependency(depends=[
    "test_create_buyer_user"
])
def test_get_all_users():
    response = client.get("/user/list/all")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() is not None


@pytest.mark.dependency(depends=["test_create_buyer_user"])
def test_get_one_user(request):
    user_id = request.config.cache.get("user_id", None)
    response = client.get(f"/user/{user_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == user_id
    assert response.json()["username"] == initial_username_buyer
    assert response.json()["role"] == initial_role_buyer


@pytest.mark.dependency(depends=["test_create_buyer_user"])
def test_patch_user(request):
    user_id = request.config.cache.get("user_id", None)
    temp_name = generate_random_string()
    response = client.patch(
        f"/user/update/{user_id}",
        json={
            "id": user_id,
            "username": temp_name,
            "role": initial_role_buyer,
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == user_id
    assert response.json()["username"] == temp_name
    assert response.json()["role"] == initial_role_buyer


@pytest.mark.dependency(
    depends=[
        "test_create_buyer_user",
        "test_patch_user",
        "test_get_one_user",
        "test_get_all_users",
    ]
)
def test_delete_user(request):
    user_id = request.config.cache.get("user_id", None)
    response = client.delete(f"/user/delete/{user_id}")
    assert response.status_code == status.HTTP_202_ACCEPTED
    assert response.json()["detail"] == "User Deleted"
