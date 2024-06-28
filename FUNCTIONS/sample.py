# a=input("Enter the : ")
# c=a[::-1]
# if a==c:
#     print("its pali")
# else:
#     print("not")    

# keys = ['a', 'b', 'c', 'd','hh']

# # Create a dictionary with keys from the list 'keys' and default value set to None
# my_dict = dict.fromkeys(keys)



# my_dict['a']="car"
# my_dict['e']="caroo"
# print(my_dict)

# a=int(input("Enter number "))
# sum=0
# temp=a
# while temp  > 0:
#     digit=temp%10
#     sum+=  digit**3
#     temp//=10

# if a==sum:
#     print("arm")
# else:
#     print("not num")    

# li=[1,2,3,4]
# print((li))

def fib(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fib(n-2)+fib(n-1)
    
d=int(input("range: "))
for i in range(d):
    
    print(fib(i))
