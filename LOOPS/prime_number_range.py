# print all the prime numbers in an interval
lower_limit=int(input("enter the lower_limit:"))
upper_limit=int(input("enter the upper_limit:"))
for i in range(lower_limit,upper_limit+1):
    if i>1:
        for x in range(2,i):
            if (i%x==0): #not prime number(rem==0)
                break
        else:
            print(i) 
              



