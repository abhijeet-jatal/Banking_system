from repositories.account_repository import AccountRepository


class TransactionUseCase:
    def make_transaction(self, account_id, amount, transaction_type):
        """Make a transaction."""
        account = AccountRepository.find_account_by_id(account_id)
        if transaction_type == 'deposit':
            account.deposit(amount)
        elif transaction_type == 'withdraw':
            account.withdraw(amount)
        else:
            raise ValueError("Invalid transaction type")
