rows=int(input("enter number of rows:"))
ascii_value=65
for i in range(rows):
    for j in range(i+1):
        print(chr(ascii_value),end=" ")
    ascii_value+=1
    print('\n')