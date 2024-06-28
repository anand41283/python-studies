"""
Inner function
--------------
Python provides the facility to define the function inside another function.These types of functions are called inner functions.

"""
# def out_func():
#     print("We are in first function")
#     def func1():
#         print("This is first child function")
#     def func2():
#         print("This is second child function")
#     func1()
#     func2()
# out_func()

"""
Higher order function
---------------------
--> A function that accepts other function as an argument is also called higher order function.

"""
def add(x):
    return x+1
def sub(x):
    return x-1
def operators(func,x):
    return func(x)
print(operators(add,15))
print(operators(sub,10))

"""
Decorators
----------
-> Decorators are one of the most helpful and powerfful tools of python.
-> These are used to modify the behavior of the function.
-> Decorators provide the flexibility to wrap another function to expand the working of wrapped function,
   without permanently modifying it.
In decorators, functions are passed as an argument into another function and then called inside the wrapper function.

"""

#example:
def smartdiv(func):
    def inner(a,b):
        print("Iam going to divide",a,'and',b)
        if b==0:
            print("#oops can not divide")
            return
        return func(a,b)
    return inner
# def div(a,b):
#     print(a/b)
# result=smartdiv(div)
# result(4,5)

@smartdiv # This is a decorator which will take in any other function as parameter
def div(a,b):
    print(a/b)
div(4,5)
div(4,0)




