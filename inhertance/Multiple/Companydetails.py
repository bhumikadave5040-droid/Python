class company:
    def __init__(self,dept,role,cname):
        self.dept=dept
        self.role=role
        self.cname=cname

#ins method
    def display_company(self):
        print("----Company Details----")
        print(f"Company Name: {self.cname} Department: {self.dept} Role: {self.role}")
    
    def show(self):
        print("hello I'm from company class")