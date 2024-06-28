#factorial of a number

# num=int(input("enter a number:"))
# fact=1
# if(num<0):
#     print("enter a valid number")
# elif(num==0):
#     fact=1
# else:
#     for i in range(1,num+1):
#         fact*=i
#     print(f"factorial of the number is {fact}")            


# using recursive function
def factorial(n): 
     
    # Checking the number
    # is 1 or 0 then
    # return 1
    # other wise return
    # factorial
    if (n==1 or n==0):
         
        return 1
     
    else:
         
        return (n * factorial(n - 1)) 
 

num = 5; 
print("number : ",num)
print("Factorial : ",factorial(num))


    