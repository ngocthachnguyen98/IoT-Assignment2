import MySQLdb

# MISSING TRY/EXCEPT
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
                print("Inserted...")

                # Return True if insert successfully
                return cursor.rowcount == 1
        else: 
            print("The username or email ALREADY EXISTS. Can't be used for registration")
            pass


    def login(self, parameter_list):
        pass
    
    def showAllUnbookedCars(self, parameter_list):
        pass
    
    def searchCar(self, parameter_list):
        pass
    
    def makeABooking(self, parameter_list):
        pass
    
    def cancelABooking(self, parameter_list):
        pass
    
    def showUserHistory(self, parameter_list):
        pass
    
    """PART B"""
    def showCarLocations(self, parameter_list):
        pass

    def unlockCar(self, parameter_list):
        pass
    
    def lockCar(self, parameter_list):
        pass
    