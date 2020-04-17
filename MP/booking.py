"""
This Booking class is for interaction with Bookings table in the MySQL database
"""

import datetime
import idGenerator

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorCode

class Booking:

    # Part A
    def make_a_booking(parameter_list):
        """
        The user needs to select which car they want to book and input the duration they want to use. 
        A car that is booked cannot be booked again until returned. 
        
        Note: when booked, an event should be added to Google Calendar, detailing the car, who books the car and the booked duration. Google Calendar will be tied to the Google login of the user.
        
        A new row in Bookings table will be added.
        """
        pass

    def cancel_a_booking(parameter_list):
        """
        The event added to Google Calendar will be removed, and the related information in the database needs to be modified.

        A row in Bookings table will be removed.
        """
        pass

    # Part B
    def unlock_a_car(parameter_list):
        """
        To unlock the car, User provides current date and time, username, password, carID. These will be checked in the **Bookings** table.
        
        If everything is validated:
            - The booking's "ongoing" will be change to true


        A SELECT query will be executed in Bookings table to see if validated.
        """
        pass

    def lock_a_car(parameter_list):
        """
        When user locks the car, this means "the booking is over (it's a history now) and can be removed":
            - The booking with the targeted car_id and the ongoing status (true) will be removed from Bookings table and added to Histories table
            - Car's booked attribute will be changed to true again in Cars table
        """
        pass