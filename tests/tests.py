import pytest
from use_cases.user_use_case import UserUseCase
from tests.conftest import customer_and_account


def test_create_account():
    user_use_case = UserUseCase()

    # Customer creation test
    customer = user_use_case.create_customer("Test User", "testuser@test.com", "1234567890")
    assert customer is not None
    assert customer.name == "Test User"
    assert customer.email == "testuser@test.com"
    assert customer.phone_number == "1234567890"

    # Account creation test
    account = user_use_case.create_account(customer, 100000)
    assert account is not None
    assert account.customer.customer_id == customer.customer_id
    assert account.balance == 100000


def test_valid_withdraw(customer_and_account):
    _, account = customer_and_account
    initial_balance = account.get_balance()
    account.withdraw(10000)
    assert account.get_balance() == initial_balance - 10000


def test_invalid_withdraw(customer_and_account):
    _, account = customer_and_account
    initial_balance = account.get_balance()
    with pytest.raises(ValueError) as excinfo:
        account.withdraw(initial_balance + 1000)
    assert str(excinfo.value) == "Insufficient funds"


def test_deposit(customer_and_account):
    _, account = customer_and_account
    initial_balance = account.get_balance()
    account.deposit(100)
    assert account.get_balance() == initial_balance + 100
