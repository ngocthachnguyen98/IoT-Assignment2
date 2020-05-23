import unittest
from flask import Flask, session
from flask_session import Session
import importlib, importlib.util
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt
from sqlalchemy import or_
from flask_api import api, db, User, Booking, Car, History

# The set up vairables for the test cases app and Google SQL access
app = Flask(__name__)
HOST= "35.201.22.170"
USER= "root"
PASSWORD= "password"
DATABASE= "Carshare"

class MasterPiTest(unittest.TestCase):

    """
        This is the set up for the test case, config the Flask app with
        Database access variables and init the db (from flask_api) with the app context
    """
    def setUp(self):
        db = SQLAlchemy()
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{}:{}@{}/{}".format(USER, PASSWORD, HOST, DATABASE)
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
        app.app_context().push()
        db.init_app(app)
        with app.app_context():
            db.create_all()

    # This will be the boolean function to check whether a user exists or not in
    #  the database by browsing the username
    def userExists(self, username):
        """
            This function will return a boolean if a user with specific username
            exits in the database, it will support later tests of user with assertion
            - Parameter: username in String type
            - Function, will search for a user id that has matching username from the param
            - Return False if the searched user id is None and vice versa
        """
        data = db.session.query(User.id).filter_by(username = username).first()
        if data is None:
            return False
        else:
            return True
   
    # This will be the boolean function to check whether a car exists or not in
    #  the database by browsing the car make         
    def carExists(self, carmake):
        """
            This function only support the add car test case
            it will query the database for a car id that has matching make
            - Parameter: car make in String type
            - Function: query for car id that has the matching car make 
            (in this case, the only time it is called make = "Test_Toyota")
            - Return False if the car id is None and vice versa
        """
        data = db.session.query(Car.id).filter_by(make = carmake).first()
        if data is None:
            return False
        else:
            return True
    
    # This will be the boolean function to check whether a booking exists or not in
    #  the database by browsing the user id and car id, get the first result
    def bookingExists(self, user_id, car_id):
        """
            This function will 
        """
        data = db.session.query(Booking).filter_by(user_id = user_id, car_id = car_id).first()
        if data is None:
            return False
        else:
            return True

    # This is the test of login, we try with 
    def test_login(self):
        username = "user1"
        password = "pw1"
        userID = 1
        data = db.session.query(User.id).filter_by(username = username, password = password).first()
        self.assertTrue(data is not None)
    
    # This method creates a dummy user in the first run, from the second run
    # it will only check if the user already exists
    def test_register(self):
        username        = "testusername"
        password        = "testpassword"
        email           = "testemail@gmail.com"
        fname           = "testfirstname"
        lname           = "testlastname"
        role            = "engineer"

        registered = db.session.query(User).filter(or_( User.username == username, 
                                                        User.email == email)).first()
        if registered is not None:
            self.assertTrue(self.userExists(username))
        else:
            hashed_password = sha256_crypt.hash(str(password))
            newUser = User( username = username, 
                            password = hashed_password, 
                            email = email, 
                            fname = fname, 
                            lname = lname, 
                            role = role)
            db.session.add(newUser)
            db.session.commit()
            self.assertTrue(self.userExists(username))
    #Get test user id for the later tests
    def get_test_id(self):
        test_username = "testusername"
        test_user_id = db.session.query(User.id).filter_by(username = test_username).first()
        print(test_user_id)
        return test_user_id
    
    # This test will search for a user history bases on his/her user id
    def test_userHistories(self):
        user_id = 12
        histories = History.query.filter_by(user_id = user_id).all()
        self.assertTrue((histories is not None))
    
    # This will test the search car function base on make, body type, colour,
    # seats, cost per hour and booked
    def test_searchCar(self):
        make            = "Toyota"
        body_type       = "Seden"
        colour          = "Black"
        seats           = "5"
        cost_per_hour   = "10.5"
        booked          = True
        cars = db.session.query(Car).filter(or_(Car.make            == make, 
                                                Car.body_type       == body_type,
                                                Car.colour          == colour,
                                                Car.seats           == seats,
                                                Car.cost_per_hour   == cost_per_hour,
                                                Car.booked          == booked)).all()
        self.assertTrue((cars is not None))
    
    # This method will create a dummy car for testing the booking without disrupting
    # other valid cars in the database
    def add_car(sefl):
        make            = "Test_Toyota"
        body_type       = "Seden"
        colour          = "Black"
        seats           = 5
        location        = "-37.814, 144.96332"
        cost_per_hour   = 10.5

        newCar = Car( make = make,
                        body_type = body_type,
                        colour = colour,
                        seats = seats,
                        location = location,
                        cost_per_hour = cost_per_hour,
                        booked = True

        )
        db.session.add(newCar)
        db.session.commit()
        self.assertTrue(self.carExists(make))

    # This method will use the dummy user to book a car and check in the Booking table
    # if that booking exits
    def test_bookCar(self):
        user_id     = "12"
        car_id      = "6"
        begin_date  = "2020-05-21" 
        begin_time  = "12:00:00"
        return_date = "2020-05-23"
        return_time = "12:00:00"

        begin_datetime  = "{} {}".format(begin_date, begin_time) 
        return_datetime = "{} {}".format(return_date, return_time)

        newBooking = Booking(   user_id = user_id,
                                car_id = car_id,
                                begin_time = begin_datetime,
                                return_time = return_datetime,
                                ongoing = False)
         # Add new row to the database
        db.session.add(newBooking)

        # Update car's availability 
        car = Car.query.get(car_id) 
        car.booked = True

        # Commit changes
        db.session.commit()
        self.assertTrue(self.bookingExists(user_id, car_id))
    
    # This method will delete the booking from the previous test and check
    # if it still exits
    def test_cancelBooking(self):
        user_id     = "12"
        car_id      = "6"
        begin_date  = "2020-05-21" 
        begin_time  = "12:00:00"

        begin_datetime  = "{} {}".format(begin_date, begin_time) 

        booking = db.session.query(Booking).filter( Booking.user_id == user_id,
                                                    Booking.car_id == car_id,
                                                    Booking.begin_time == begin_datetime).first()
         # Delete row from the database
        db.session.delete(booking)

        # Update car's availability 
        car = Car.query.get(car_id)
        car.booked = False

        # Commit changes
        db.session.commit()
        self.assertFalse(self.bookingExists(user_id, car_id))
    
    def test_unlockCar(self):
        self.test_bookCar()
        user_id     = "12"
        car_id      = "6"
        begin_date  = "2020-05-21" 
        begin_time  = "12:00:00"

        begin_datetime  = "{} {}".format(begin_date, begin_time)
        # Check if this is the right user with the right booked car and time 
        booking = db.session.query(Booking).filter_by(  user_id = user_id,
                                                    car_id = car_id,
                                                    begin_time = begin_datetime).first()

        # Activate booking
        booking.ongoing = 1

        # Commit changes
        db.session.commit()
        self.assertTrue(self.bookingExists(user_id, car_id))
        

    def test_lockCar(self):

        user_id     = "12"
        car_id      = "6"
        # Find the booking
        booking = db.session.query(Booking).filter_by(user_id = user_id,
                                                    car_id = car_id).first()
        # Remove record from Booking table
        # db.session.delete(booking)
        begin_date  = "2020-05-21" 
        begin_time  = "12:00:00"
        return_date = "2020-05-23"
        return_time = "12:00:00"

        begin_datetime  = "{} {}".format(begin_date, begin_time) 
        return_datetime = "{} {}".format(return_date, return_time)

        # Record finished booking to History table
        newHistory = History(   user_id = user_id,
                                car_id = car_id,
                                begin_time = begin_datetime,
                                return_time = return_datetime)
        db.session.add(newHistory)


        # Update car's availability
        car = Car.query.get(car_id) 
        car.booked = False

        # Commit changes
        db.session.commit()
        self.assertFalse(self.bookingExists(user_id, car_id))

if __name__ == "__main__":
    unittest.main()
MasterPiTest.get_test_id()