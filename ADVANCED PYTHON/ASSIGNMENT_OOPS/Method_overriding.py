# create a class that implement method overriding

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    pass  # Cow inherits the speak() method from Animal

# Example usage:
dog = Dog()
cat = Cat()
cow = Cow()

print("Dog says:", dog.speak())
print("Cat says:", cat.speak())
print("Cow says:", cow.speak())
"""
We have a base class Animal with a speak method defined. This method is marked with pass, indicating that it's meant to be overridden 
by subclasses.

We then create three subclasses (Dog, Cat, and Cow) that inherit from Animal.

Each subclass overrides the speak method with its own implementation.

In the example usage section, we create instances of each subclass and call their speak methods. 
As a result, the appropriate speak method for each animal type is executed, demonstrating method overriding.

Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass,
enabling polymorphism and more specific behavior for each subclass.

"""
