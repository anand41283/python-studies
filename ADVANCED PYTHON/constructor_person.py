class Person:
    name:str
    age:int
    sex:str
    profession:str
    def __init__(self,name,age,sex,profession):
        self.name=name
        self.age=age
        self.sex=sex
        self.profession=profession
    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("sex:",self.sex)
        print("Profession:",self.profession)
    def work(self):
        print(self.name," works in ",self.profession)

obj1=Person('arjun',24,'male','IT')
obj1.show()        
obj1.work()        