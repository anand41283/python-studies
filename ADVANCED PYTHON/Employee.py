"""
class employee:
    emp_id
    name
    dept
    salary
    
    add_emp()
    display()
    
"""

class Employee:
    emp_id:int
    emp_name:str
    dep:str
    salary:int
    def add_employee(self):
        id=int(input("enter employee id: "))
        name=input("enter employee name: ")
        dept=input("enter dept name: ")
        salary= int(input("enter salary: "))
        self.emp_id=id
        self.emp_name=name
        self.dep=dept
        self.salary=salary
    def display(self):
        print("employee_id: ",self.emp_id)
        print("employee_name: ",self.emp_name)
        print("employee_dept: ",self.dep)
        print("employee_salary: ",self.salary)

obj1=Employee()
obj2=Employee()
obj1.add_employee()
obj1.display()
obj2.add_employee()
obj2.display()