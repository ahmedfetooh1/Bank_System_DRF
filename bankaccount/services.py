from .models import BankAccount ,Transaction




class ManageBankAccount:

    @staticmethod
    def get_account_by_id(pk):
        return BankAccount.objects.get(id=pk)
    

    @staticmethod
    def create_bank_account(**user):
        bank_account = BankAccount.objects.create(**user)
        return bank_account
    

    @staticmethod
    def get_all_bank_accounts():
        return BankAccount.objects.all()
    
class ManageTransaction:

    @staticmethod
    def get_all_transaction():
        return Transaction.objects.select_related('account').all()
    

    @staticmethod
    def get_transaction_by_id(pk:int):
        return Transaction.objects.get(id=pk)
    