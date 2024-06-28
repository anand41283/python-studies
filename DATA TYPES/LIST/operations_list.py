# Length of list (no of items in list)
#-------------------------------------
# example

# l1=[1,2,3,4,5]
# l2=["auto","car","bike"]
# print(len(l1))
# print(len(l2))

# repetition(*)
#--------------

# l3=[1,2,3,4,5]
# l=l3*2
# print(l)# will print elements of l3 2 times in a single list


# Equality (==)
#--------------

# check 2 lists are similar or equal

# l4=["apple","blue",1,2,63.2,"red","yellow"]
# l5=["apple","blue",1,63.2,"red","yellow",2]
# l6=["apple","blue",1,2,63.2,"red","yellow"]

# print(l4==l5) # False---> order of elements changed(same value/elements but different order)
# print(l4==l6)




# update a value
# --------------
#  syntax:
#    list_var[index] = update value

# l6=["apple","blue",1,2,63.2,"red","yellow"]
# l6[1] = "green"
# print(l6)



# Print the sum of elements in the list

li=[34,45,65,36,78,56]
# sum=0
# for i in li:
#     sum+=i
# print(sum)

sum=0
i=0
length=len(li)
while(i<length):
    sum+=li[i]
    i+=1
print(sum)    
