from database_utils import DatabaseUtils

class Menu:
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

            if(selection == "1"):
                with DatabaseUtils() as db:
                    # To skip prompting, uncomment the line below:
                    #db.register("user100", "pw100", "user100@carshare.com", "Thach", "Nguyen", "Customer")
                    
                    self.register()
            elif(selection == "2"):
                with DatabaseUtils() as db:
                    logged_in = self.login()

                    if logged_in:
                        self.runMenu2()
                    else:
                        print("Re-run Menu 1...")
            elif(selection == "0"):
                print("Goodbye!")
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

            if(selection == "1"):
                print("--- Make a Booking ---")
                print()
                break
            elif(selection == "2"):
                print("--- Cancel a Booking ---")
                print()
                break
            elif(selection == "3"):
                print("--- Show unbooked car ---")
                print()
                break
            elif(selection == "4"):
                print("--- Car search ---")
                print()
                break
            elif(selection == "5"):
                print("--- View your history ---")
                print()
                break
            elif(selection == "0"):
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

if __name__ == "__main__":
    Menu().main()