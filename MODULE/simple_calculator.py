# program make simple calculator using function
n=int(input("enter your choice:1.add,2.sub,3.mul,4.div,5.mod: "))

if n==1:
    x=int(input("enter a number: "))
    y=int(input("enter a number: "))
    def add(a,b):
        print(f'{x}+{y}={a+b}')
    add(x,y)
elif n==2:
    x=int(input("enter a number: "))
    y=int(input("enter a number: "))
    def sub(a,b):
        print(f'{x}-{y}={a-b}')
    sub(x,y)
elif n==3:
    x=int(input("enter a number: "))
    y=int(input("enter a number: "))
    def mul(a,b):
        print(f'{x}*{y}={a*b}')
    mul(x,y)
elif n==4:
    x=int(input("enter a number: "))
    y=int(input("enter a number: "))
    def div(a,b):
        print(f'{x}/{y}={a/b}')
    div(x,y)
elif n==5:
    x=int(input("enter a number: "))
    y=int(input("enter a number: "))
    def mod(a,b):
        print(f'{x}%{y}={a%b}')
    mod(x,y)
else:
    print(("enter a valid choice"))