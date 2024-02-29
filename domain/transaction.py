from datetime import datetime


class Transaction:
    def __init__(self, account_id, amount, transaction_type, transaction_date=None):
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.transaction_date = transaction_date or datetime.now()

    def __repr__(self):
        return (f"Transaction(account_id={self.account_id}, amount={self.amount}, type={self.transaction_type}, \\"
                f"date={self.transaction_date})")
