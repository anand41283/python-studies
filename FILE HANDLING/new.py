l_count = 0
u_count = 0
file = open("hello.txt")
k = file.read()
for i in k:
    if i.isupper():
        u_count+=1

    elif i.islower():
        l_count+=1
print("Uppercase letters count: ",u_count)
print("Lowercase letters count: ",l_count)
