"""
Accessing items
---------------
You can access the items of a dictionary by referring to its key name,inside square brackets
syntax:
dict_var[key]

"""
employee={"name":"manu","age":25,"company":"abc"}
print(employee)
#1.Accessing item using keys

# print(employee["name"])
# print(employee["age"])
# print(employee["company"])

#2.Using get() method

# print(employee.get("name"))
# print(employee.get("company"))
# print(employee.get("age"))

#get key
#The keys() method will return a list of all the keys in the dictionary.

# print(employee.keys()) #o/p dict_keys(['name', 'age', 'company'])

#get values
#The values() method will return a list of all the values in the dictionary.

# print(employee.values()) #o/p dict_values(['manu', 25, 'abc'])

#get items
#The items() method will return each item in a dictionary,as tuples in a list

# print(employee.items()) #o/p dict_items([('name', 'manu'), ('age', 25), ('company', 'abc')])

#Check if key exists
#To determine if a specified key is present in a dictionary use the "in" keyword:
# if "name" in employee:
#     print("present")
# else:
#     print("not present")

#change values
#You can change the value of a specific item by referring to its keyname:
# print(employee)
# employee["name"]="anu"
# print("after change")
# print(employee)
"""
{'name': 'manu', 'age': 25, 'company': 'abc'}
after change
{'name': 'anu', 'age': 25, 'company': 'abc'}

"""

#Update dictionary
#The update() method will update the dictionary with the item from the given argument.
#The argument must be a dictionary,or an iterable object with key:value pairs.

employee.update({"company":"moto"})
print(employee)  #o/p {'name': 'manu', 'age': 25, 'company': 'moto'}

#If the item does not exist,the item will be added.

employee.update({"location":"kochi"})
print(employee)


