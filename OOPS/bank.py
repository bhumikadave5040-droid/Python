class bank:
    #class var
    bankname="SBI"
    ifsc="SBI100"

    def __init__(self,name,bal,email):
        self.name=name
        self.bal=bal        
        self.email=email

    def show_details(self):
        print(f"name:{self.name}\nbalance:{self.bal}\nEmail:{self.email}\nBankname:{self.bankname}\nIfsc:{self.ifsc}")

    def check_balance(self):
        print("available bal:",self.bal)

    def deposit(self):
        amount=int(input("Enter the amount"))
        if amount>0:
         self.bal+=amount
         print("deposited",amount)
         print("available balance:",self.bal)
        else:
            print("amount should be greater than 0")

    def withdraw(self):
        amount=int(input("Enter the amount"))
        if amount<self.bal:
            self.bal-+amount
            print(f"withdraw amount is rs{amount}")
        
        else:
            print("insuf bal")

def compare():
        if user1.bal>user2.bal:
            print("User 1 is gretar") 
            user1.show_details() 
        else:
            print("user 2 is greater")
            user2.show_details()



user1=bank("ram",0,"ram@gmail.com")
user1.show_details()
user1.check_balance()
user1.deposit()
user2=bank("bhumika",0,"bhumika@gmail.com")
user2.show_details()
user2.check_balance()
user2.deposit()
compare()




