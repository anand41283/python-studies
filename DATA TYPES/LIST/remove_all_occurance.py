# program to remove all occurance of a given element from a list

# l1=[1,1,2,3,4,1,5,1,6]
# l2=[]
# re=int(input("enter item to be removed:"))
# for i in l1:
#     if(i!=re):
#         l2.append(i)
# print(l2)  
l1=[1,1,2,3,4,1,5,1,6]
re=int(input("enter item to be removed:"))
for i in l1[:]:
    if(i==re):
        l1.remove(i)
print(l1)        

