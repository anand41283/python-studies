#factorial of a number  (4! = 4*3*2*1)---->for loop

num=int(input("enter a number:"))
fact=1
x=num
if (num==0):
    fact=1
elif(num<0):
    print("enter valid number")    
while(x>1):
    fact*=x
    x-=1 
print(fact)       