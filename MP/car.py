"""
This Car class is for interaction with Cars table in the MySQL database
"""

import idGenerator

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorCode

class Car:
    
    # Part A
    def show_all_available_car(self):
        """
        Show a list of cars available

        QUESTIONS:
            - Is this returning all rows in Cars table?
            - Or just returing the cars which are available on certain dates? (filters) [search_car() can be used for this]
        """
        pass

    def search_car(parameter_list):
        """
        Be able to search by any of the car’s properties

        QUESTIONS:
            - What are the properties/filters to search by?
        """
        pass

    # Part B
    def show_all_car_location(parameter_list):
        """
        This function will help showing all the car's location by using Google Map API
        """
        pass
