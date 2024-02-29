from repositories.account_repository import AccountRepository


class StatementUseCase:
    def generate_account_statement(self, account_id):
        """Generate account statement."""
        account = AccountRepository.find_account_by_id(account_id)
        statement = f"Account Statement for Account ID: {account.account_id}\n"
        # Append transaction details to statement
        return statement
