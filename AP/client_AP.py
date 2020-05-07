#!/usr/bin/env python3

import socket

HOST = input("Enter IP address of Carshare server: ")

# HOST = "0.0.0.0"    # The server's hostname or IP address
PORT = 65000       # The port used by the server
ADDRESS = (HOST, PORT)

def credentialsCheck():
    """This function will ask the user to enter their username and password.
    The credentials will be sent to the Master Pi via TCP socket once there is a connection to it.

    Returns:
        int -- User ID if the credentials are valid to indicate successful login. None if the credentials are invalid.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Connecting to {}...".format(ADDRESS))
        s.connect(ADDRESS)
        print("Connected.")

        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if(not username or not password): # if blank input, will break the loop
                break
            
            # Send credentials 
            credentials = "{} {}".format(username, password)
            s.sendall(credentials.encode())


            # Receive data, which is a user ID if validated
            data = s.recv(4096) # 4096 is the buffersize
            print("Received {} bytes of data decoded to: '{}'".format(  len(data), 
                                                                        data.decode()))
            return data.decode()
        
        print("Disconnecting from server.")
    print("Done.")
