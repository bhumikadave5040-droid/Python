from BankAcc import BankAcc
from SavingAcc import SavingAcc
from Premiumacc import Premiumacc

print("Welcome to xyz bank")
while True:
    ch=input("1.admin\n2.user:")
    match ch:
        case "1":
            print("1.deposit\n2.withdraw\n3.calculate interest\n4.apply interest\n5.calculate benefits")
            ch1=input("enter your choice:")
            match ch1:   
                case "1":
                    print(obj.deposit())
                case "2":
                    print(obj.withdraw())
                case "3":
                    print(obj.calculate_interest())
                case "4":
                    print(obj.apply_interest())
                case "5":
                    print(obj.calculate_benefits())
        case "2":
            print("1.create account\n2.withdraw\n3.get balance")
            ch2=input("enter your choice:")
            match ch2:
                case "1":
                    print(obj.create_account())
                    obj=Premiumacc(accno=0, name="", balance=0)
                case "2":
                    print(obj.withdraw())
                case "3":
                    print(obj.get_balance())
