"""
python has a set of built-in methods that you can use on strings

1.upper()
 returns the string in upper case
2.lower()
 returns the string in lower case
3.strip()
 removes any whitespaces from the beginning or end
 syntax: str_var.strip()
4.replace()
 replace a string with another string
 syntax: str_var.replace("character","replace_character")
5.split()
 return a list where the text b/w the seperator becomes the list items
 syntax: str_var.split(",")
6.join()
 join all items in a tuple/list into a string
 syntax: string.join(tuple/list) 

"""
# a="anjitha"
# print(a.upper())

# b="AMMU"
# print(b.lower())

# w=" hello world "
# print(len(w))
# print(w.strip())
# print(len(w.strip()))

# s1="manu"
# print(s1.replace('m','j'))

# a1="anjitha t v"
# print(a1.split(" "))

# l1=['balck','is','my','favorite','colour']
# print(" ".join(l1))

# #1.convert string into uppercase half string
# s='pythondjango' #o/p pythonDJANGO
# a=(s[:6]+s[6:].upper())
# print(a)
#method2
# s='pythondjango'
# half_ind=len(s)//2
# res=''
# for i in range(len(s)):
#     if i>=half_ind:
#         res+=s[i].upper()
#     else:
#         res+=s[i]
# print(res)       

#2.capitalize first and last character of each word in a string
st="welcome to ooty" #o/p "WelcomE TO OotY"
l=st.split()
l2=[]
for i  in l:
    x=i[0].upper()+i[1:-1]+i[-1].upper()
    l2.append(x)
print(l2)
r=" ".join(l2)    
print(r)




