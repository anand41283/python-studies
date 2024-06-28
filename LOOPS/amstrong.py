#print to check given number is amstrong or not

# num=int(input("enter the number: "))
# cube=0
# for i in str(num):
#     cube+=int(i)**3
# if (cube==num):
#     print(f"{num} is an amstrong number")
# else:
#     print(f"{num} is not a amstrong number")



#method2 using while loop

num = int(input("enter a number:"))
sum=0
temp=num
while(temp>0):
    digit=temp%10
    sum+=digit**3
    temp//=10
if (sum==num):
    print("amstrong number")
else:
    print("not amstrong number")        







