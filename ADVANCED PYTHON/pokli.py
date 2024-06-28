class Student():
    def __init__(self,name,roll_no,dept):
        self.name=name
        self.roll_no=roll_no
        self.dept=dept

    def display(self):
        print(self.name)
        print(self.roll_no)
        print(self.dept)

obj=Student("ajay",1,"cs")
obj.display()