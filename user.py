# This class defines Users
class User:
    username = 'username'
    password = 'password'
    email = 'email@gmail.com'

    # Constructor
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
    
    # Getter
    def getUserName(self):
        return self.username

    def getPassword(self):
        return self.password
    
    def getEmail(self):
        return self.email
    