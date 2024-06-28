"""
LIST COMPREHENSION
-------------------
It offers a shorter syntax for looping through list when you want to create a new list based on the values of an existing list

syntax ---->
   new_list=[expression for item in iterable if condition==True] """

# find square of elements in the list(1-10)
# l1=[1,2,3,4,5,6,7,8,9,10]
# l2=[]
# for i in l1:
#     l2.append(i**2)
# print(l2)    
# # or 
# # using L.C
# l1=[1,2,3,4,5,6,7,8,9,10]
# print([x**2 for x in l1])
# # print characters in name 
# name=input("enter your name:")
# print([i for i in name])

# create a list with fruits and create another list that contains fruits ==apple


# l2=['apple','banana','kiwi','orange']
# print([i for i in l2 if i=='apple'])


# given a list of numbers,remove float values using lc
# l1=[1,2,3,4.5,6,7,89.0,20.1]
# #op=[1,2,3,6,7]
# print([x for x in l1 if type(x)==int])

# find all of the numbers from 1-1000 that are divisible by 7
# print([i for i in range(1,1001) if i%7==0])

#count the no of spaces in a string
# a="tom is a good cricket player"
# space=[x for x in a if x==' ']
# print(len(space))

# find common numbers in the two list
# a=[1,2,3]
# b=[2,3,4,5]
# print([x for x in a if x in b])

