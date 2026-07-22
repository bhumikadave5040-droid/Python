import math

print(math.pi)
print(math.sqrt(25))
print(math.ceil(45.63))
print(math.floor(45.01))
print(math.pow(2,3))

import random as r
print(r.randint(1000,9999))
print(r.random())
print(r.randrange(2,20,2))

x=["red","black","pink","white"]
print(r.choice(x))
print(r.choices(x,k=2))
r.shuffle(x)
print(x)

import datetime
d=datetime.datetime.now()#current time
print(d)
print(d.day)
print(d.year)
print(d.month)

today_date=datetime.date.today()
print(today_date)

dob=datetime.date(2005,4,1)
cd=datetime.date.today()
print(cd.year-dob.year)