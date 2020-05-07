#!/usr/bin/env python3

import socket
import requests

def loginWithCredentials(username, password):
    """After the credentials are sent from the Agent Pi via TCP socket. The TCP server will trigger this function to log the user in via Flask API.
    A POST request will be sent to the API. If the credentials are valid, an User ID will be returned and send back to the Agent Pi via TCP socket.
    
    Arguments:
        username {str} -- User's username
        password {str} -- User's password

    Returns:
        int -- User ID if successfully login. None for the otherwise
    """
    data = {
        'username' : username,
        'password' : password 
    }

    # Send the POST request to the API
    response = requests.post("http://127.0.0.1:5000/ap_login", data)

    # Examine the response from the API
    if response.status_code == 200:
        return response.text # Return User ID
    elif response.status_code == 404:
        return None # No User ID is returned

        
HOST = ""    # Empty string means to listen on all IP's on the machine, also works with IPv6.
             # Note "0.0.0.0" also works but only with IPv4.
PORT = 65000 # Port to listen on (non-privileged ports are > 1023).
ADDRESS = (HOST, PORT)

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(ADDRESS)
        s.listen()

        print("Listening on {}...".format(ADDRESS))
        conn, addr = s.accept()
        with conn:
            print("Connected to {}".format(addr))

            while True:
                # Receive credentials and check if it's empty
                credentials = conn.recv(4096) # 4096 is the buffersize
                if(not credentials):
                    break

                print("Received {} bytes of data decoded to: '{}'".format(  len(credentials), 
                                                                            credentials.decode()))
                
                # Data handling - credentials = username + " " + password
                username = credentials.decode().split()[0]
                password = credentials.decode().split()[1]
                print("Received: {}, {}".format(username, password))
                
                # Check with database
                user_id = loginWithCredentials(username, password)

                print("Sending data back.")
                conn.sendall(user_id.encode())
            
            print("Disconnecting from client.")
        print("Closing listening socket.")
    print("Done.")

