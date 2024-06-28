lower_limit=int(input("enter lower_limit: "))
upper_limit=int(input("enter upper_limit: "))
for i in range(lower_limit,upper_limit+1):
    if(i%2!=0):
        print(i)