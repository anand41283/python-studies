# num=int(input("enter a number:"))
# if (num==1):
#     print(f"{num} is not a prime number")
# elif (num>1):
#     for i in range(2,num):
#         if (num%i==0):
#             print(f"{num} is not a prime number")
#             break
#     else:   # else case of for loop  #The else block just after for/while is executed only when the loop is NOT terminated by a break statement.
#         print(f"{num} is a prime number")    
# else:
#     print(f"{num} is not a prime number")    



# n = int(input("enter a number: "))
# for i in range(n):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)


# def prime(num):
#     if (num==1):
#         print(f"{num} is not a prime number")
#     elif (num>1):
#         for i in range(2,num):
#             if (num%i==0):
#                 print(f"{num} is not a prime number")
#                 break
#         else:   # else case of for loop  #The else block just after for/while is executed only when the loop is NOT terminated by a break statement.
#             print(f"{num} is a prime number")    
#     else:
#         print(f"{num} is not a prime number")    


# prime(int(input("enter a number:")))

def prime(l_limit,u_limit):
    for i in range(l_limit,u_limit+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)


n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
prime(n1,n2)
