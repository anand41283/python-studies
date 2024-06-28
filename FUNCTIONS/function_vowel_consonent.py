def vowel_consoent(a):
    count_v=0
    count_c=0
    for i in a:
        if i in 'aeiou':
            count_v+=1
        else:
            count_c+=1
    return("vowel",count_v,"consonent",count_c)
       
print(vowel_consoent(input("enter your string: ")))