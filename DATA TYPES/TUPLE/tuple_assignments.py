#1.create a tuple and add elements to the tuple
# a=10,12,14,15
# print(a)
# t=10,12,14,15
# a=int(input("enter the limit:"))
# l=list(t)
# for i in range(a):
#     l.append(int(input("enter number:")))
#     t=tuple(l)
# print(t)

#2.write a program to test if a variable is list or tuple or string
# a=(2,3)
# if (type(a)==tuple):
#     print(f"{a} is a tuple")
# elif(type(a)==list):   
#     print(f"{a} is a list")
# else:
#     print(f"{a} is a string")    

#3.write a program to sort the elements in the tuple alphabetically

# t='apple','orange','mango','kiwi','papaya','anar'
# print(t)
# l=list(t)
# l.sort()
# t=tuple(l)
# print(t)

#4.write a program to check if given element is present in tuple or not
# t='apple','orange','mango','kiwi','papaya','anar',1,2,3
# a=eval(input("enter the variable:"))
# if a in t:
#     print(f"{a} is in tuple")
# else:
#     print(f"{a} is not in tuple")    

#tuple_1=("blue","red","green","apple","orange",23,45,67,23.5,67.8,100,"red","red")
#5.Find the first and last element in the tuple
# tuple_1=("blue","red","green","apple","orange",23,45,67,23.5,67.8,100,"red","red")
# print(tuple_1[0])
# print(tuple_1[-1])

#6.create a subtuple from the tuple start with the value "green"
# sub=tuple_1[2:]
# print(sub)

#7.create a subtuple from the tuple end with the value 23
# sub=tuple_1[:6] #sub=tuple_1[:-7]
# print(sub)

#8.create a subtuple from the tuple start with the value "apple" and step = 3
# sub=tuple_1[3::3]
# print(sub)

#9.print the tuple using slicing
# print(tuple_1[:])

#10.find the max value of the tuple
# a=max(tuple_1)
# print(a)#error since mixed values of int and str

#11.find the min value of the tuple
# a=min(tuple_1)
# print(a)#error

#12.find the index of the value 23.5
#print(tuple_1.index(23.5))

#13.find the count of the value red
# print(tuple_1.count('red'))

#14.add the value 67,'nami','mittu',8 to that tuple
# a=int(input("enter the limit:"))
# l=list(tuple_1)
# for i in range(a):
#     l.append((input("enter item:")))
#     tuple_1=tuple(l)
# print(tuple_1)

#15.find the no of elements in the tuple
#print(len(tuple_1))

#16.print each element in the tuple
# for i in tuple_1:
#     print(i)

#17.unpack these variables into 5 variables
# a,b,c,d,*e=tuple_1
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

#18.write a program to adding a tuple to list and vice-versa

# l1=[1,2,3]
# t1=(4,5)
# # t1=list(t1)
# # print(l1+t1)
# l1=tuple(l1)
# print(t1+l1)


#19.write a program to find repeated items of a tuple
# list1=list(tuple_1)
# re=[]
# re=[i for i in list1 if ((list1.count(i)>1) and (i not in re))]
# re=tuple(re)
# print(re)
# list1=list(tuple_1)
# re=[]
# for i in list1:
#     if(list1.count(i)>1) and (i not in re):
#         re.append(i)
# re=tuple(re)
# print(re)        



#20.create a tuple with single item 23
# a=23,
# print(a)
# print(type(a))








