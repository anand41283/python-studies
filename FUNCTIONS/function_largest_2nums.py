# #create a function to find largest among two numbers with 2 parameters
# def largest(n1,n2):
#     if (n1>n2):
#         return n1
#     else:
#         return n2
# print(largest(100,34))

#ternary operator

def largest(n1,n2):
   return(n1 if n1>n2 else n2)    
print(largest(100,34))