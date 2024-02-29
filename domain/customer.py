from .utils import generate_customer_id


class Customer:

    def __init__(self, builder):
        self.customer_id = builder.customer_id
        self.name = builder.name
        self.email = builder.email
        self.phone_number = builder.phone_number

    def get_customer_id(self):
        return self.customer_id

    @staticmethod
    def get_builder():
        return CustomerBuilder()


class CustomerBuilder:

    def __init__(self):
        self.customer_id = generate_customer_id()
        self.name = None
        self.email = None
        self.phone_number = None

    def set_name(self, name):
        self.name = name
        return self

    def set_email(self, email):
        self.email = email
        return self

    def set_phone_number(self, phone_number):
        if len(phone_number) < 10 or len(phone_number) > 13:
            raise ValueError("invalid phone number")
        self.phone_number = phone_number
        return self

    def build(self):
        return Customer(self)
