"""create a Bus child class that inherits from the vehicle class.The default fare charge of any vehicle is seating capacity*100.If vehicle is Bus instance,
we need to add an extra 10% on full fare as a maintainance charge.So total fare for bus instance will become the final amount=totalfare+10% of the total fare.
note:The bus seating capacity is 50.so the final fare amount should be 5500.You need to override the fare() method of a vehicle class in Bus class.
"""

class Vehicle:
    def __init__(self,seating_capacity):#=50):
        self.seating_capacity = seating_capacity

    def calculate_fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def calculate_fare(self):
        base_fare = super().calculate_fare() # Calculate base fare using the parent class method
        maintenance_charge = 0.10 * base_fare # Calculate the maintenance charge (10% of base fare)
        total_fare = base_fare + maintenance_charge # Add maintenance charge to base fare
        return total_fare


bus = Bus(50) # Creating a Bus instance with a seating capacity of 50
fare=bus.calculate_fare() # Calculating the fare for the bus
print(f"The total fare for the bus is {fare}")

