from database_utils import DatabaseUtils

class Menu:
    def main(self):
        self.runMenu()

    def runMenu(self):
        while(True):
            print()
            print("1. Register Example")
            print("0. Quit")
            selection = input("Select an option: ")
            print()

            if(selection == "1"):
                with DatabaseUtils() as db:
                    db.register("user100", "pw100", "user100@carshare.com", "Thach", "Nguyen", "Customer")
            elif(selection == "0"):
                print("Goodbye!")
                break
            else:
                print("Invalid input - please try again.")

if __name__ == "__main__":
    Menu().main()