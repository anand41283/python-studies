def diff(n1,n2):
    if n1>n2:

        return(n1-n2)
    else:
        return(n2-n1)
x=int(input("enter a number: "))
y=int(input("enter a number: "))
print(diff(x,y))