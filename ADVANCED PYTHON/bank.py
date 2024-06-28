class Bank:
    acc_no:int
    balance:int
    ac_type:str
    p_name:str
    def create_acc(self,acno,bal,actype,name):
        self.acc_no=acno
        self.balance=bal
        self.ac_type=actype
        self.p_name=name
    def display(self):
        print("account_no:",self.acc_no)
        print("account_balance:",self.balance)
        print("account_type:",self.ac_type)
        print("account_holder:",self.p_name)
    def deposite(self):
        amount=int(input("enter deposite amount: "))
        self.balance+=amount
        print(f"your SBI account {self.acc_no} is credited with {amount} avl balance is {self.balance}")
    def withdraw(self):
        withdraw=int(input("enter withdraw amount: "))
        if self.balance>=withdraw:
            self.balance-=withdraw
            print(f"your SBI account {self.acc_no} is debited with {withdraw} avl balance is {self.balance}")
        else:
            print("insufficient balance")
obj1=Bank()
obj1.create_acc(100,400,'savings','anu')
obj1.deposite()
obj1.display()
obj1.withdraw()


