import client_TCP
import requests

class Menu:
    """This class consists of 2 menus. One for logging in and the other one is for unlock/lock the car.
    Only when the user has logged in that he/she can unlock/lock the car in the second menu.

    There is a variable called user_id, which will be set once the user logged in. This is also a proof that the user is authenticated.
    
    This class imports client_TCP.py module to send messages to the TCP for specific request.
    """
    user_id = None

    def main(self):
        """This function will start running the first menu, which is for logging in.
        """
        self.runMenu1()


    def runMenu1(self):
        """This menu is for the user to choose whether to enter credentials or to use facial recognition for logging in.
        Once the user logged in, the second menu will let the user decide whether to unlock or lock the car. Also, an User ID will be set in order to trigger unlock/lock car function.

        Option 1: Login with credentials
        Option 2: Login with facial recognition

        Enter 0 to quit
        """
        while(True):
            print()
            print("MENU 1")
            print("1. Login with credentials")
            print("2. Login with facial recognition")
            print("0. Quit")
            selection = input("Select an option: ")
            print()

            if(selection == "1"): # Login with credentials
                self.user_id = self.login()
                
                if self.user_id is not None: 
                    print("You logged in! Your user ID: {}".format(self.user_id))
                    self.runMenu2()
                else: print("Invalid Credentials!")
            elif(selection == "2"): # Login with facial recognition
                break
            elif(selection == "0"): # Quit app
                print("--- Goodbye! ---")
                break
            else:
                print("Invalid input - please try again.")


    def runMenu2(self):
        """This menu is when the user has logged in and the user_id has been set.
        This menu is for the user to unlock/lock the booked car.

        Option 1: Unlock Car
        Option 2: Lock Car

        Enter 0 to log out 
        """
        while(True):
            print("You logged in!")
            print()
            print("MENU 2")
            print("1. Unlock Car")
            print("2. Lock Car")
            print("0. Log out")
            selection = input("Select an option: ")
            print()

            if(selection == "1"): # Unlock car
                unlocked = self.unlockCar()

                if unlocked == "unlocked": print("Car Unlocked!")
                else: print("Unlocking Failed!")
            elif(selection == "2"): # Lock car
                locked = self.lockCar()

                if locked == "locked": print("Car Locked!")
                else: print("Locking Failed!")
            elif(selection == "0"): # Log out
                print("--- Logging out! ---")
                self.user_id = None
                break
            else:
                print("Invalid input - please try again.")


    def login(self):
        """This function will trigger client_TCP.credentialsCheck() and ask the user to enter their credentials to log in.
        
        Returns:
            int -- an User ID if the credentials are valid and None if they are invalid
        """
        print("--- Login ---")
        user_id = client_TCP.credentialsCheck()
        return user_id


    def unlockCar(self):
        """This function will trigger client_TCP.unlockCar() and ask the user to enter their details to unlock.
        
        Returns:
            str -- "unlocked" if successful
        """
        print("--- Unlock Car ---")
        unlocked = client_TCP.unlockCar(self.user_id)
        return unlocked

    def lockCar(self):
        """This function will trigger client_TCP.lockCar() and ask the user to enter their details to lock.
        
        Returns:
            str -- "locked" if successful
        """
        print("--- Lock Car ---")
        locked = client_TCP.lockCar(self.user_id)
        return locked


if __name__ == "__main__":
    Menu().main()
