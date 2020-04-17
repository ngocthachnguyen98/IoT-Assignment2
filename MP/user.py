"""
This User class is for interaction with Users table in the MySQL database
"""

import idGenerator

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorCode

class User:

    # Part A
    def register(self, username, password, email, fname, lname, role):
        """
        A new row will be input into Users table. The function should check whether the username and email is duplicated in the database.
        """        

    def login(self, username, password):
        """
        Upon logging, username and password will be checked in the Users table to validate the user.
        A connection will be establish to the database. A SELECT query will be executed to find out if the user's credential available in the database.
        
        If the query returns 1 row, the function will return True.
        If the query returns 0 row, the function will return False.

        Arguments:
            username {String} -- User's credential
            password {String} -- User's credential
        """

    def logout(self):
        """
        Log the user out of the system
        """
        