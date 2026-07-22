class mobile:
    def __init__(self,Uname,ubrand,ucolour,uprice):
        self.name=Uname
        self.brand=ubrand
        self.colour=ucolour
        self.price=uprice

obj=mobile("iphone17","IPhone","white",150)    
print(obj.name,obj.brand,obj.colour,obj.price)
obj1=mobile("iphone15","IPhone","pink",160)    
print(obj1.name,obj.brand,obj.colour,obj.price)  


#store object inside loop
x=[obj,obj1]
for i in x:
    print(i.name)