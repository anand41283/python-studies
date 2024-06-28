# 2.W.p to create a calculator class. include methods for arithematic operations

class Calculator:
    num1:int
    num2:int
    def __init__(self):#,num1,num2):
        self.num1=int(input("enter a number:"))#num1
        self.num2=int(input("enter a number:"))#num2

    def addition(self):
        return (self.num1+self.num2)
    
    def substraction(self):
        return (self.num1-self.num2)
    
    def division(self):
        if self.num2==0:
            print("Error: can't divide by 0")
        else:
            return (self.num1/self.num2)
    
    def multiplication(self):
        return(self.num1*self.num2)
    
    
    

obj=Calculator()
print(obj.addition())
print(obj.substraction())
print(obj.division())
print(obj.multiplication())