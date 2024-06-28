#Duck typing
#-----------
class Animal:
    def perform(self):
        print("Animal perform in circus")


class Human:
    def perform(self):
        print("human performs in circus")


class Circus:
    def play(self,a2:Animal):
        a2.perform()

a1=Animal()
h1=Human()
c1=Circus()
c1.play(a1)
c1.play(h1)


"""
def add(a,b):
    return a+b
add(10,20)

"""
