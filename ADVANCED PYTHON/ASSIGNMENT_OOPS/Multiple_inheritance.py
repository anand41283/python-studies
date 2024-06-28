# create a class that implement multiple inheritance

class Parent1:
    def method1(self):
        print("Method from Parent1")

class Parent2:
    def method2(self):
        print("Method from Parent2")

class Child(Parent1, Parent2):
    def method3(self):
        print("Method from Child")

# Example usage:
child = Child()

child.method1()  # Calls method from Parent1
child.method2()  # Calls method from Parent2
child.method3()  # Calls method from Child


"""
We define two parent classes, Parent1 and Parent2, each with their own methods.

We then create a Child class that inherits from both Parent1 and Parent2 using multiple inheritance.

The Child class has its own method method3.

In the example usage section, we create an instance of the Child class and demonstrate that it can access 
methods from both Parent1 and Parent2, as well as its own method method3.

Multiple inheritance allows a class to inherit attributes and methods from multiple parent classes,
but it's important to use it carefully to avoid conflicts and maintain a clear understanding of the class hierarchy.
"""
