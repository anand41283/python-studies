class Student:
    rollno:int
    name:str
    course:str
    def add_student(self):#,rollno,name,course):#self refers to the specific instance of Class
        rollno=int(input("enter your rollno: "))
        name=input("enter your name: ")
        course=input("enter your course: ")
        self.rollno=rollno  #first rollno attribute,second one parameter
        self.name=name
        self.course=course
    def display(self):
        print("Roll no: ",self.rollno)#should call attribute using self--->refference keyword used to access atributes. identity of that class(object that identifies that particular class)
        print("Name: ",self.name)
        print("Course: ",self.course)
obj1=Student()
obj2=Student()
obj3=Student()
# obj1.add_student()#1,"ammu","python")
# obj2.add_student()
# obj3.add_student()
# obj1.display()
# obj2.display()
# obj3.display()
# #print(dir(obj1))
#print(obj1.__class__) # used to find class of an object

""" 
'self' represents instance of a class.This parameter allows you to access variables,attributes and methods
of a defined class

dir()

return all properties and methods of the specified object without values
"""

