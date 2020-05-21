import unittest
import client_TCP
import socket
import server_TCP
import requests


PORT = 65000
HOST = "Enter IP address of Carshare server"
ADDRESS = (HOST, PORT)


# make a test server




# send dummy file from ap to mp




# print the file in mp (check if received)




# send the crendentials back to ap





class MyTestCase(unittest.TestCase):
    def test_credentialsCheck(self):
# test if the connection function between AP and MP is working
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(ADDRESS)
            self.assertTrue(s.connect)
# test for if the validation process will break if not enough credential is provided

# test for the login function

# test if the function disconnect correctly when validation complete

if __name__ == '__main__':
    unittest.main()
