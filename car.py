# This is the class defines Car
import idGenerator

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorCode

class Car:
    # Attributes
    id = 0
    make = 'Make'
    body_type = 'Body Type'
    colour = 'Colour'
    seats = 2
    location = 'Location'
    cost_per_hour = 20.99 # Should we make this a decimal-type variable? e.g. the cost could $20.99/hour
    booked = False 

    # Constructor
    def __init__(self, make, body_type, colour, seats, location, cost_per_hour):
        self.id = idGenerator.carIdGenerator
        self.make = make
        self.body_type = body_type
        self.colour = colour
        self.seats = seats
        self.location = location
        self.cost_per_hour = cost_per_hour

        # sql command to insert a row to Cars table
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='carshare',
                                                user='root',
                                                password='pynative@#29')

            mySql_insert_query = "INSERT INTO Cars (id, make, body_type, colour, seats, location, cost_per_hour, booked) 
                                VALUES (self.id, self.make, self.body_type, self.colour, self.seats, self.location, self.cost_per_hour, False)"

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Cars table")
            
            cursor.close()

        except mysql.connector.Error as error:
            print("Failed to insert record into Cars table {}".format(error))

        finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")
    
    # Book the car
    def book(self):
        self.booked = True
    
    # Lock and unlock
    def lock(self):
        pass
    
    def unlock(self):
        pass
