class vehicle:
    def __init__(self,fuel_type,brand):
        self.fuel_type=fuel_type
        self.brand=brand
    
    def start(self):
        return("Vehicle is starting")
    def stop(self):
        return("Vehicle is stopping")