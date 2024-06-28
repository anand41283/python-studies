"""
abstract class and abstract method
----------------------------------
Abstarct method: method without body is known as abstract method
Abstract class: class that contain abstract method is known as abstract class
--> python does not support abstract class 
--> we can implement this concept using abc module

"""
class A: #abstract class
    def abc(self):
        pass

#Example1:
from abc import ABC,abstractmethod
class Vehicle(ABC):
    def start_engine(self):
        print("engine started")
    def stop_engine(self):
        print("engine stopped")
    @abstractmethod
    def change_gear(self):
        pass
class car(Vehicle):
    def speed(self):
        print("speed limit")
    def change_gear(self):
        print("Gear changed")
class truck(Vehicle):
    def change_gear(self):
        print("Gear changed")

    
c1=car()
c1.start_engine()
c1.stop_engine()
c1.speed()
c1.change_gear()

