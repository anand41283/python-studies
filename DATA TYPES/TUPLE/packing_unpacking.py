# Packing 
"""The process of assigning values to a tuple is known as packing

Unpacking
--> The process that assigns the value on the right hand side to the left hand side variable extract the values of the tuple into a single variable
--> If no of variables less than the number of values you can add an * to the variable name and the value will be assigned to the variable as a list.
"""
# Example of packing
#--------------------
a=1,2,3
print(a)

# Example of unpacking
#---------------------
b,c,d=a
d,*b=a
# *d,b=a
print(d)
print(b)