#Adding elements to blank list

# li=[]
# n=int(input("enter no of elements to be added in the list:"))
# for i in range(0,n+1):
#     item=eval(input("enter items to be added:")) #li.append(input("enter item:"))
#     li.append(item)
# print(li)  

# n=[10,0,-1,7]
# nm=["jenny","kk","ll"]
# print(n+nm)


#list slicing

# l1=[10,0,-1,7,8,-67]
# # print(l1[0::2])
# # l1.append(100)
# # print(l1)

# l1.insert(3,12)
# print(l1)


# l1=[]

# n=int(input("enter the length of list"))
# for i in range(n):
#     l1.append(input("enter the values"))
#     print(l1)


# # decending
# l1=[1,2,90,444,-5,-66]
# l1.sort(reverse=True)
# print(l1)


#elimijnate duplicates from a list

l1=["blue","blue","red","bus",1,1,2]
# l2=[]
# for i in l1:  # for loop
#     if i not in l2:
#         l2.append(i)
# print(l2)

l1=set(l1)
l1=list(l1)

print(l1)





