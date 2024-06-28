"""
REGULAR EXPRESSION
------------------
--> A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

--> RegEx can be used to check if a string contains the specified search pattern.

--> Python has a built-in package called re, which can be used to work with Regular Expressions.
--> The re module offers a set of functions that allows us to search a string for a match:
        Function	Description
        findall	    Returns a list containing all matches
        search	    Returns a Match object if there is a match anywhere in the string
        split	    Returns a list where the string has been split at each match
        sub	        Replaces one or many matches with a string
META CHARACTERS
---------------
Metacharacters are characters with a special meaning:

Character	     Description	

1. []	            A set of characters	
2. \	            Signals a special sequence (can also be used to escape special characters)		
3. .	            Any character (except newline character)	
4. ^	            Starts with		
5. $ *	            Ends with	
6. *	            Zero or more occurrences	
7. +	            One or more occurrences	
8. ?	            Zero or one occurrences	
9. {}	            Exactly the specified number of occurrences		
10. |	            Either or		
11. ()	            Capture and group	 	 





"""
#1.
# import re

# txt = "The rain in Spain"

# #Find all lower case characters alphabetically between "a" and "m":

# x = re.findall("[a-m]", txt)
# print(x)

#2.
# import re

# txt = "That will be 59 dollars"

# #Find all digit characters:

# x = re.findall("\d", txt)
# print(x)

#3.
# import re

# txt = "hello planet"

# #Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

# x = re.findall("he..o", txt)
# print(x)



#4.
# import re

# txt = "hello planet"

# #Check if the string starts with 'hello':

# x = re.findall("^hello", txt)
# if x:
#   print("Yes, the string starts with 'hello'")
# else:
#   print("No match")



#5.
# import re

# txt = "hello planet"

# #Check if the string ends with 'planet':

# x = re.findall("planet$", txt)
# if x:
#   print("Yes, the string ends with 'planet'")
# else:
#   print("No match")



#6.
# import re

# txt = "hello planet"

# #Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

# x = re.findall("he.*o", txt)

# print(x)




#7.
# import re

# txt = "hello planet"

# #Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

# x = re.findall("he.+o", txt)

# print(x)




#8.
# import re

# txt = "hello planet"

# #Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

# x = re.findall("he.{2}o", txt)

# print(x)




#9.
# import re

# txt = "The rain in Spain falls mainly in the plain!"

# #Check if the string contains either "falls" or "stays":

# x = re.findall("falls|stays", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")


