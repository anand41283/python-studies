"""
Operator overloading
--------------------
-> Same operatorto have different meaning according to the context is called operator overloading

"""
# print(dir(int))
# print(dir(str))

class Product:
    def __init__(self,p_name,p_price):
        self.p_name = p_name
        self.p_price = p_price
    def __len__(self):
        return self.p_price
    def __add__(self,other):
        final_result=self.p_price+other.p_price
        return final_result
    def __sub__(self,other):
        final_result=self.p_price-other.p_price
        return final_result
p1=Product("phone",50000)
p2=Product("laptop",60000)
print(len(p1))
print(p1+p2) #Product.__add__(p1,p2)
print(p1-p2) #Product.__sub__(p1,p2)

# print(len("abcd"))
# str.__len__("abcd")
# print(10+5)
# int.__add__(10,5)

"""
Magic methods
-------------
magic methods are the methods having two prefixes and suffixes underscores in the method name.
--> These are commonly used in operator overloading
--> Examples
__len__() : len()
__add__() : addition"""
