"""
SET
---
---> It is a datatype.
---> used to store multiple values in a single variable
---> It is enclosed in {}
---> do not allow duplicates (sets remove duplicate elements)
---> sets are mutable which means we can modify it after creation
---> unordered item(each element is unique)
---> no index attached to the elements of the set
---> we can't directly access any element of the set by index
---> you can loop through the set items using a 'for' loop
---> a specified value is present in a set by using 'in' keyword
---> set() used to convert list/tuple into set
---> set contains any type of elements such as integer,float,tuple(immutable types).but mutable elements such as list,dictionary,set can't be member of set

"""
# s={1,2,3,1,3}
# print(s)
# color={"red","green","blue"}
# print(color)
# print(type(color))
# print("each element in the set using for loop ")
# for i in color:
#     print(i)

#using set()

# color=set(["yellow","white","black"])    
# print(color)
# print(type(color))
# print("each element in the set using for loop ")
# for i in color:
#     print(i)

# set1={1,2,2.3,"helo",("king","queen")}
# print(set1)
# set2={24,26,35,2.3,[1,2,3]}
# print(set2) # error becasue list can't be a member of set

"""creating empty set
---> It is a bit different because empty curly braces {} are also used to create DICTIONARY as well
---> So python provides set() method (without parameter) to create empty set
"""
# set3={}
# print(type(set3)) # dictionary

# set4=set()
# print(type(set4))

# duplicates not allowed

# s1={2,3,4,5,5,2,3}
# print(s1)

# # get length of a set
# using len()
# print(len(s1))

# change items
# ------------
#-> once you created a set  ,you can't change its items but you can add new item

#print(type(True))
# s5={0,1,2,3,True,False}
# print(s5)

# True and 1
# The values True and 1 (0 and False) are considered the same value in sets and are treated as duplicates
# s={2,3,41,True,False,0,1}
# print(s)

