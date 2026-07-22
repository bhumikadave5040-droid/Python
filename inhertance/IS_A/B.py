from A import A
class B(A):
    def __init__(self):
        print("B class constructor")

obj=B()
print(B.mro())#mro is method resolution order it will tell us which class is called first and which class is called next