#1.program to multiply all the elements in the list
# list1=[20,2,1,4]
list1=[]
num=int(input("enter the no of elements in the list:"))
for x in range(0,num):
    list1.append(int(input('enter element:')))

mul=1
for i in list1:
    mul*=i
print(mul)  


#method2
# list1=[20,2,1,4]
# mul=1
# i=0
# while(i<len(list1)):
#     mul*=list1[i]
#     i+=1
# print(mul)    

