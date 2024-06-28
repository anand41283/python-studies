"""
SCOPE OF A VARIABLE
-------------------
1.Local variable---> inside the function(can access only inside the function)
   Its scope is limited to its own function
2.Global variable--> outside the function(can access throughout the program)
   Its scope is available throughout the program

"""
x=10 #global variable
def add():
    a=20 #local variable
    return(a+x)
print(add())
#print(a) # will throw error