import MySQLdb, datetime

"""
TO-DO:
    - Missing try/except
    - Add input validation scheme
    - Flask API
"""
class DatabaseUtils:
    HOST = "35.201.22.156"
    USER = "root"
    PASSWORD = "password"
    DATABASE = "carshare"

    def __init__(self, connection = None):
        if(connection == None):
            connection = MySQLdb.connect(DatabaseUtils.HOST, DatabaseUtils.USER,
                DatabaseUtils.PASSWORD, DatabaseUtils.DATABASE)
        self.connection = connection
    
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()
    
    # For closing db connection
    def close(self):
        self.connection.close()

    """PART A"""
    def register(self, username, password, email, fname, lname, role):
        # Check if username and email already exist
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Users WHERE username=(%s) OR email=(%s)", (username, email))
            queryResult = cursor.fetchall() 

        # Check if the result is an empty list
        if not queryResult:
            print("The username and email DO NOT EXIST. Can be used for registration")
            
            with self.connection.cursor() as cursor:
                # Preparing insert query
                insert_stmt = (
                    "INSERT INTO Users (username, password, email, fname, lname, role)"
                    "VALUES (%s, %s, %s, %s, %s, %s)"
                )
                data = (username, password, email, fname, lname, role)

                # Execute and commit
                cursor.execute(insert_stmt, data)
                self.connection.commit()
                print("Registered...")

                # Return True if insert successfully
                return cursor.rowcount == 1
        else: 
            print("The username or email ALREADY EXISTS. Can't be used for registration")
            pass


    def login(self, username, password):
        # Verify the username and password in the database
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Users WHERE username=(%s) AND password=(%s)", (username, password))
            queryResult = cursor.fetchone()

        if not queryResult: # No row returned
            print("Invalid credentials. Username / Password is incorrect.")
            return None
        else: # Row found
            print("Welcome {}! You logged in.".format(username))
            return queryResult[0]

    
    def showAllUnbookedCars(self, booked=0):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Cars WHERE booked=(%s)", (booked))
            queryResult = cursor.fetchall()
    
    def searchCar(self, car_id):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Cars WHERE id=(%s)", (car_id))
            queryResult = cursor.fetchall()
    
    def makeABooking(self, user_id, car_id, begin_time=datetime.datetime.now(), return_time=None, ongoing=1):
        
        # Check if user_id already exist
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Bookings WHERE user_id=(%s)", (user_id))
            queryResult = cursor.fetchall()
        
        if not queryResult:
            print("The user_id DOES NOT EXIST. Can be used for booking")
            with self.connection.cursor() as cursor:
               
                cursor.execute("INSERT INTO Bookings (user_id, car_id, begin_time, return_time, ongoing) VALUES (%s %s %s %s %s)", (user_id, car_id, begin_time, return_time, ongoing))#adds booking to bookings table
                cursor.execute("UPDATE Cars SET booked = 1 WHERE car_id = (%s)",(car_id)) #sets the value of the car to booked: booked = 1 
                self.connection.commit()
                print("Booked!")
                return cursor.rowcount == 1
        else:        
             print("The user_id ALREADY EXISTS. Can't be used for booking")
    

    def cancelABooking(self, user_id, car_id, begin_time):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Bookings WHERE user_id=(%s)", (user_id))
            queryResult = cursor.fetchall()
        
        if not queryResult:
            print("The user_id DOES NOT EXIST. Can be cancelled")
           
        else:        
             with self.connection.cursor() as cursor:
               
                cursor.execute("DELETE FROM Bookings (user_id, car_id, begin_time) VALUES (%s %s %s)", (user_id, car_id, begin_time))#deletes booking from bookings table
                cursor.execute("UPDATE Cars SET booked = 0 WHERE car_id = (%s)",(car_id)) #sets the value of the car to booked: booked = 0 
                self.connection.commit()
                print("Cancelled!")
                
    
    def getUserHistory(self, user_id):
        with self.connection.cursor() as cursor:
            # cursor.execute("SELECT * FROM Histories WHERE user_id=1")
            queryResult = cursor.fetchall()
        
        if not queryResult: # No row returned
            return None
        else: # Row found
            return queryResult
    
    """PART B"""
    def showCarLocations(self, parameter_list):
        pass

    def unlockCar(self, parameter_list):
        pass
    
    def lockCar(self, parameter_list):
        pass
    
