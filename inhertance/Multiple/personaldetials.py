class person:
    def __init__(self,name,city,age):
        self.name=name
        self.city=city
        self.age=age

#instance method
    def display_personal_info(self):
        print("----Person Details----")
        print(f"Name: {self.name} age: {self.age} city: {self.city}")

    def show(self):
        print("hello I'm from person class")