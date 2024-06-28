# color={"green","red","white"}
# # write a program to add "blue" to the set color

# color.add("blue")
# print(color)

# # Find the length of the set color

# print(len(color))

# # add "black","yellow","pink" to the set

# adds={"balck","yellow","pink"}
# color.update(adds)
# print(color)

# # create an empty set

# emset=set()
# print(type(emset))

# # add 3,4,5,6,7,4,5,10 to the set {1,2,21,3,1,True}

# s1={1,2,21,3,1,True}
# s2= {3,4,5,6,7,4,5,10}
# s1.update(s2)
# print(s1)

# The object in the update() method does not have to be a set,it can be iterable
# object (tuple,list,dictionary)

s2={"apple","grapes"}
s3=["jackfruit","orange"]
s4=(1,2,3)
print(s2)
print(s3)
print(s4)
s2.update(s3)
print(s2)
s2.update(s4)
print(s2)