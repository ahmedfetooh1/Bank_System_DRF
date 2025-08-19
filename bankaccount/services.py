from .models import BankAccount ,Transaction




class ManageBankAccount:

    @staticmethod
    def get_account_by_id(pk):
        return BankAccount.objects.get(id=pk)
    

    @staticmethod
    def create_bank_account(user):
        bank_account = BankAccount.create(**user)
        return bank_account
    
    