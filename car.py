import datetime
# This is the class defines Car
currentDT = datetime.datetime.now()
class Car:
    # Attributes of Cars
    make = 'Make'
    bodyType = 'Body Type'
    colour = 'Colour'
    seats = 2
    location = 'Location'
    costPerHour = 20
    bookedStart = currentDT.hour
    bookedDuration = 1
    booked = False
    # Constructor
    def __init__(self, make, bodyType, colour, seats, location, costPerHour):
        self.make = make
        self.bodyType = bodyType
        self.colour = colour
        self.seats = seats
        self.location = location
        self.costPerHour = costPerHour
    
    # Book the car
    def book(self):
        self.booked = True
    
    # Lock and unlock
    def lock(self):
        pass
    

    def unlock(self):
        pass
