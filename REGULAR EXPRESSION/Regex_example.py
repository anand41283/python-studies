# import re
# n = "hello"
# k = re.search("^h",n)  # ^ :starts with a character
# if k:
#     print("yes")
# else:
#     print("no")


# k = "hello"
# n = re.findall("^h.*o",k)
# print(n)

# n = re.findall("^[0123]",k)
# print(n)



# PAN CARD
# import re
# pan_number = input("Enter your pan number: ")
# k = re.compile(r'^[A-Z]{5}[0-9]{4}[A-Z]$')
# if k.match(pan_number):
#     print("Pan number succeeded")
# else:
#     print("not a pan number")

# import re
# lst = ["ASDFG4356M","qwerty1234a","12345qwertN","AAaas32422"]
# k = re.compile(r'^[A-Z]{5}[0-9]{4}[A-Z]$')
# for i in lst:
#     if k.match(i):
#         f=open("new.txt","a")
#         f.write(i)
#         f.close()
#     #     print("valid")
        
#     else:
#         print("invalid")



# l = "ABEABEAAABBC"
# d = {l.count(i):i for i in l}
# print(d)
# print(max(d.keys()))
# k = d.get(max(d.keys()))
# print(k)




s ="AJHABSBAIBCCSBAAA"
lst=list(s)
d={}
for i in lst:
    if i.upper() not in ['A','E','I','O','U']:
        if i in d:
            d[i]+=1
        else:
            d[i]=1


