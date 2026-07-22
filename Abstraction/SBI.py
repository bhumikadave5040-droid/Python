from ATM import ATM
class SBI(ATM):
    def withdraw(self, amount):
        if amount>0:
            self.bal-=amount
            print(f"amount is {amount} debited")


obj=SBI(1000)
print(obj.getbal())
obj.withdraw(300)
print(obj.getbal())
