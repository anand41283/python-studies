#create a function that accept a number from user and returns its factorial
#5!=5*4*3*2*1=120

def fact(n1):
    fact=1
    for x in range(1,n1+1):
        fact*=x
    return(fact)
print(fact(int(input("enter a number: "))))
