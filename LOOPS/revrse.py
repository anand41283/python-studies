num=int(input("enter a number:"))
rev=0
while(num>0):
    dig=num%10
    rev=(rev*10)+dig
    num//10
print(rev)    

"""
case1
num=421
rev=124
num%10 =421%10 = 1
rev=0*10+1=1
num//10=421//10=42

case2

num%10=42%10=2
rev=1*10+2=12
num//10=42//10=4

case3
num%10=4%10=4
rev=12*10=124
num//10=4//10=0

rev=124
"""