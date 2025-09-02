class BankAccount:
    def __init__(self,owner,account_type,balance=0):
        self.owner=owner
        self.account_number= self.get_account_number()
        self.account_type=account_type
        self.balance=balance
    
    # method checkBalance
    def check_balance(self):
        return f"{self.owner} your account balance is {self.balance}"

    def get_account_number(self):
        import random
        from datetime import datetime
        current_date=datetime.now()
        timeRand=current_date.strftime("%d%m%H%M%S")
        return timeRand
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            return f"{self.owner}, ₦{amount} has been deposit to your account"
        else:
            return f"Enter a valid amount"
    def withdraw(self, amount):
        if amount>0:
            self.balance+=amount
            return f"{self.owner}, ₦{amount} has been withdraw from your account"
        else:
            return f"Enter a valid amount"
    @staticmethod
    def create_account(name,acc_type,balance):
        account_details = BankAccount(name,acc_type, balance)
        msg = f"Hello {name}! Your account has been created. Your account Number is {account_details.account_number} with initial deposit of ₦{balance}"
        return msg, account_details
