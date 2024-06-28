"""Create a module that defines some functions like
1.print your name
2.perform arithmatic operators
3.count the vowels and consonants in the string
4.print 1 to 10 numbers
5.print special characters in the given string
and perform each functions in another file mod.py

"""
def print_name(s):
    print(s)
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def div(a,b):
    print(a/b)
def mul(a,b):
    print(a*b)
def mod(a,b):
    print(a%b)
def exp(a,b):
    print(a**b)
def fl_div(a,b):
    print(a//b)

def vow_cons(s):
    count_v=0
    count_c=0
    for i in s:
        if i.lower() in 'aeiou':
            count_v+=1
        else:
            count_c+=1
    print('count of vowel: ',count_v)        
    print('count of consonant: ',count_c)      

def one_ten():
    for i in range(1,11):
        print(i)

def special(s):
    for i in s:
        if (i.isalnum()):
            pass
        else:
            print(i)

