num=int(input("enter a number:"))
temp=num
rev=0
while(temp>0):
    dig=temp%10
    rev=rev*10+dig
    temp//=10
if (rev==num):
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")

