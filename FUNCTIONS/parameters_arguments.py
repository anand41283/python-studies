"""
PARAMETERS AND ARGUMENTS
------------------------
parameter---> function definition
arguments---> function call

"""
# def add(a,b):
#     return(a+b)
# c=10
# d=20
# print(add(c,d))

#in the above example a,b are parameters and c,d are arguments

# default arguments
# def add(a=10,b=20):
#     return(a+b)
# print(add(1,2)) # 3
# print(add(5)) # 25
# print(add()) # 30

# Arbitrary arguments
def sum(*n): # if we don't know how many arguments are going to be given put a * before parameter
    res=0
    for i in n:
        res+=i
    return res
print(sum(1,2,3))

#Recurssion 
"""
Function call itself
"""
# def abc():
#     print("hai")
#     abc()
# abc()

#find factorial of a number
def fact(n):
    if n<=1:
        return 1
    else:
        return (n* fact(n-1))
print(fact(5))    
