"""
Special sequences
-----------------

A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

Character	    Description	

1. \A	            Returns a match if the specified characters are at the beginning of the string	
2. \b	            Returns a match where the specified characters are at the beginning or at the end of a word
               
                                                                                                                    	
3. \B	           Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
	           
4. \d	           Returns a match where the string contains digits (numbers from 0-9)
5. \D	           Returns a match where the string DOES NOT contain digits		
6. \s	           Returns a match where the string contains a white space character	
7. \S	           Returns a match where the string DOES NOT contain a white space character
8. \w	           Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	
9. \W	           Returns a match where the string DOES NOT contain any word characters	
10. \Z	           Returns a match if the specified characters are at the end of the string	


"""
#1.

# import re

# txt = "The rain in Spain"

# #Check if the string starts with "The":

# x = re.findall("\AThe", txt)

# print(x)

# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")



#2.
# import re

# txt = "The rain in Spain"

# #Check if "ain" is present at the beginning of a WORD:

# x = re.findall(r"\bain", txt) #(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain" r"ain\b"

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# import re

# txt = "The rain in Spain"

# #Check if "ain" is present at the end of a WORD:

# x = re.findall(r"ain\b", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")


#3.

# import re

# txt = "The rain in Spain"

# #Check if "ain" is present, but NOT at the beginning of a word:

# x = re.findall(r"\Bain", txt) #(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain" r"ain\B"


# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# import re

# txt = "The rain in Spain"

# #Check if "ain" is present, but NOT at the end of a word:

# x = re.findall(r"ain\B", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")


#4.
# import re

# txt = "The rain in Spain"

# #Check if the string contains any digits (numbers from 0-9):

# x = re.findall("\d", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

#5.
# import re

# txt = "The rain in Spain"

# #Return a match at every no-digit character:

# x = re.findall("\D", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")


# 6.
# import re

# txt = "The rain in Spain"

# #Return a match at every white-space character:

# x = re.findall("\s", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")


# 7.
# import re

# txt = "The rain in Spain"

# #Return a match at every NON white-space character:

# x = re.findall("\S", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")


# 8.
# import re

# txt = "The rain in Spain"

# #Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

# x = re.findall("\w", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")


# 9.
# import re

# txt = "The rain in Spain"

# #Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

# x = re.findall("\W", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")


# 10.
# import re

# txt = "The rain in Spain"

# #Check if the string ends with "Spain":

# x = re.findall("Spain\Z", txt)

# print(x)

# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")

