from B import P

class C(P):
    pqr="bye"

    def __init__(self,name,age,marks):
        super.__init__(name,age)
        self.marks=marks

obj=C("Bhumika",20,90)
print(obj.pqr,obj.xyz,obj.abc)
print(obj.name,obj.age,obj.marks)
