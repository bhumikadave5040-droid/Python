class car:
    brand="tata"
    def __init__(self,name,price,qty):
        self.name=name
        self.price=price
        self.qty=qty

c1=car("punch",1000,10)
c2=car("seira",5000,4)
c3=car("safari",50000,25)
#all info
x=[c1,c2,c3]
total=0
for i in x:
    print(i.name,i.price)
    total+=(i.qty*i.price)
    
    print("-------------------")
print(total)

for i in x:
    if i.qty>4 and i.qty<25:
        print(i.name,i.qty)
