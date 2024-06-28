"""STRING
   ------
   String is the collection of the characters surrounded by single quotes or double quotes or triple quotes
   'hello'
   "python"
   --->print a string
   print("students")
   --->assign a value into variable
   a="file"
   print(a)

"""

# abc="""hi students how are you
#     hvqqdggdwhd;
#     hbddndcbhdvhes;;""" # multi line string
# print(abc)
# print(type(abc))

"""Indexing and splitting
   ----------------------
   -> the index of string starts from 0
   -> accessing individual character from string using [] #(slice operator)
   -> : operator to access substring from the given string
   -> negative indexing(-1,-2,-3...) starts from endd of the string
 """
# str1="python"

# #p y t h o n
# #0 1 2 3 4 5

# print(str1[0])
# print(str1[1])
# print(str1[2])
# print(str1[3])
# print(str1[4])
# print(str1[5])

# # print substring of python
# print(str1[2:])
# print(str1[1:3])


#Q1.
# py='welcome to python django'
# # print first character
# print(py[0])

# #print last character
# print(py[-1])

# #print second last character
# print(py[-2])

# #create a substring "python django"
# print(py[11:])

# #create a substring starting value  'c'
# print(py[3:])

# #create a string in reverse order
# print(py[::-1])

# #create a substrin endvalue='j'
# print(py[:20])

# print("hello \nworld")
print("python{}".format(" rules!"))