import unittest
from flask import Flask, session
from flask_session import Session
import importlib, importlib.util
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt
from sqlalchemy import or_
from flask_api import api, db, User, Booking, Car, History

app = Flask(__name__)
# Set up session for storing session data and showing flashed messages

HOST        = "35.189.9.144"
USER        = "root"
PASSWORD    = "iotassignment2"
DATABASE    = "CarShare"

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db = SQLAlchemy()
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{}:{}@{}/{}".format(USER, PASSWORD, HOST, DATABASE)
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
        app.app_context().push()
        db.init_app(app)
        with app.app_context():
            db.create_all()

    def userExists(self, username):
        data = db.session.query(User.id).filter_by(username = username).first()
        if data is None:
            return False
        else:
            return True
            
    def carExists(self, carmake):
        data = db.session.query(Car.id).filter_by(make = carmake).first()
        if data is None:
            return False
        else:
            return True
    
    # def bookingExists(self, user_id, car_id):


    def test_login(self):
        username = "user1"
        password = "pw1"
        userID = 2
        data = db.session.query(User.id).filter_by(username = username).first()
        self.assertTrue(data[0] == 2)
    
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
    def test_userHistories(self):
        user_id = 4
        histories = History.query.filter_by(user_id = user_id).all()
        self.assertTrue((histories is not None))
    
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
    def add_car(sefl):
        make            = "Test_Toyota"
        body_type       = "Seden"
        colour          = "Black"
        seats           = "5"
        location        = "-37.814, 144.96332"
        cost_per_hour   = "10.5"

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
    # def test_bookCar(self):
    #     user_id     = session.get("user_id")
    #     car_id      = request.form.get("car_id")
    #     begin_date  = request.form.get("begin_date")
    #     begin_time  = request.form.get("begin_time")
    #     return_date = request.form.get("return_date")
    #     return_time = request.form.get("return_time")

if __name__ == "__main__":
    unittest.main()