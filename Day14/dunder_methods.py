# Dunder Methods
# Special Class Methods which has double underscore both infront and behind the name of method (Example: __init__)
# Dunder Methods are used to change the default behaviors of class and object operations
# Example: adding two classes

class Vehicle:
    def __init__(self, name, price, wheels, model, mileage):
        self.name = name
        self.price = price
        self.wheels = wheels
        self.model = model
        self.mileage = mileage
    
    # Operator Overloading using Dunder Method
    def __add__(self, other):
        new_name = f"{self.name}-{other.name}"
        new_price = self.price + other.price
        new_wheels = self.wheels + other.wheels
        new_model = f"{self.model}-{other.model}"
        new_mileage = self.mileage + other.mileage

        return Vehicle(new_name, new_price, new_wheels, new_model, new_mileage)

yamaha_bike = Vehicle("FZ", 450000, 2, "2025", 45)
suzuki_car = Vehicle("Jimmy", 5500000, 4, "2025", 15)

new_vehicle = yamaha_bike + suzuki_car

print(new_vehicle.name)
print(new_vehicle.price)

# __add__, __sub__, __mul__, __div__, __mod__, __pow__
