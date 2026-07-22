from SavingAcc import SavingAcc
class Premiumacc(SavingAcc):
    def __init__(self, accno, name, balance):
        super().__init__(accno, name, balance)
       

    def calculate_benefits(self):
        if self.balance>5000:
            benefits=5000
            ch=input("do you want to add this benefits? (yes/no):")
            if ch=="yes":
                self.balance+=benefits
                return f"after adding benefits of {benefits} the updated balance is {self.balance}"
            else:
                return "benefits not added"
        else:
            return "maintain basic limit of premium acc rs200"

obj=Premiumacc(accno=0, name="", balance=0)
print(obj.deposit(),obj.withdraw())
print(obj.calculate_interest(),obj.apply_interest())
print(obj.calculate_benefits())


