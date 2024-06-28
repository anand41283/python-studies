#1.create a blank set and add elements(12)

# set1=set()
# for i in range(12):
#     set1.add(eval(input("enter item:")))
# print(set1)    


#2.check given element is present or not using if

# de={"blue","green","red","white",23,45,67}
# check=eval(input("enter element to be checked:"))
# if  check in de:
#     print("element is in set")
# else:
#     print("element is not in set")

#3.add a list of elements to a set
# l1=["bike","car"]
# s1={"kiwi"}
# s1.update(l1)
# print(s1)

#4.create a set(fruits) and add 8 fruits into it
# fruits=set()
# for i in range(8):
#     fruits.add(input("enter item:"))
# print(fruits)

# #method2
#fruits=set()
# s2={'apple','kiwi','banana','lichi','jackfruit','orange'}#l2=['apple','kiwi','banana','lichi','jackfruit','orange']
# fruits.update(s2)#fruits.update(l2)
# print(fruits)

#5.Return a new set of identical items from 2 sets
# s1={2,3,4,5}
# s3={8,6,4,3}
# s2=s1.intersection(s3)
# print(s2)

#6.get only unique items from two sets
# set1={10,20,30,40,50}
# set2={30,40,50,60,70}
# set1.symmetric_difference_update(set2)
# print(set1)
#method2
# set3=set1.symmetric_difference(set2)
# print(set3)


#7.update the first set with items that don't exist in the second set
# set2={10,20,30}
# set3={20,40,50}
# set2.difference_update(set3)
# print(set2)

#8.Return a set of element present in set a or b but not both

# set1={10,20,30,40,50}
# set2={30,40,50,60,70}
# set3=set1.symmetric_difference(set2)
# print(set3)

#9.check if 2 sets have any elements in common,if yes print the common element
# set1={10,20,30,40,50}
# set2={30,40,50,60,70}
# set1.intersection_update(set2)
# print(set1)
#method2
# for i in set1:
#     if i in set2:
#         print(i)

#10.update set1 by adding items from set2 except common
# set1={10,20,30,40,50}
# set2={30,40,50,60,70}
# set1.symmetric_difference_update(set2)
# print(set1)

#11.remove items from set1 that are not common to both set1 and set2
# set1={10,20,30,40,50}
# set2={30,40,50,60,70}
# set1.intersection_update(set2)
# print(set1)



#12.prgrm to check if two given sets have no elements in common
# set1={1,2,3}
# set2={4,5,6}
# if set1.isdisjoint(set2):
#     print("sets are disjoint") 

#13.prgrm to remove all elemnts from given set
# set2={1,2,3,4,5,7}
# set2.clear()
# print(set2)

#14.convert a set into list
# s1={1,2,3}
# l1=list(s1)
# print(l1)

#15.convert a set into tuple
# s1={1,2,3}
# tu=tuple(s1)
# print(tu)

#16.check if a set is a subset of itself
# s1={1,2,3}
# s2=s1.copy()
# if s1.issubset(s2):
#     print("s1 is the subset of s1")

#17.check if a set {1,2,3} is a subset of another set {1,2,3,4,5}
# s1={1,2,3}
# s2={1,2,3,4,5}
# print(s1.issubset(s2))


#18. find union,symmetric difference,and intersection of two sets.print the result of each operation
# a={1,2,3,4}
# b={3,4,5,7}
# #union
# c=a.union(b)
# print(c)

# #symmetric_difference

# d=a.symmetric_difference(b)
# print(d)

# # intersection
# e=a.intersection(b)
# print(e)




