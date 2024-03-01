import pytest
from use_cases.user_use_case import UserUseCase


@pytest.fixture()
def customer_and_account():
    user_use_case = UserUseCase()
    # Customer creation
    customer = user_use_case.create_customer("Test User", "testuser@test.com", "1234567890")
    # Account creation
    account = user_use_case.create_account(customer, 100000)

    return customer, account
