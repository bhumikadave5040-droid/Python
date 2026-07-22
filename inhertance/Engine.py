class engine:
    brand="xyz"
    def __init__(self, horsepower):
        #ins var manually
        self.name = "v8"
        #user ip when obj get created at that time user will send some ip
        self.horsepower = horsepower

    def show_details(self):
        return f"engine details are {self.brand} {self.name} {self.horsepower}"