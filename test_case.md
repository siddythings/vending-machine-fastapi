# Vending Machine FastAPI - Test Case

## User Tests

- **test_create_buyer_user**
    - Creates a new buyer user with a random username and verifies the successful creation of the user.
    - Stores the user's ID in the cache for future reference.

- **test_create_owner_user**
    - Creates a new owner user with a random username and verifies the successful creation of the user.
    - Stores the user's ID in the cache for future reference.

- **test_duplicate_user**
    - Attempts to create a user with the same username and role as an existing user.
    - Verifies that the server returns a conflict status (HTTP 409).

- **test_get_all_users**
- Retrieves the list of all users and verifies that the response status is OK (HTTP 200) and the response is not empty.

- **test_get_one_user**
    - Retrieves the details of a specific user (buyer) using the user ID obtained from the cache.
    - Verifies that the response status is OK (HTTP 200) and the user details match the initial creation values.

- **test_patch_user**
    - Updates the username of an existing user (buyer) using a random username.
    - Verifies the successful update of the user and checks that the response status is OK (HTTP 200).

- **test_delete_user**
    - Deletes a user (buyer) using the user ID obtained from the cache.
    - Verifies that the user is successfully deleted, and the response status is ACCEPTED (HTTP 202).
    - This test case has dependencies on other tests.


## Product Tests

- **test_create_product**
    - Creates a product with a random name, a price of 5, and a seller ID of 1.
    - Verifies the successful creation of the product and stores the product ID in the cache for future reference.

- **test_create_product2**
    - Creates another product with the same name as the first product but with a higher price (25) and the same seller ID (1).
    - Verifies the successful creation of the second product and updates the product ID in the cache.

- **test_create_product_with_invalid_amount**
    - Attempts to create a product with the same name as the first product but with an invalid price (13).
    - Verifies that the server returns a bad request status (HTTP 400).

- **test_get_all_products**
    - Retrieves the list of all products and verifies that the response status is OK (HTTP 200) and the response is not empty.
    - Depends on the successful execution of `test_create_product`.

- **test_get_one_product**
    - Retrieves the details of a specific product using the product ID obtained from the cache.
    - Verifies that the response status is OK (HTTP 200) and the product details match the initial creation values.
    - Depends on the successful execution of `test_create_product`.

- **test_put_product**
    - Updates the details of an existing product using a new random name and a higher price (200).
    - Verifies the successful update of the product and checks that the response status is OK (HTTP 200).
    - Depends on the successful execution of `test_create_product` and `test_get_one_product`.


## Deposit Tests

- **test_create_buyer_user**
    - Creates a buyer user with a random username and role "buyer."
    - Verifies the successful creation of the user and stores the user ID in the cache for future reference.

- **test_create_deposit**
    - Creates a deposit for the buyer user with a user ID obtained from the cache and an amount of 100.
    - Verifies the successful creation of the deposit and stores the user ID in the cache.

- **test_create_deposit_invalid_amount**
    - Attempts to create a deposit for the buyer user with an invalid amount (99).
    - Verifies that the server returns a bad request status (HTTP 400).

- **test_get_deposit_detail**
    - Retrieves the details of the deposit for the buyer user using the user ID obtained from the cache.
    - Verifies that the response status is OK (HTTP 200).
    - Depends on the successful execution of `test_create_deposit`.

## Buy Tests

- **test_create_deposit**
    - Creates a deposit for the buyer user with an amount of 100.
    - Verifies the successful creation of the deposit and stores the user ID in the cache for future reference.

- **test_create_purchase**
    - Creates a purchase for the buyer user with a specified product ID (PRODUCT_ID_1) and quantity.
    - Verifies the successful purchase and checks various aspects of the response, including `product ID`, `quantity`, `total spent`, `user ID`, and `change` in `acceptable coins`.

- **test_insufficient_funds**
    - Attempts to create a purchase for the buyer user with insufficient funds for the specified product (`PRODUCT_ID_2`).
    - Verifies that the server returns a bad request status (HTTP 400) with the detail "Insufficient funds."

- **test_reset_buyer_account**
    - Resets the deposit for the buyer user.
    - Verifies the successful reset of the deposit and checks the response details.
