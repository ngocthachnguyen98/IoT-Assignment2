import client_AP

class Menu:
    user_id = None

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
                self.user_id = self.login()
                
                if self.user_id is not None: self.runMenu2
                else: print("Invalid Credentials!")
            elif(selection == "2"): # Login with facial recognition
                break
            elif(selection == "0"): # Quit app
                print("--- Goodbye! ---")
                break
            else:
                print("Invalid input - please try again.")

    def runMenu2(self):
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

                if unlocked: print("Car Unlocked!")
                else: print("Unlocking Failed!")
            elif(selection == "2"): # Lock car
                locked = self.lockCar()

                if unlocked: print("Car Locked!")
                else: print("Locking Failed!")
            else:
                print("Invalid input - please try again.")

    def login(self): # A user ID will be returned if validated
        print("--- Login ---")
        user_id = client_AP.credentialsCheck()
        return user_id

    def unlockCar(self):
        print("--- Unlock Car ---")
        user_id     = self.user_id
        car_id      = input("Enter your car ID: ")
        begin_time  = input("Enter your begin time (YYYY-MM-DD HH:MM:SS): ")

        response = client_AP.unlockCar(user_id, car_id, begin_time)

        if response:
            return True
        else: return False
    

    def lockCar(self):
        print("--- Lock Car ---")
        user_id     = self.user_id
        car_id      = input("Enter your car ID: ")

        
        response = client_AP.lockCar(user_id, car_id)


        if response:
            return True
        else: return False


if __name__ == "__main__":
    Menu().main()