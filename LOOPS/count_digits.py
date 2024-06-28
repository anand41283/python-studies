#method1
num=int(input("enter a number:"))
length=len(str(num))
print(f"count of digits in {num} is {length}")


#method2
num=int(input("enter a number:"))
count=0
while(num>0):
    count+=1
    num//=10
print(count)    




