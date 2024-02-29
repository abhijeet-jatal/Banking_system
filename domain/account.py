from .utils import (
    generate_account_id,
    generate_account_number
)


class Account:

    def __init__(self, builder):
        self.account_id = builder.account_id
        self.customer_id = builder.customer_id
        self.account_number = builder.account_number
        self.balance = builder.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def get_balance(self):
        return self.balance

    @staticmethod
    def get_builder():
        return AccountBuilder()


class AccountBuilder:
    def __init__(self):
        self.account_id = generate_account_id()
        self.account_number = generate_account_number()
        self.customer_id = None
        self.balance = None

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id
        return self

    def set_balance(self, balance):
        self.balance = balance
        return self

    def build(self):
        if not all([self.account_id, self.customer_id, self.account_number, self.balance]):
            raise ValueError("Missing required attributes")
        return Account(self)
