"""
Assignments
---------------

1. Write a python pgm to create a class representing a circle. Include methods to find area and perimeter

2.W.p to create a calculator class. include methods for arithematic operations

3. Write a Python program to create a class that represents a shape. Include methods to calculate its area 
and perimeter. Implement subclasses for different shapes like circle, triangle, and square.

4. create a class that implement method overriding

5. create a class that implement multiple inheritance


"""

# 1. Write a python pgm to create a class representing a circle. Include methods to find area and perimeter

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area_circle(self):
        return (3.14*self.radius**2)
    
    def perimeter_circle(self):
        return (2*3.14*self.radius)
    

c=Circle(5)
print(c.area_circle())
print(c.perimeter_circle())