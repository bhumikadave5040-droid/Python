from Parent1 import p1
from Parent2 import p2

class child(p1,p2):
    def __init__(self,c_name,p1name,p2name):
        self.c_name=c_name
        p1.__init__(self,p1name)
        p2.__init__(self,p2name)

obj=child("Bhumika","Alice","Bob")
print(obj.c_name)
print(obj.p1name)
print(obj.p2name)