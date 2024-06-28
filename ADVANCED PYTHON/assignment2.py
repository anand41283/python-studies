"""
define a class which has at least two methods:
getString:to get a string from console input
printString:to print the string in uppercase
also include simple test function to test the class methods
"""
class Test:
    def __init__(self):
        self.string=""
    def getString(self):
        self.string=input("enter your string: ")
        
    def printString(self):
        print(self.string.upper())
def test_function():  
    obj1=Test()
    obj1.getString()
    obj1.printString()

test_function()

# class String:
    
#     def getString(self):
#         self.string=input("enter your string: ")
        
#     def printString(self):
#         print(self.string.upper())
    
# obj1=String()
# obj1.getString()
# obj1.printString()



# Define a class, which have a class parameter and have a same instance parameter
# Define a instance parameter, need add it in __init__ method
# You can init a object with construct parameter or set the value later

class Person():
    age=20
    def __init__(self,al):
        self.al=al
obj1=Person(12)
print(obj1.age)
print(obj1.al)
print(Person.age)