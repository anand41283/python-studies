# l1=[]
# square=[]
# cube=[]
# n=int(input("enter the no of elements in the list:"))
# for i in range(0,n+1):
#     item=(int(input("enter number:")))
#     l1.append(item)
#     square.append(item**2)
#     cube.append(item**3)
# print(l1)    
# print(square)    
# print(cube)  

#method2
l1=[]
square=[]
cube=[]
n=int(input("enter the no of elements in the list:"))
for i in range(0,n):
    l1.append(int(input("enter item:")))
    for x in l1:
        square.append(x**2)
        cube.append(x**3)
print(l1)
print(square)
print(cube)        


    

