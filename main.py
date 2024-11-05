class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

Schoolbus = Bus("School Volvo", 180, 12)

print("Vehicle Name:", Schoolbus.name, "Speed:", Schoolbus.max_speed, "Mileage:", Schoolbus.mileage)
