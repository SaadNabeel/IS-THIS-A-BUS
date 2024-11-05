class Vehicle:

    def __init__(self, name, max_speed, mileage, owner):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.owner=owner
class Bus(Vehicle):
    pass

Schoolbus = Bus("School Volvo", 180, 12,"Saad")

print("Vehicle Name:", Schoolbus.name, "Speed:", Schoolbus.max_speed, "Mileage:", Schoolbus.mileage,'Owner:',Schoolbus.owner)
