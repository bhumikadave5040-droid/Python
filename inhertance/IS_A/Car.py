from Vehicle import vehicle
class car(vehicle):
    def __init__(self,colour,price,fuel_type,brand):
        self.colour=colour
        self.price=price
        
        super().__init__(fuel_type,brand)#super() is used to call the constructor of the parent class

    def ride(self):
        return("Car is riding")
    
    def custom_start(self):
        print(super().start())#super() is used to call the method of the parent class
        return "brummm brummm"
    
    def avg(self):
        total_distance=int(input("Enter total distance travelled by car in km: "))
        total_petrol=int(input("Enter total petrol consumed by car in litres: "))
        
        return total_distance / total_petrol
    
    def remaining_petrol(self):
       pass
    




c1=car("red",1000000,"petrol","BMW")
print(c1.ride())
print(c1.fuel_type)
print(f"Average mileage: {c1.avg()} km/litre")

#find remaining petrol, car runs 10km per litre of petrol, car has 50 litres of petrol, how many km can the car run?
