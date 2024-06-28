#1.pop()
#The pop() method removes the item with the specified key name

product={"name":"soap","weight":200,"colour":("red","green")}
# product.pop("colour")
print(product)

#2.del
#The del keyword removes the item with the specified key name

# del product["weight"]
# print(product)
#The del keyword can also delete the dictionary completely
# del product
# print(product) 

#3.clear()
#The clear() method empties the dictionary
product.clear()
print(product)  