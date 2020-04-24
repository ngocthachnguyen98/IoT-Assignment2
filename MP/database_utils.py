import MySQLdb
from passlib.hash import sha256_crypt

"""
TO-DO:
    - Missing try/except
    - Flask API
"""
class DatabaseUtils:
    HOST = "35.244.95.33"
    USER = "root"
    PASSWORD = "password"
    DATABASE = "Carshare"

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
                # Hash password
                hashed_password = sha256_crypt.hash(password)

                # Preparing insert query
                insert_stmt = (
                    "INSERT INTO Users (username, password, email, fname, lname, role)"
                    "VALUES (%s, %s, %s, %s, %s, %s)"
                )
                data = (username, hashed_password, email, fname, lname, role)

                # Execute and commit
                cursor.execute(insert_stmt, data)
                self.connection.commit()
                print("Registered...")
        else: 
            print("The username or email ALREADY EXISTS. Can't be used for registration")


    def login(self, username, password):
        # Verify the username and password in the database
        with self.connection.cursor() as cursor:
            # Retrive hashed/stored password for verification from the entered username
            cursor.execute("SELECT id, password FROM Users WHERE username=(%s)", (username,))
            queryResult = cursor.fetchone()

        if not queryResult: # No row returned
            print("Invalid credentials. Username DOES NOT EXIST.")
            return None
        else: # Row found
            stored_password = queryResult[1]
            verified = sha256_crypt.verify(password, stored_password)

            if verified:
                print("Welcome {}! You logged in.".format(username))
                return queryResult[0] # Return user ID
            else:
                print("Invalid credentials. Wrong password.")
                return None # Return no user ID

    
    def getAllUnbookedCars(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Cars WHERE booked=False")
            queryResult = cursor.fetchall()

        if not queryResult: # No row returned
            return None
        else: # Row found
            return queryResult
    
    def searchCar(self, car_id, make, body_type, colour, seats, location, cost_per_hour):
        with self.connection.cursor() as cursor:
            # Preparing query
            queryStmt = """SELECT * FROM Cars 
                WHERE id = %(car_id)s 
                OR make = %(make)s 
                OR body_type = %(body_type)s 
                OR colour = %(colour)s 
                OR seats = %(seats)s 
                OR location = %(location)s
                OR cost_per_hour = %(cost_per_hour)s
            """

            filters = {
                'car_id': car_id,
                'make': make,
                'body_type': body_type,
                'colour': colour,
                'seats': seats,
                'location': location,
                'cost_per_hour': cost_per_hour
            }

            # Execute car search
            cursor.execute(queryStmt, filters)
            queryResult = cursor.fetchall()
        
        if not queryResult: # No row returned
            return None
        else: # Row found
            return queryResult
    
    def makeABooking(self, user_id, car_id, begin_time, return_time):
        with self.connection.cursor() as cursor:
            # Add new booking to the database
            cursor.execute("INSERT INTO Bookings (user_id, car_id, begin_time, return_time, ongoing) VALUES (%s, %s, %s, %s, False)", (user_id, car_id, begin_time, return_time))#adds booking to bookings table
            inserted_row_count = cursor.rowcount
            print("Inserted {} row in Bookings table".format(inserted_row_count))

            # Update car's availability
            cursor.execute("UPDATE Cars SET booked = True WHERE id = %(car_id)s", {'car_id': car_id})
            updated_row_count = cursor.rowcount
            print("Updated {} row in Cars table".format(updated_row_count))
            
            self.connection.commit()
            print("Booking Completed...")
    
    def cancelABooking(self, user_id, car_id, begin_time):
        with self.connection.cursor() as cursor:
            # Delete the targeted booking from Bookings table
            cursor.execute("DELETE FROM Bookings WHERE user_id=(%s) AND car_id=(%s) AND begin_time=(%s)", (user_id, car_id, begin_time))
            deleted_row_count = cursor.rowcount
            print("Deleted {} row from Bookings table".format(deleted_row_count))

            # Update car's availability
            cursor.execute("UPDATE Cars SET booked = False WHERE id = %(car_id)s", {'car_id': car_id})
            updated_row_count = cursor.rowcount
            print("Updated {} row in Cars table".format(updated_row_count))
            
            self.connection.commit()
            print("Cancelling Completed...")
    
    def getUserHistory(self, user_id):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Histories WHERE user_id=%(user_id)s", {'user_id': user_id})
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
    