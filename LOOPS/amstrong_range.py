lower_limit=int(input("enter lower_limit:"))
upper_limit=int(input("enter upper_limit:"))
for i in range(lower_limit,upper_limit+1):
    sum=0
    length=len(str(i))
    temp=i
    while(temp>0):
        digit=temp%10
        sum+=(digit**length)
        temp//=10
    if (sum==i):
        print(i)    
