# print fibinacci series
"""0,1,1,2,3,5,8,13,21....
0+1=1
1+1=2
2+1=3
3+2=5
5+3=8
8+5=13
13+8=21
"""
def fibinocci(limit):
    
    n1,n2=0,1
    count=0
    if (limit<=0):
        print("enter a valid number")
    elif (limit==1):
        print(n1)    
    else:
        while (count<=limit):
            print(n1)
            n3=n1+n2
            n1=n2
            n2=n3
            count+=1    


limit=int(input("enter a number:"))
fibinocci(limit)


# def fibinocci(n):
#     f1=0
#     f2=1
#     sum=0
#     print(f1)
#     print(f2)
#     for i in range(n):
#         sum=f1+f2
#         print(sum)
#         f1=f2
#         f2=sum

# fibinocci(5)