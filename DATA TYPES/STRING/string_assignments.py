#1.Check  given character is alphabet or digit or special symbol
# check=input('enter your character:')
# if check.isalpha():
#     print('character is alphabet')
# elif check.isdigit():
#     print('character is digit')
# else:
#     print('character is special symbol')

#2.print a to z alphabet in uppercase using for loop
# for i in range(97,123):
#     print(chr(i).upper())

#3.Print A to Z using for loop
# for i in range(65,91):
#     print(chr(i).lower())

#4.count the no of alphabets,digits,and special symbols in a sentence
# alpha=[]
# dig=[]
# spl=[]
# a=input('enter sentence')
# for i in a:
#     if i.isalpha():
#         alpha.append(i)
#     elif i.isdigit():
#         dig.append(i)
#     else:
#         spl.append(i)
# print('count of alphabets',len(alpha))            
# print('count of digits',len(dig))            
# print('count of special symbol',len(spl))   
#simpler method
# alpha=0
# dig=0
# spl=0
# a=input('enter sentence')
# for i in a:
#     if i.isalpha():
#         alpha+=1
#     elif i.isdigit():
#         dig+=1
#     else:
#         spl+=1
# print('count of alphabets',alpha)            
# print('count of digits',dig)            
# print('count of special symbol',spl)          

#5.write a program to check if the given letter is present or not in the word
# word=input('enter the word')
# letter=input('enter the letter to be checked:')
# if letter in word:
#     print('letter is present')
# else:
#     print('letter is not present')


#6.write a program to find the length of the string with out using len function
# alpha=0
# dig=0
# spl=0
# a=input('enter sentence')
# for i in a:
#     if i.isalpha():
#         alpha+=1
#     elif i.isdigit():
#         dig+=1
#     else:
#         spl+=1
# print('length of sentance',(alpha+dig+spl))            




#7.print even length words of string
# str=input('enter your string: ')
# li=str.split()
# print(li)
# for i in li:
#     if (len(i)%2==0):
#         print(i)

#8.count vowels in a string
# word=input('enter the word')
# vowel=0
# for i in word:
#     if i.lower() in 'aeiou':#['a','e','i','o','u']:
#         vowel+=1
# print('count of vowels:',vowel)

#9.write a program to remove duplicates in a string
# str=input('enter your string: ')
# li=[]
# for i in str:
#     if i not in li:
#         li.append(i)
# print((' '.join(li))) 

#10.write a program to convert lower letter to upper and upper letter to lower in a string
# str=input('enter your string:')
# print(str.swapcase())       

#11.write a prgrm to sort letters of word by lower to uppecase format
# str=input('enter your string:')
# li=list(str)
# li.sort(reverse=True)
# str="".join(li)
# print(str)

#12.write a progrm in python to count lower,upper,numeric and special characters in a string
# str=input('enter your string:')
# low=0
# upp=0
# num=0
# spl=0
# for i in str:
#     if i.islower():
#         low+=1
#     elif i.isupper():
#         upp+=1
#     elif i.isnumeric():
#         num+=1
#     else:
#         spl+=1        
# print("count of lower:",low)
# print("count of upper:",upp)
# print("count of numeric:",num)
# print("count of special:",spl)
