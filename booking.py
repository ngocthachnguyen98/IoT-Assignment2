import datetime
import idGenerator
class Booking:
    # Class attributes
    id = 0
    user_id = 0
    car_id = 0
    begin_time = datetime.datetime.now
    return_time = datetime.datetime.now
    done = False

    # Constructor
    def __init__(self, user_id, car_id, begin_time, return_time):
        self.id = idGenerator.bookingIdGenerator
        self.user_id = user_id
        self.car_id = car_id
        self.begin_time = begin_time
        self.return_time = return_time

    def confirmDone(self):
        self.done = True