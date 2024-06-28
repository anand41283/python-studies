# full pyramid

rows=int(input("enter the number of rows:"))
for row in range(rows+1):
    for space in range(rows-row):
        print("",end=" ")
    for column in range(row):
        print("*",end="  ")

    print()
