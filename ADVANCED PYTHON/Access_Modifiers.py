"""
ACCESS MODIFIERS
-----------------
--> Access modifierss are used to set the accessibility (visibility) of classes,interfaces,variables,methods,
   constructors and data members.

--> There are 3 types of access modifiers.
    -> Public: accessible from anywhere in your code. default access modifier for all declarations.
    -> Private: only visible within its class or interface declaration.
    -> Protected: The members of a class that are declared protected are only accessible to a class derived from it.


Public Access Modifier
-----------------------
--> By default the member variables and methods are public which means they can be accessed from anywhere outside or inside the class.
--> No public keyword is required to make the class or methods and properties public.


Private Access Modifier
-----------------------
--> Class properties and methods within private access modifier can only be accessed within the class where they are defined and can not be accessed outside the class.
--> In Python private properties and methods are declared by adding a prefix with two underscores('__').
    before their declaration.



Protected Access Modifier
-------------------------
--> Protected access modifier allows you to restrict access to certain attributes/methods so that other
--> Class properties and methods with protected access modifier can be accessed within the class and from the class that inherits the protected class.
--> In Python, Protected members and methods are declared using single underscore('_') as prefix before their names.

"""

# Example of Public

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         return self.name,self.age
    
# s1=Student("Raj",20)
# print(s1.display())


# Example of Private

class Bank:
    def __init__(self,acc_num,balanc):
        self.acc_num=acc_num
        self.balanc=balanc
    def __display(self):
        print("Balance is",self.balanc)


b1=Bank(12345678,5000)
Bank.__display()
# b1.__display() #error attribute error



# Example of Protected

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def _display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)

# class Stud(Student):
#     def __init__(self, name, age,rollno):
#         super().__init__(name, age)
#         self.rollno=rollno
#     def display(self):
#         self._display()
#         print("Rollno:",self.rollno)

# s1=Stud("Mittu",23,8)
# s1.display()
            
