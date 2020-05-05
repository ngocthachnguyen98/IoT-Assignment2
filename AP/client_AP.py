#!/usr/bin/env python3

import socket
import requests

HOST = input("Enter IP address of Carshare server: ")

# HOST = "0.0.0.0"    # The server's hostname or IP address
PORT = 5000         # The port used by the server
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


def unlockCar(user_id, car_id, begin_time):
    """This function will make a request to unlock the car via the Flask API.
    This function will trigger flask_api.unlockCar().

    Arguments:
        user_id {int} -- User ID of the user who has made the booking
        car_id {int} -- Car ID of the booked car
        begin_time {datetime} -- The beginning date and time of the booking

    Returns:
        boolean -- True if the car is successfully unlocked. False for the otherwise
    """
    data = {
        'user_id'   : user_id,
        'car_id'    : car_id,
        'begin_time': begin_time   
    }

    # Send a request to Flask API
    response = requests.put("http://{}:{}/car/unlock".format(HOST, PORT), data)


    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False


def lockCar(user_id, car_id):
    """This function will make a request to lock the car via the Flask API.
    This function will trigger flask_api.lockCar().

    Arguments:
        user_id {int} -- User ID of the user who has made the booking
        car_id {int} -- Car ID of the booked car

    Returns:
        boolean -- True if the car is successfully locked. False for the otherwise
    """
    data = {
        'user_id'   : user_id,
        'car_id'    : car_id
    }

    # Send a request to Flask API
    response = requests.put("http://{}:{}/car/lock".format(HOST, PORT), data)


    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False