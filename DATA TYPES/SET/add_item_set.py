"""
Add item
--------
1. add()
2. update()
add()
to add one item to a set use add() method
syntax:
    set_var.add(item)
"""
s2={"bus","car","train"}
print(s2)
s2.add("bike")
print(s2)

# update()
# add multiple elements to the set 
# To add items from another set into the current set use update() method

s3={"apple","mango"}
s4={"kiwi","jack fruit"}
print(s3)
print(s4)
s3.update(s4)
print(s3)