from BankAcc import BankAcc
class SavingAcc(BankAcc):
    def __init__(self,accno,accholder,balance):
        super().__init__(accno,accholder,balance)
        

    def calculate_interest(self):
        amount=int(input("enter amount to calculate interest:"))
        months=int(input("enter number of months:"))
        interest=(amount*months)/100
        return interest
    
    def apply_interest(self):
        self.balance+=self.calculate_interest()
        return f"after applying interest the updated balance is {self.balance}"
    



