"""
Remove set items
----------------
1.remove()
2.discard()

1.remove()
    remove() function is used to remove a item from the set 
    syntax:
    set_var.remove(item)
"""

# s3={1,2,3,5.6,7,10}
# print(s3)
# s3.remove(5.6)
# print(s3)
# s3.remove(4)
# print(s3) # error since item is not present in set

# 2.discard()
# discard() function is used to remove a item from the set 
    # syntax:
    # set_var.discard(item)
# discard() function doesn't throw an error while the element to be removed is not in the set

# s3={1,2,3,5.6,7,10}
# print(s3)
# s3.discard(5.6)
# print(s3)
# s3.discard(4)   # do not throw an error if the item is not present in the set...instead of return the same set
# print(s3)

# clear()
# empties the set
#syntax: set_var.clear()

# se={1,2,3}
# se.clear()
# print(se)
# print(type(se))


# del keyword
# delete the set completely

# syntax: del set_var

# se={1,2,3}
# del se
# print(se)

#pop()
# removes a random element from the set
# syntax: set_var.pop()

# s1=se={1,2,3,4,5}
# s1.pop()
# print(s1)
