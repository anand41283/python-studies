class Vehicle:
    def __init__(self,name,max_speed,milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage
    def capacity(self,capacity):
        self.capacity=capacity
        print(f"The seating capacity of a {self.name} is {capacity} passengers")
        # print(f"seating capacity {capacity}")
    
class Bus(Vehicle):
    def __init__(self, name, max_speed, milage,seating_capacity=50):
        super().__init__(name, max_speed, milage)
        self.seating_capacity = seating_capacity

my_bus=Bus('volswagon',1500,50)
print(f"Bus_name: {my_bus.name}")
print(f"seating_capacity: {my_bus.seating_capacity}")
my_bus.capacity(24)

        

    