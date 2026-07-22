from personaldetials import person
from Companydetails import company

class employee(person, company):
    def __init__(self, name, city, age, dept, role, cname,salary):
        #classname.__init__(self, parameters)
        person.__init__(self, name, city, age)
        company.__init__(self, dept, role, cname)
        self.salary = salary

    def display_emp_info(self):
        print("-----all information of employee----")
        print()
        self.display_personal_info()
        print()
        self.display_company()
        print()
        print(f"salary:{self.salary}")

