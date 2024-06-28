
def vowel(a):
    count=0
    for i in a:
        if i.lower() in 'aeiou':
            count+=1
    return count
print(vowel(input("enter your string: ")))
