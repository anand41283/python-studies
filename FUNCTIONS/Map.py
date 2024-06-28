"""
map function accepts another function and a sequence of ‘iterables’ as parameters
and provides output after applying the function to each iterable in the sequence.

"""

# items=[1,2,3,4]
# sqr=[i**2 for i in items]
#sqr=[i**2 for i in range(1,5)]
# print(sqr)
#items=[1,2,3,4]
# sqr=list(map(lambda x : x**2,items))
# print(sqr)

# items=[1,2,3,4]
# sqr=list(map(lambda x : x+x,items))
# print(sqr)



# numbers1=[1,2,3]
# numbers2=[4,5,6]
# result= map(lambda x,y:x*y,numbers1,numbers2)
# #print(type(result))
# print(list(result))

# Write a Python program to triple all numbers in a given list of integers. Use Python map

numbers=[11,32,24,65,50]
triple=list(map(lambda x:3*x,numbers))
print(triple)


