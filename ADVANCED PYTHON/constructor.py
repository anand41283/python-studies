"""
constructor
-----------
--> duty: initializing instance variables----> for initialize objects
--> construcor name for java,cpp is same as class name(Student)
--> in python __init__() function is used for initializing.
--> The constructor is invoked(call) when the object is created
instance variables----> programmatic name of attributes
concept of initializing attributes is used by constructor
default constructor
parameteraised constructor
non parameteraised constructor

"""
class Student:
    rollno:int
    name:str
    course:str
    def __init__(self,rollno,name,course):#self refers to the specific instance of Class
        # rollno=int(input("enter your rollno: "))
        # name=input("enter your name: ")
        # course=input("enter your course: ")
        self.rollno=rollno  #first rollno attribute,second one parameter
        self.name=name
        self.course=course
    def display(self):
        print("Roll no: ",self.rollno)#should call attribute using self--->identity of that class(object that identifies that particular class)
        print("Name: ",self.name)
        print("Course: ",self.course)
obj1=Student(1,'anu','pyhton')  # we can pass values to attributes directly..it will automatically assign values to attributes
obj2=Student(2,'aku','data science')
obj3=Student(3,'lachu','mearn')
obj1.display()
obj2.display()
obj3.display()
