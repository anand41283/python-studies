class Employee:
    emp_id:int
    emp_name:str
    dep:str
    salary:int
    def __init__(self,id,name,dept,salary):
        self.emp_id=id
        self.emp_name=name
        self.dep=dept
        self.salary=salary
    def display(self):
        print("employee_id: ",self.emp_id)
        print("employee_name: ",self.emp_name)
        print("employee_dept: ",self.dep)
        print("employee_salary: ",self.salary)

obj1=Employee(100,'arun','banking',50000)
obj2=Employee(101,'arjun','sales',40000)
obj1.display()
obj2.display()