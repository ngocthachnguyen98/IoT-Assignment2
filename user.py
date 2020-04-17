# This class defines Users
import idGenerator

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorCode

class User:
    id = 0
    username = 'username'
    password = 'password'
    email = 'email@gmail.com'
    fname = 'first_name'
    lname = 'last_name'
    role = 'role'


    # Constructor
    def __init__(self, username, password, email, fname, lname, role):
        self.id = idGenerator.userIdGenerator
        self.username = username
        self.password = password
        self.email = email
        self.fname = fname
        self.lname = lname
        self.role = role

        # sql command to insert a row to Users table
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='carshare',
                                                user='root',
                                                password='pynative@#29')

            mySql_insert_query = "INSERT INTO Users (id, username, password, email, fname, lname, role) 
                                VALUES (self.id, self.username, self.password, self.email, self.fname, self.lname, self.role)"

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Users table")

            cursor.close()

        except mysql.connector.Error as error:
            print("Failed to insert record into Users table {}".format(error))

        finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")
    
    # Getter
    def getUserName(self):
        return self.username

    def getPassword(self):
        return self.password
    
    def getEmail(self):
        return self.email
    
    def getFname(self):
        return self.fname
    
    def getLnameLname(self):
        return self.lname
    
    def getRole(self):
        return self.role
    