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
                    # To skip registration prompting, uncomment the line below:
                    #db.register("user200", "pw200", "user200@carshare.com", "Tyler", "Newyen", "Customer")
                    
                    self.register()
            elif(selection == "2"): # Login
                with DatabaseUtils() as db:
                    # To login faster with use1, uncomment the line below:
                    # self.user_id = 6

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
                self.makeABooking()
            elif(selection == "2"): # Cancel a booking
                print("--- Cancel a Booking ---")
                print()
                break
            elif(selection == "3"): # Show unbooked car
                self.showAllUnbookedCar()           
            elif(selection == "4"): # Car search
                self.searchCar()
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

    def searchCar(self):
        print("--- Car search ---")
        car_id = input("Enter car ID for filtering: ")
        make = input("Enter make for filtering: ")
        body_type = input("Enter body type for filtering: ")
        colour = input("Enter colour for filtering: ")
        seats = input("Enter number of seats for filtering: ")
        location = input("Enter location for filtering: ")
        cost_per_hour = input("Enter cost per hour (in AUD) for filtering: ")

        with DatabaseUtils() as db:
            search_result = db.searchCar(car_id, make, body_type, colour, seats, location, cost_per_hour)
            print("--- Search result ---")

            if not search_result: # No row returned
                print("No car found with your entered filters.")
            else: # Row(s) found - Display search result
                print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<30} {:<30} {}".format("Car ID", "Make", "Body type", "Colour", "Seats", "Location", "Cost per hour (AUD)", "Booked"))

                for row in search_result:
                    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<30} {:<30} {}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    def viewUserHistory(self):
        print("--- View your history ---")
        
        with DatabaseUtils() as db:
            user_history = db.getUserHistory(self.user_id)

            if not user_history: # No row returned
                print("There is nothing to see in your histories.")
            else: # Row(s) found - Display user history
                print("{:<15} {:<30} {}".format("Car ID", "Begin Time", "Return Time"))

                for row in user_history:
                    begin_time = row[3].strftime("%d/%m/%Y, %H:%M:%S") # Convert MySQL datetime type to Python string type
                    return_time = row[4].strftime("%d/%m/%Y, %H:%M:%S") # Convert MySQL datetime type to Python string type

                    print("{:<15} {:<30} {}".format(row[2], begin_time, return_time)) # Display Car ID, Begin and Return Time
        
    def showAllUnbookedCar(self):
        print("--- All unbooked cars ---")

        with DatabaseUtils() as db:
            unbooked_cars = db.getAllUnbookedCars()

            if not unbooked_cars: # No row returned
                print("All cars are booked.")
            else: # Row(s) found - Display list of unbooked cars
                print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<40} {}".format("Car ID", "Make", "Body type", "Colour", "Seats", "Location", "Cost per hour (AUD)"))

                for row in unbooked_cars:
                    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<40} {}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6])) 

    def makeABooking(self):
        print("--- Make a Booking ---")
        
        # Show a list of unbooked cars, so that the user can choose from
        self.showAllUnbookedCar()
        print()

        # Prompt for input
        print("Please enter your booking details below")
        car_id = int(input("Enter a car ID: "))
        begin_time =  input("Enter the beginning date and time of the booking (YYYY-MM-DD HH:MM:SS): ")
        return_time =  input("Enter the end date and time of the booking (YYYY-MM-DD HH:MM:SS): ")

        # Add new booking to the database
        with DatabaseUtils() as db:
            db.makeABooking(self.user_id, car_id, begin_time, return_time)

if __name__ == "__main__":
    Menu().main()