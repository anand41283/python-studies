"""
while loop
executes a block of codes as long as condition is true

syntax:

initialization
while(condition):
    stmnts
    increment/decrement


"""
#example of while loop

# i=0
# while(i<=6):
#     print(i)
#     i+=1
# print("numbers between 0-5")    

# break in while loop

i=0
while(i<=6):
    if (i==3):
        break
    print(i)
    i+=1

#continue in while loop

i=0
while(i<=6):
    i+=1
    if(i==3):
        continue
    print(i)
    



