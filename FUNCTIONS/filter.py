# Filter
# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not. 

# numbers=[-3,-6,-5,2,5,6,-2]
# less_than_zero=list(filter(lambda x:x<0,numbers)) # we can also convert into tuple
# print(less_than_zero)


# to filter even numbers

# nums=[1,2,3,4,5,6,7,8,9]
# even=list(filter(lambda x:x%2==0,nums))
# print(even)


# Using filter() and list() functions and .lower() method filter all the vowels in a given string.
str1="Winter Olympics in 2022 will take place in Beijing China"







words = ["apple","banana","grapes","cherry","pineapple","kiwi"]
def values(a):
    #print(a)

    return len(a)>5

#print(values(words))

five_letters=list(filter(values,words))
print(five_letters)

# five_letters=list(filter(lambda x:len(x)>5,words))
# print(five_letters)


# words = ["apple","","banana","grapes","","cherry","","pineapple"]

# non_empty=list(filter(lambda x:x!="",words))
# print(non_empty)


# def values(w):
#     return len(w)>0

# non_empty=list(filter(values,words))
# print(non_empty)