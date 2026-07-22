from EmployeeDetails import employee
from personaldetials import person
from Companydetails import company


obj=employee("Bhumika","pune","20","IT","developer","Linkcode",50000000)

obj.display_emp_info()
obj.show()
#obj.show() mro-->child-->p1,p2 resolve
#same method 2 class : classname,Methodname_call(obj) of class pass

person.show(obj)
company.show(obj)