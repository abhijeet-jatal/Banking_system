import unittest
from use_cases.user_use_case import UserUseCase


class TestAccountUseCase(unittest.TestCase):
    def test_create_account(self):
        user_use_case = UserUseCase()

        # Customer creation test
        customer = user_use_case.create_customer("Test User", "testuser@test.com", "1234567890")
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, "Test User")
        self.assertEqual(customer.email, "testuser@test.com")
        self.assertEqual(customer.phone_number, "1234567890")

        # Account creation test
        account = user_use_case.create_account(customer.customer_id, 100000)
        self.assertIsNotNone(account)
        self.assertEqual(account.customer_id, customer.customer_id)
        self.assertEqual(account.balance, 100000)
