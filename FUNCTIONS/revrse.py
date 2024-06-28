#create a function 'reverse' with a parameter and that returns its reverse
def reverse(n):
    rev=0
    while n>0:
        dig=n%10
        rev=(rev*10)+dig
        n//=10
    return rev    

    
s=int(input("enter string: "))
print(reverse(s))