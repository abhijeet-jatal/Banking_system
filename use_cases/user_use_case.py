from domain.account import Account
from domain.customer import Customer


class UserUseCase:

    def create_customer(self, name, email, phone_number):
        """Create a new customer."""
        return (Customer.get_builder()
                .set_name(name)
                .set_email(email)
                .set_phone_number(phone_number)
                .build())

    def create_account(self, customer, balance):
        """Create a new account."""
        return Account.get_builder().set_customer(customer).set_balance(balance).build()
