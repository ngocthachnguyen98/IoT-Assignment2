import idGenerator
# This is the class defines Car
# Car class
class Car:
    # Attributes of Cars
    id = 0
    make = 'Make'
    bodyType = 'Body Type'
    colour = 'Colour'
    seats = 2
    location = 'Location'
    costPerHour = 20
    booked = False
    # Constructor
    def __init__(self, make, bodyType, colour, seats, location, costPerHour):
        self.id = idGenerator.carIdGenerator
        self.make = make
        self.bodyType = bodyType
        self.colour = colour
        self.seats = seats
        self.location = location
        self.costPerHour = costPerHour
        # sql command to add to table here
    
    # Book the car
    def book(self):
        self.booked = True
    
    # Lock and unlock
    def lock(self):
        pass
    

    def unlock(self):
        pass
