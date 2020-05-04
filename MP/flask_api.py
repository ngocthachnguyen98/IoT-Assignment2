from flask import Flask, Blueprint, request, jsonify, render_template, flash, redirect, url_for, session, escape
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os, requests, json
from flask import current_app as app
from passlib.hash import sha256_crypt
from sqlalchemy import or_
import calendar_for_api  

api = Blueprint("api", __name__)

db = SQLAlchemy() # for accessing database
ma = Marshmallow() # for serializing objects


# DECLARING THE MODELS

# USER
class User(db.Model):
    __tablename__   = "Users"
    id              = db.Column(db.Integer,     primary_key = True,     autoincrement = True)
    username        = db.Column(db.String(),    nullable = False,       unique = True)
    password        = db.Column(db.String(),    nullable = False)
    email           = db.Column(db.String(),    nullable = False,       unique = True)
    fname           = db.Column(db.String(),    nullable = False)
    lname           = db.Column(db.String(),    nullable = False)
    role            = db.Column(db.String(),    nullable = False)

    # bookings        = db.relationship('Booking', backref = 'User', lazy = True) # One-to-many relationship
    # histories       = db.relationship('History', backref = 'User', lazy = True) # One-to-many relationship
    
    def __init__(self, username, password, email, fname, lname, role):
        self.username   = username
        self.password   = password
        self.email      = email
        self.fname      = fname
        self.lname      = lname
        self.role       = role

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose (not exposing password)
        fields = ('id', 'username', 'email', 'fname', 'lname', 'role')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


# CAR
class Car(db.Model):
    __tablename__   = "Cars"
    id              = db.Column(db.Integer,         primary_key = True,     autoincrement = True)
    make            = db.Column(db.String(),        nullable = False)
    body_type       = db.Column(db.String(),        nullable = False)
    colour          = db.Column(db.String(),        nullable = False)
    seats           = db.Column(db.Integer(),       nullable = False)
    location        = db.Column(db.String(),        nullable = False)
    cost_per_hour   = db.Column(db.Float(4, 2),     nullable = False)
    booked          = db.Column(db.Boolean(),       nullable = False)

    # bookings        = db.relationship('Booking', backref = 'Car', lazy = True) # One-to-many relationship
    # histories       = db.relationship('History', backref = 'Car', lazy = True) # One-to-many relationship
    
    def __init__(self, make, body_type, colour, seats, location, cost_per_hour, booked):
        self.make           = make
        self.body_type      = body_type
        self.colour         = colour
        self.seats          = seats
        self.location       = location
        self.cost_per_hour  = cost_per_hour
        self.booked         = booked

class CarSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'make', 'body_type', 'colour', 'seats', 'location', 'cost_per_hour', 'booked')

car_schema = CarSchema()
cars_schema = CarSchema(many=True)


# BOOKING
class Booking(db.Model):
    __tablename__   = "Bookings"
    id              = db.Column(db.Integer,     primary_key = True,         autoincrement = True)
    user_id         = db.Column(db.String(),    nullable = False)
    car_id          = db.Column(db.String(),    nullable = False)
    begin_time      = db.Column(db.DateTime(),  nullable = False)
    return_time     = db.Column(db.DateTime(),  nullable = False)
    ongoing         = db.Column(db.Boolean(),   nullable = False)
    
    def __init__(self, user_id, car_id, begin_time, return_time, ongoing):
        self.user_id        = user_id
        self.car_id         = car_id
        self.begin_time     = begin_time
        self.return_time    = return_time
        self.ongoing        = ongoing

class BookingSchema(ma.Schema):
    class Meta:
        # Fields to expose (not exposing id)
        fields = ('user_id', 'car_id', 'begin_time', 'return_time', 'ongoing')

booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)


# HISTORY
class History(db.Model):
    __tablename__   = "Histories"
    id              = db.Column(db.Integer,     primary_key = True,         autoincrement = True)
    user_id         = db.Column(db.String(),    nullable = False)
    car_id          = db.Column(db.String(),    nullable = False)
    begin_time      = db.Column(db.DateTime(),  nullable = False)
    return_time     = db.Column(db.DateTime(),  nullable = False)
    
    def __init__(self, user_id, car_id, begin_time, return_time):
        self.user_id        = user_id
        self.car_id         = car_id
        self.begin_time     = begin_time
        self.return_time    = return_time

class HistorySchema(ma.Schema):
    class Meta:
        # Fields to expose (not exposing id)
        fields = ('user_id', 'car_id', 'begin_time', 'return_time')

history_schema = HistorySchema()
histories_schema = HistorySchema(many=True)

# ENDPOINTS

# TESTED
# Endpoint to register
@api.route("/register", methods = ["GET", "POST"])
def register():
    if request.method=="POST":
        # Get form data
        username        = request.form.get("username")
        password        = request.form.get("password")
        email           = request.form.get("email")
        fname           = request.form.get("fname")
        lname           = request.form.get("lname")
        role            = request.form.get("role")

        # Check if the username or email has already been registered
        registered = db.session.query(User).filter(or_( User.username == username, 
                                                        User.email == email)).first()

        if registered is not None:
            flash("The username or email ALREADY EXISTS. Cannot be used for registration", "danger")
            
            return redirect(url_for('site.registerPage'))
        else:
            flash("The username and email DO NOT EXIST. Can be used for registration")
            
            # Hash the password before insertion
            hashed_password = sha256_crypt.hash(str(password))
            
            # Prepare row and add to the database
            newUser = User( username = username, 
                            password = hashed_password, 
                            email = email, 
                            fname = fname, 
                            lname = lname, 
                            role = role)

            db.session.add(newUser)
            db.session.commit()

            flash("You are registered and can now login","success")
            return redirect(url_for('site.loginPage'))  # Go to Login page after registration

    return render_template('register.html')


# TESTED
# Endpoint to login 
@api.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="POST":
        # Get form data
        username    = request.form.get("username")
        password    = request.form.get("password")

        # Query 
        data = db.session.query(User.id, User.password).filter_by(username = username).first()

        if data is None: # If username does not exist
            flash("Invalid Username!", "error")
            return render_template('login.html')
        else: # If username exists
            user_id = data[0]
            stored_password = data[1] 

            # Verify password
            if sha256_crypt.verify(password, stored_password):
                flash("You are now logged in!", "success")

                # Set session data
                session["user_id"] = user_id

                return redirect(url_for('site.homePage'))
            else:
                flash("Invalid Password!", "error")
                return render_template('login.html') 
 
    return render_template('login.html')


# TESTED
# Endpoint to logout
@api.route('/logout')
def logout():
   # Remove the user ID from the session if it is there
   session.pop('user_id', None)
   flash("You are now logged out!", "danger")
   return redirect(url_for('site.index'))


# TESTED
# Endpoint to view histories (user-specified)
@api.route("/history/<user_id>", methods = ["GET"])
def getUserHistories(user_id):
    histories = History.query.filter_by(user_id = user_id).all()

    result = histories_schema.dump(histories)

    return jsonify(result)


# TESTED
# Endpoint to show all UNBOOKED cars
@api.route("/car/unbooked", methods = ["GET"])
def getUnbookedCars():
    cars = Car.query.filter_by(booked = False).all()

    result = cars_schema.dump(cars)

    return jsonify(result)


# TESTED
# Endpoint to search for cars
@api.route("/car/search", methods = ["GET", "POST"])
def carSearch():
    if request.method=="POST":
        make            = request.form.get("make")
        body_type       = request.form.get("body_type")
        colour          = request.form.get("colour")
        seats           = request.form.get("seats")
        location        = request.form.get("location")
        cost_per_hour   = request.form.get("cost_per_hour")
        booked          = request.form.get("booked") # if this field is null, it's equivalent to 0, which booked = False 

        cars = db.session.query(Car).filter(or_(Car.make            == make, 
                                                Car.body_type       == body_type,
                                                Car.colour          == colour,
                                                Car.seats           == seats,
                                                Car.location        == location,
                                                Car.cost_per_hour   == cost_per_hour,
                                                Car.booked          == booked)).all()

        result = cars_schema.dump(cars)

        return render_template("car_search_result.html", cars = result)

    return render_template('car_search.html')


# TESTED
# Endpoint to make a booking
@api.route("/booking/make", methods = ["GET", "POST"])
def makeABooking():
    if request.method=="POST": # WARNING: using POST for update and insertion
        # Get input from form data
        # Resource to handle date/time values: https://www.w3schools.com/html/html_form_input_types.asp
        user_id     = session.get("user_id")
        car_id      = request.form.get("car_id")
        begin_date  = request.form.get("begin_date")
        begin_time  = request.form.get("begin_time")
        return_date = request.form.get("return_date")
        return_time = request.form.get("return_time")

        begin_datetime  = "{} {}".format(begin_date, begin_time) 
        return_datetime = "{} {}".format(return_date, return_time) 

        # Prepare object for database insertion
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

        # Add event to Google Calendar
        event = {
            'summary': 'Carshare Booking Reservation',
            'description': f'userId: {user_id} and carId: {car_id}',
            'start': {
                'dateTime': begin_datetime.replace(' ', 'T') + ':00+10:00',  # '2020-05-02T10:00:00+10:00'
            },
            'end': {
                'dateTime': return_datetime.replace(' ', 'T') + ':00+10:00',
            },
        }
        calendar_for_api.insert(event)

        flash("Booking made")

        return redirect(url_for('site.homePage'))

    return render_template('make_a_booking.html')


# TESTED
# Endpoint to cancel a booking
@api.route("/booking/cancel", methods = ["GET", "POST"])
def cancelABooking():
    if request.method=="POST": # WARNING: using POST for update and deletion
        # Get input from form data
        # Resource to handle date/time values: https://www.w3schools.com/html/html_form_input_types.asp
        user_id     = session.get("user_id")
        car_id      = request.form.get("car_id")
        begin_date  = request.form.get("begin_date")
        begin_time  = request.form.get("begin_time")

        begin_datetime  = "{} {}".format(begin_date, begin_time) 

        # Prepare object for database insertion
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

        # Delete event from Google Calendar
        calendar_for_api.delete(user_id, car_id, begin_datetime)

        flash("Booking cancelled")

        return redirect(url_for('site.homePage'))

    return render_template('cancel_a_booking.html')


# Endpoint to unlock a car



# Endpoint to lock a car



# Endpoint to get car's location with Google Maps API