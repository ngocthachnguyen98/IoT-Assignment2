from database_utils import DatabaseUtils

class Menu:
    def main(self):
        self.runMenu1()

    def runMenu1(self):
        while(True):
            print()
            print("MENU 1")
            print("1. Register Example")
            print("2. Login")
            print("0. Quit")
            selection = input("Select an option: ")
            print()

            if(selection == "1"):
                with DatabaseUtils() as db:
                    db.register("user100", "pw100", "user100@carshare.com", "Thach", "Nguyen", "Customer")
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
                print("MAKE A BOOKING")
                print()
                break
            elif(selection == "2"):
                print("CANCEL A BOOKING")
                print()
                break
            elif(selection == "3"):
                print("SHOW UNBOOKED CARS")
                print()
                break
            elif(selection == "4"):
                print("CAR SEARCH")
                print()
                break
            elif(selection == "5"):
                print("VIEW YOUR HISTORY")
                print()
                break
            elif(selection == "0"):
                print("Logged out!")
                break
            else:
                print("Invalid input - please try again.")

    def login(self):
        print("--- Login ---")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        with DatabaseUtils() as db:
            return db.login(username, password)

if __name__ == "__main__":
    Menu().main()