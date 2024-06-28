# print right angled pyramid

n = int(input("enter the levels you want:"))
for i in range(n): # rows i=0,i=1....
    for j in range(i+1): # stars
        print("*", end="  ")
    print()


# reversed right angled pyramid

n=int(input("enter the levels you want:"))
for i in range(n,0,-1):
    for j in range (i):
        print("*",end=" ")
    print()


