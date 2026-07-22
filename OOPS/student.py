class demo:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age

#instance method
def welcome(self):
    return"hello students"

def modify(self):
    newvalue=input("enter new name")
    #print(f"existing name:{self.name}")
    ex_name=self.name
    self.name=newname
    print(f"existing name:{ex_name}updated name:{self.name}")

s1=demo("ram",101,21)
print(s1.name,s1.age,s1.id)
print(welcome())
s1.modify()


