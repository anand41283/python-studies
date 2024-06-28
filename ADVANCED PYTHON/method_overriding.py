"""
Method overriding
-----------------
-> In object-oriented programming,is a language feature that allows a subclass or child class to provide a specific implementation of a method that is already provided 
   by one of its superclasses or parent classes

"""
class A:
    def func1(self):
        print("function1 in class A")
    def func(self):
        print("function2 in class A")

class B(A):
    def func3(self):
        print("function3 in class B")
    def func(self):
        print("function in class B")
        super().func()

b1=B()
b1.func1()
b1.func3()
b1.func()

