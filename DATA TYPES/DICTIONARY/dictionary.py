"""
DICTIONARY
----------
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered,changeable,and do not allow duplicates.
--> This data structure is mutable
--> The components of dictionary were made using keys and values.
--> keys must only have one component.
--> values can be of any type,including integer,list and tuple.
Dictionary entries are ordered as of python version 3.7. In python 3.6 and before,dictionaries are generally unordered.

Creating the Dictionary
-----------------------
Curly brackets are the simplest way to generate a python dictionary,although there are other approaches as well.With many
key-value pairs surrounded in curly brackets and a colon seperating each key from its value,the dictionary can be built (:).
syntax:

dict_var={key:value,key:value}
The empty curly braces {} is used to create empty dictionary

"""
# di={"name":"asha","age":29,32:'mani'}
# print(di)
# #creating an empty dictionary
# Dict={}
# print("empty dictionary:")
# print(Dict)

#Creating a dictionary
#with dict method
# Dct=dict({1:"html",2:"css",3:"bootstrap"})
# print("\nCreate Dictionary by using dict():")
# print(Dct)

#Dictionary length 
#To determine how many items a dictionary has ,use the len() function:
employee={"name":"arun","age":24,"company":"federal bank"}
# print(len(employee))

#Datatype
#find the datatype od dict using type()
print(type(employee))