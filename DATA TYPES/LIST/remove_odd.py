#print program to removing odd numbers from a list
# l1=[1,2,3,4,5,46,31,56,55]
# l2=[]
# for i in l1:
#     if(i%2==0):
#         l2.append(i)
# print(l2)

l1=[1,2,3,4,5,46,31,56,55]
for i in l1[:]:
    if(i%2!=0):
        l1.remove(i)
print(l1)        