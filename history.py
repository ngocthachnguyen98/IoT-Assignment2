# This class defines Histories
import datetime
import idGenerator

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorCode

class History:
    # Attributes
    id = 0
    user_id = 0
    car_id = 0
    begin_time = datetime.datetime.now
    return_time = datetime.datetime.now

    # Constructor
    def __init__(self, user_id, car_id, begin_time, return_time):
        self.id = idGenerator.historyIdGenerator
        self.user_id = user_id
        self.car_id = car_id
        self.begin_time = begin_time
        self.return_time = return_time

        # sql command to insert a row to Cars table
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='carshare',
                                                user='root',
                                                password='pynative@#29')

            mySql_insert_query = "INSERT INTO Histories (id, user_id, car_id, begin_time, return_time) 
                                VALUES (self.id, self.user_id, self.car_id, self.begin_time, self.return_time)"

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Histories table")
            
            cursor.close()

        except mysql.connector.Error as error:
            print("Failed to insert record into Histories table {}".format(error))

        finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")

    def showUserHistory(self, user_id):
        pass