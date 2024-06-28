"""

A dictionary is an unordered collection of key-value pairs. Each entry has a key and value. A dictionary can be considered as a list with special index.

The keys must be unique and immutable. So we can use strings, numbers (int or float), or tuples as keys. Values can be of any type

"""

words = ['data', 'science', 'machine', 'learning']
#list comprehension
[len(i) for i in words]
[4, 7, 7, 8]
#dictionary comprehension
{i:len(i) for i in words}
{'data': 4, 'science': 7, 'machine': 7, 'learning': 8}

# {1:1,2:4,3:9.......}
x={i:i**2 for i in range(1,11)}
print(x)