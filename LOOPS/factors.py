# find the factors of a number

num=int(input("enter a number:"))
for i in range(2,num):
    if(num%i)==0:
        print(f"factors = {i}")
   
