"""
Tuple
---------
--->it is used to store multiple values in a single variable
--->written in rounded brackets()
--->features
    ->Tuples are immutable that means their elements can not be changed after they are generated.
    ->Tuples are orderd(Each element in tuples has a specific order that will never change)
    ->allow duplicates
--->syntax
    tuple_var=(tuple_item1,tuple_item2,tuple_item3,tuple_item4) 
         
 """
# tuple1=(1,2,3,4) #tuple contains integer type values
# tuple2=("ammu","arun","sanviya","emeric","saam")#tuple contains string type values
# tuple3=("bus","green",1,2,6.3,45,5.2)#tuple contains mixed type of values

# print(tuple1)
# print(tuple2)
# print(tuple3)
# print(type(tuple1))
# print(type(tuple2))
# print(type(tuple3))

#Triple pressing: parentheses are not necessary for the construction of multiples(tuples)

# tu=1,2,3,4
# print(tu)
# print(type(tu))


#create tuple with one item

# tup=("bus")
# print(type(tup))
# tup1=("bus",)
# print(type(tup1))

#without parenthesis

# tup="bus"
# print(type(tup))

# tup1="bus",
# print(type(tup1))

"""
len()
---> used to find the no of elements in the tuple
---> syntax:
         len(tuple_var)

"""

# t=(1,2,3,4)
# print(len(t))

"""
Accessing tuple elements
------------------------

1.Indexing

--> you can access tuple items by referring to the index number,inside square brackets
--> syntax: tuple_var[index]
--> index value starts at 0 by default

2.Negative indexing

--> python sequence objects support negative indexing
--> it starts from last item
--> -1,-2,-3....

3.Slicing

--> to gain access to various tuple elements,we can use the slicing operator colon(:)
--> syntax: tuple_var[start:stop:step]
--> these values are optional


"""
# example of indexing

# tuple1=('asha','namitha','neelima','shobhika','nidhina')#tuple contains 5 elements
# print(tuple1[3]) #o/p shobhika

#example of negative indexing
# tuple2=('asha','namitha','neelima','shobhika','nidhina')#tuple contains 5 elements
# print(tuple2[-1]) #o/p nidhina
# print(tuple2[-2]) #o/p shobhika

#example of slicing

# print(tuple2[:])
# print(tuple2[2:])
# print(tuple2[:3])
# print(tuple2[1:3])
# print(tuple2[1::2])

#4.Deleting a tuple
# tupl=(1,2,3,4,5)
# del tupl
# print(tupl) 
# converting tuple to list
#tu=('ammu','unni','black','ami','sreedhu')
# using list()
# x=list(tu)
# print(x)

# tu=tuple(x)
# print(tu)
