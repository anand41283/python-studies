"""
Methods used in python dictionary
---------------------------------

1.fromkeys()
------------
Returns a dictionary with the specified keys and values.
Python dictionary method fromkeys() creats a new dictionary with keys from sequence and values set to val
syntax:
dict.fromkeys(seq,value)
seq---> This is the list of values which would be used to for dictionary keys preparation.
value---> This is optional,if provided then value would be set to this value

"""
# seq=("name","age","sex")
# di=dict.fromkeys(seq)
# print("the dictionary : ",str(di))

# dict=dict.fromkeys(seq,20)
# print("new dictionary: ",str(dict))

#2.setdefault()
# #--------------
# Returns the value of the specified key.If the key does not exist  insert the key with the specified Value
# syntax:
# dict.setdefault(key,default=None)

# dict={"name":"zara","age":26}
# print(dict.setdefault("name",None)) #o/p zara
# print(dict.setdefault("sex",None)) #o/p none

#popitem()
#Returns the last inserted key-value pair

# dict={"name":"zara","age":24,"sex":"female"}
# print(dict)
# dict.popitem()
# print(dict)

