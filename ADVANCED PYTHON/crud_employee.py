"""
create a class "employee" that has one attribute emp_data(contains 5 items).and perform all operations 
listed below:
1. display all data
2. get one employee details
3. add one employee to the user
4. update an existing employee's detail
(emp_id,emp_name,dept,salary)

"""
class Employee:
    employee_data=[
        {"emp_id":1,"emp_name":"anu","dept":"sales","salary":35000,"email":"anu@gmail.com"},
        {"emp_id":2,"emp_name":"arun","dept":"banking","salary":50000,"email":"aru@gmail.com"},
        {"emp_id":3,"emp_name":"vinu","dept":"marketing","salary":45000,"email":"vinu@gmail.com"},
        {"emp_id":4,"emp_name":"ganga","dept":"manager","salary":65000,"email":"ganga@gmail.com"},
        {"emp_id":5,"emp_name":"manu","dept":"business","salary":45000,"email":"manu@gmail.com"},
        {"emp_id":6,"emp_name":"jyothi","dept":"sales","salary":35000,"email":"jyothi@gmail.com"},
        
    ]

    # display all data
    def display_all_data(self):
        print(self.employee_data)

    # get one employee details
    def get_one_employee(self,id):
        for emp in self.employee_data:
            if emp.get("emp_id")==id:
                print(emp)
    # add one employee to the user
    def add_employee(self,item):
        for emp in self.employee_data:
            if emp.get("emp_id")==item.get("emp_id"):
                print("id already exist")
                break
        else:
            self.employee_data.append(item)
            print("item added successfully")
    # update an existing employee_details
    # def update_employee(self,id):
    #     for emp in self.employee_data:
    #         if emp.get("emp_id")==id:
    #             updation=int(input("enter what you want to update:1.emp_id 2.emp_name 3.dept 4.salary 5.email "))
    #             if updation==1:
    #                 new_empid=int(input("enter new_empid: "))
    #                 emp["emp_id"]=new_empid
    #             elif updation==2:
    #                 new_empname=input("enter new name: ")
    #                 emp["emp_name"]=new_empname
    #             elif updation==3:
    #                 new_dept=input("enter new_dept: ")
    #                 emp["dept"]=new_dept
    #             elif updation==4:
    #                 new_salary=int(input("enter new_salary: "))
    #                 emp["salary"]=new_salary
    #             elif updation==5:
    #                 new_email=input("enter new_email: ")
    #                 emp["email"]=new_email
    #             else:
    #                 print("enter a valid updation")


    def update(self,id,value):
        for user in self.employee_data:
            if user.get("emp_id")==id:
                pos=self.employee_data.index(user)
                self.employee_data[pos]=value
                print(type(value))
                    
                       



em=Employee()
# em.display_all_data()
# em.get_one_employee(2)
# em.add_employee({"emp_id":7,"emp_name":"janu","dept":"marketing","salary":45000,"email":"janu@gmail.com"})
# em.display_all_data()
#em.update_employee(2)
use={"emp_id":5,"emp_name":"alka","dept":"sales","salary":45000,"email":"alka@gmail.com"},
em.update(5,use)
#em.display_all_data()

#em.get_one_employee(5)