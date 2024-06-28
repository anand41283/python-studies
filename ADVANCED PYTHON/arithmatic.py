class Arithematic:
    num1:int
    num2:int
    def value_add(self,n1,n2):
        self.num1 = n1
        self.num2 = n2
    def add(self):
        print(self.num1+self.num2)
    def sub(self):
        print(self.num1-self.num2)
    def mul(self):
        print(self.num1*self.num2)
    def div(self):
        print(self.num1/self.num2)

a1=Arithematic()
a1.value_add(20,10)
a1.add()
a1.sub()
a1.mul()
a1.div()
