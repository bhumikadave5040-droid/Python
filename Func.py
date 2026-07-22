#no return type no argument
def greet():
    print("welcome user")

greet()

#no return with argument
def greet1(name):
    print("welcome",name)

name=input("enter your name")
greet1(name)

#with return type no argument

def getno():
    return 10**2
print(getno())

op=getno()
print(op)
op+=2
print(op)