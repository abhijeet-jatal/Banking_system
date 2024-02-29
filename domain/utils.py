import uuid
import random


def generate_account_id():
    """Generate unique account ID."""
    return str(uuid.uuid4())


def generate_account_number():
    """Generate unique account number."""
    return random.randint(10000000, 99999999)


def generate_customer_id():
    """Generate unique customer ID."""
    return str(uuid.uuid4())
