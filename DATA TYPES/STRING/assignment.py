# reverse the words in the given string
# str='welcome to python django'
# #o/p django python to welcome
# l=str.split()
# a=l[::-1]
# str=" ".join(a)
# print(str)


# check if a string has atleast one alphabet and one number

str1=input("enter your string:")
letter=False
number=False
for i in str1:
    if i.isalpha():
        letter=True
    if i.isdigit():
        number=True
print('result is',letter and number)               
