# This class defines Users
import idGenerator
# User 
class User:
    id = 0
    username = 'username'
    password = 'password'
    email = 'email@gmail.com'

    # Constructor
    def __init__(self, username, password, email):
        self.id = idGenerator.userIdGenerator
        self.username = username
        self.password = password
        self.email = email
        # sql command to add to table here
    
    # Getter
    def getUserName(self):
        return self.username

    def getPassword(self):
        return self.password
    
    def getEmail(self):
        return self.email
    