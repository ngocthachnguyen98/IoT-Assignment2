from database_utils import DatabaseUtils
from datetime import datetime

class Menu:

    user_id = None

    def main(self):
        
         self.runMenu1()

    def runMenu1(self):
        
        while(True):
            print()
            print("MENU 1")
            print("1. Register")
            print("2. Login")
            print("0. Quit")
            selection = input("Select an option: ")
            print()

            if(selection == "1"): # Register
                with DatabaseUtils() as db:
                    # To skip prompting, uncomment the line below:
                    #db.register("user100", "pw100", "user100@carshare.com", "Thach", "Nguyen", "Customer")
                    
                    self.register()
            elif(selection == "2"): # Login
                with DatabaseUtils() as db:
                    # Set user ID for better query in other tables
                    self.user_id = self.login()
                    print("Your user_id is set: {}".format(self.user_id))

                    if self.user_id != None:
                        self.runMenu2()
                    else:
                        print("Re-run Menu 1...")
            elif(selection == "0"): # Quit app
                print("--- Goodbye! ---")
                break
            else:
                print("Invalid input - please try again.")

    def runMenu2(self):
        while(True):
            print()
            print("MENU 2")
            print("1. Make a Booking")
            print("2. Cancel a Booking")
            print("3. Show unbooked cars")
            print("4. Car search")
            print("5. View your history")
            print("0. Log out")
            selection = input("Select an option: ")
            print()

            if(selection == "1"): # Make a booking
                print("--- Make a Booking ---")
                self.makeABooking()
                
            elif(selection == "2"): # Cancel a booking
                print("--- Cancel a Booking ---")
                self.cancelABooking()
                
            elif(selection == "3"): # Show unbooked car
                print("--- Show unbooked car ---")
                print()
                break
            elif(selection == "4"): # Car search
                print("--- Car search ---")
                print()
                break
            elif(selection == "5"): # View user history
                self.viewUserHistory()
            elif(selection == "0"): # Log out
                print("--- Logged out! ---")
                break
            else:
                print("Invalid input - please try again.")

    def register(self):
        print("--- Register ---")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        email = input("Enter your email: ")
        fname = input("Enter your first name: ")
        lname = input("Enter your last name: ")
        role = input("Enter your role: ")

        with DatabaseUtils() as db:
            db.register(username, password, email, fname, lname, role)

    def login(self):
        print("--- Login ---")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        
        with DatabaseUtils() as db:
            return db.login(username, password)

    def viewUserHistory(self):
        print("--- View your history ---")
        
        with DatabaseUtils() as db:
            user_history = db.getUserHistory(self.user_id)

            if not user_history: # No row returned
                print("There is nothing to see in your histories.")
            else: # Row(s) found
                print("{:<15} {:<30} {}".format("Car ID", "Begin Time", "Return Time"))

                for row in user_history:
                    begin_time = row[3].strftime("%d/%m/%Y, %H:%M:%S") # Convert MySQL datetime type to Python string type
                    return_time = row[4].strftime("%d/%m/%Y, %H:%M:%S") # Convert MySQL datetime type to Python string type

                    print("{:<15} {:<30} {}".format(row[2], begin_time, return_time)) # Display Car ID, Begin and Return Time

    
    def makeABooking(self):
        print("Unbooked cars are shown below: ")
        with DatabaseUtils() as db:
            db.showAllUnbookedCars()
        
        print("Enter Details below: ")
        user_id = self.user_id
        car_id = int(input("Enter a car_id which is the first item as seen from the car list: "))
        
        begin_time = input("Enter the date and time in format ex. 2011-04-12 03:00:00  : ")
        converted_begin_time = datetime.strptime(begin_time, "%Y-%m-%d %H:%M:%S")
        return_time = input("Enter the date and time in format ex. 2011-04-12 03:00:00  : ")
        converted_return_time = datetime.strptime(return_time, "%Y-%m-%d %H:%M:%S")
        ongoing = False

        with DatabaseUtils() as db:
            db.makeABooking(user_id, car_id, converted_begin_time, converted_return_time, ongoing)


    def cancelABooking(self):
        user_id = int(input("Enter user id: "))
        car_id = int(input("Enter car id: "))
        begin_time =  input("Enter the date and time in format ex. 2011-04-12 03:00:00  : ")
        converted_begin_time = datetime.strptime(begin_time, "%Y-%m-%d %H:%M:%S")

        with DatabaseUtils() as db:
            db.cancelABooking(user_id, car_id, converted_begin_time) 




        

if __name__ == "__main__":
    Menu().main()