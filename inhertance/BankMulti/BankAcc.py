class BankAcc:
    def __init__(self,accno,accholder,balance):
        self.accno=accno
        self.accholder=accholder
        self.balance=balance
#method to deposit amount into the account
    def deposit(self):
        amount=int(input("enter the amount to deposit:"))
        self.balance+=amount
        print("Amount deposited:",amount)
        return f"Updated balance: {self.balance}"
    
    def withdraw(self):
        amount=int(input("enter the amount to withdraw:"))
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            return f"Amount withdrawn: {amount}\nUpdated balance: {self.balance}"
           
    def get_balance(self):
        return self.balance
    def create_account(self):
        accno=int(input("enter account number:"))
        accholder=input("enter account holder name:")
        balance=int(input("enter balance:"))
        obj=BankAcc(accno,accholder,balance)
        print("account created successfully")
        return f"Account number: {obj.accno}\nAccount holder name: {obj.accholder}\nBalance: {obj.balance}"


