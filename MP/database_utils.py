import MySQLdb

"""
TO-DO:
    - Missing try/except
    - Add input validation scheme
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
    
    def makeABooking(self, parameter_list):
        pass
    
    def cancelABooking(self, parameter_list):
        pass
    
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
    