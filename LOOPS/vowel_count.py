string=input("enter a string:")
v_count=0
c_count=0
for i in string:
    if i in "aeiouAEIOU":
        v_count+=1
    else:
        c_count+=1
print("number of vowels in that string is ",v_count)       
print("number of consonants in that string is ",c_count)       
