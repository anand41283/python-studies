"""
sets
----
A set is a set of characters inside a pair of square brackets [] with a special meaning:

Set	        Description

1.[arn]	     Returns a match where one of the specified characters (a, r, or n) is present	
2.[a-n]	     Returns a match for any lower case character, alphabetically between a and n	
3.[^arn]	     Returns a match for any character EXCEPT a, r, and n	
4.[0123]	     Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
5.[0-9]	     Returns a match for any digit between 0 and 9	
6.[0-5][0-9]	 Returns a match for any two-digit numbers from 00 and 59	
7.[a-zA-Z]	 Returns a match for any character alphabetically between a and z, lower case OR upper case	
8.[+]	         In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string	


"""
# 1.
# import re

# txt = "The rain in Spain"

# #Check if the string has any a, r, or n characters:

# x = re.findall("[arn]", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")


# 2.
# import re

# txt = "The rain in Spain"

# #Check if the string has any characters between a and n:

# x = re.findall("[a-n]", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")


# 3.
# import re

# txt = "The rain in Spain"

# #Check if the string has other characters than a, r, or n:

# x = re.findall("[^arn]", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# 4.
# import re

# txt = "The rain in Spain"

# #Check if the string has any 0, 1, 2, or 3 digits:

# x = re.findall("[0123]", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")


# 5.
# import re

# txt = "8 times before 11:45 AM"

# #Check if the string has any digits:

# x = re.findall("[0-9]", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")


# 6.
# import re

# txt = "8 times before 11:45 AM"

# #Check if the string has any two-digit numbers, from 00 to 59:

# x = re.findall("[0-5][0-9]", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# 7.
# import re

# txt = "8 times before 11:45 AM"

# #Check if the string has any characters from a to z lower case, and A to Z upper case:

# x = re.findall("[a-zA-Z]", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# 8.
# import re

# txt = "8 times before 11:45 AM"

# #Check if the string has any + characters:

# x = re.findall("[+]", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")