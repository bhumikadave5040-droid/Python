import datetime


dob1=input("enter your birth date :[yyyy,mm,dd]")
dob2=input("enter your birth date :[yyyy,mm,dd]")

dob1=datetime.date(dob1)
dob2=datetime.date(dob2)
if(dob1>dob2):
    print("dob1 is older than dob2")
else:
    print("dob2 is older than dob1")
