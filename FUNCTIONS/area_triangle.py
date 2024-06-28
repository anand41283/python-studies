#find area of a triangle
def area_triangle(b,h):
    return(b*h)/2
base=float(input("enter base value: "))
height=float(input("enter height: "))
print("Area of triangle is",area_triangle(base,height))