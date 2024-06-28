"""
Static Method
-------------
A static method is a general utility method that performs a task in isolation. Inside this method,
we don't use instance or class variable because this static method doesn't take any parameters like self and cls.

A static method is bound to the class and not the object of the class. Therefore, we can call it using the class name.

A static method doesn't have access to the class and instance variables because it does not receive an implicit first argument like self and cls.

Therefore it can not modify the state of object or class


Syntax:
class ClassName(object):
    @staticmethod
    def function_name():
        pass
    
    
UTILITY FUNCTIONS
-----------------
A utility function in Python is a small,self-contained piece of code that performs a specific task.
Its called a 'utility' because its a helpful tool that makes a certain task easier to perform.
These functions are not meant to be standalone, but rather to be used in conjunction with otherr code.


Methods are two types:
1.instance methods
2.static method

"""
import datetime
class Operations:
    num1:int
    num2:int
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2
    def add(self): # instance method
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    @staticmethod
    def get_date():# static method
        return datetime.date.today()
    
obj=Operations(50,43)
print(obj.add())
print(obj.sub())
print(obj.get_date())
print(Operations.get_date())



