class AccountRepository:
    def __init__(self):
        self.accounts = {}  # Simulating a database with a dictionary
        self.transactions = []

    def save_account(self, account):
        self.accounts[account.account_id] = account

    def find_account_by_id(self, account_id):
        return self.accounts.get(account_id)

    def save_transaction(self, transaction):
        self.transactions.append(transaction)

    def find_transactions_by_account_id(self, account_id):
        return [t for t in self.transactions if t.account_id == account_id]
