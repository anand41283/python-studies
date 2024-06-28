# def fibanocci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibanocci(n-2)+fibanocci(n-1)


# n=int(input("enter a number: "))
# for i in range(n):
#     print(fibanocci(i))


# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-2)+fib(n-1)
    
# c=5   
# for i in range(c):
#     print(fib(i))

# c=input("kk: ")
# rev=c[::-1]
# print (rev)

# b=int(input("enter: "))
# for i in range(2,b):
#     if b%i==0:
#         print("not prime")
#         break
#     else:
#         print("prime")   
#         break 

# k=[]
# my_list = ['apple', 'banana', 'cherry']
# for i in my_list:
#     k.append(i)
# print(k)    

keys = ['a', 'b', 'c', 'd']

# Create a dictionary with keys from the list 'keys' and default value set to None
my_dict = dict.fromkeys(keys)

print(my_dict)

