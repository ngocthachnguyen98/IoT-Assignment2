"""
This User class is for interaction with Users table in the MySQL database
"""

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorCode


class User:

    # Part A
    def register(self, username, password, email, fname, lname, role):
        """
        A new row will be input into Users table. 

        The function should check whether the username or email is duplicated in the database.
        """  

        try:
            # Establish connection with MySQL database
            connection = mysql.connector.connect(host='localhost',
                                                database='carshare',
                                                user='root',
                                                password='pynative@#29')

            # Queries
            select_query = "SELECT * FROM Users WHERE username={0} OR email={1}".format(username, email)
            insert_query = "INSERT INTO Users (username, password, email, fname, lname, role) VALUES (\"User100\", \"pw100\", \"user100@carshare.com\", \"Thach\", \"Nguyen\", \"Customer\")"

            # Execute queries
            cursor = connection.cursor()

            # Check if the username and email present in the database
            cursor.execute(select_query)
            
            # Gets the number of rows affected by the command executed
            row_count = cursor.rowcount
            print "Number of affected rows: {}".format(row_count)

            if row_count == 0: # if the username / email doesn't not exist, register user
                cursor.execute(insert_query)
                connection.commit()
                print "Number of inserted rows: {}".format(cursor.rowcount)
            else: # else, do not register user
                print "Username / Email is already registered"


            cursor.close()
        except mysql.connector.Error as error:
            print("Failed to execute query in Users table {}".format(error))

        finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")


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
        