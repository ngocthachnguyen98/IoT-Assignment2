

class Menu:
    def main(self):
        self.runMenu1()

    def runMenu1(self):
        while(True):
            print()
            print("MENU 1")
            print("1. Login with credentials")
            print("2. Login with facial recognition")
            print("0. Quit")
            selection = input("Select an option: ")
            print()

            if(selection == "1"): # Login with credentials
                break
            elif(selection == "2"): # Login with facial recognition
                break
            elif(selection == "0"): # Quit app
                print("--- Goodbye! ---")
                break
            else:
                print("Invalid input - please try again.")

    def runMenu2(self):
        while(True):
            print()
            print("MENU 2")
            print("1. Unlock Car")
            print("2. Lock Car")
            print("0. Log out")
            selection = input("Select an option: ")
            print()

            if(selection == "1"): # Unlock car
                break
            elif(selection == "2"): # Lock car
                break
            else:
                print("Invalid input - please try again.")


if __name__ == "__main__":
    Menu().main()