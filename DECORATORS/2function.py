# Write a program to create function func1() to accept a variable length of arguments and print their value
"""
In Python, sometimes, there is a situation where we need to pass multiple arguments to the function. Such types of arguments 
are called arbitrary arguments or variable-length arguments.

We use variable-length arguments if we don't know the number of arguments needed for the function in advance.

Types of Arbitrary Arguments:

arbitrary positional arguments (*args)
arbitrary keyword arguments (**kwargs)
The *args and **kwargs allow you to pass multiple positional arguments or keyword arguments to a function.

Arbitrary positional arguments (*args)
We can declare a variable-length argument with the * (asterisk) symbol. Place an asterisk (*) before a parameter in the function definition 
to define an arbitrary positional argument.

we can pass multiple arguments to the function. Internally all these values are represented in the form of a tuple



"""

# function with variable-length arguments
# def percentage(*args):
#     sum = 0
#     for i in args:
#         # get total
#         sum = sum + i
#     # calculate average
#     avg = sum / len(args)
#     print('Average =', avg)

# percentage(56, 61, 73)


def func1(*a):
    for i in a:
        print(i)
    
func1(20,30,40)