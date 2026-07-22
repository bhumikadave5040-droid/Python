from Engine import engine
class car:
    def __init__(self, uip):
        self.age=90
        self.a=engine(uip)
    
    def  car_details(self):
        print(self.a.show_details())
        return f"car details are{self.age}"
    
obj=car(100)
print(obj.age,obj.a.name,obj.a.horsepower)
print(engine.brand)

#method calling by print because method is returning some value so we can print it
print(obj.car_details())

#print(obj.a.show_details())
