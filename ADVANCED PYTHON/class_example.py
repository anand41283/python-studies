# Define a class named American and its subclass NewYorker.
# Define a class named circle which can be constructed by a radius.The circle has a method which can compute the area.


# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area_circle(self):
#         print("area of the circle : ",3.14*(self.radius)**2)

# c=Circle(10)
# c.area_circle()


# Define a class named rectangle which can be constructed by a length and width.The rectangle class has a method which can compute the area.


# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def Area(self):
#         print("Area of rectangle is:",self.length*self.width)

# rec=Rectangle(3,2)
# rec.Area()

# user input
class Rectangle:
    def __init__(self):
        self.length = int(input("enter length of rectangle: "))
        self.width = int(input("enter width of rectangle: "))

    def Area(self):
        print("Area of rectangle is:", self.length*self.width)


rec = Rectangle()
rec.Area()
