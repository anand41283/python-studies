#create a function to check whether a string has all unique characters.
def unique(s):
    char=set(s)
    return len(char)==len(s)
st=input("enter your string: ")
print(unique(st))