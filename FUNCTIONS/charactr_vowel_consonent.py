#create a function entered character is vowel or consonants
def vowel_con(c):
    if c.lower() in 'aeiou':
        return "vowel"
    else:
        return "consonant"
char=input("enter a character: ")
print(vowel_con(char))