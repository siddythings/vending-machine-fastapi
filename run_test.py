import pytest

if __name__ == "__main__":
    pytest.main([
        "tests/test_users.py",
        "tests/test_products.py",
        "tests/test_deposit.py",
        "tests/test_buy.py",
    ])
