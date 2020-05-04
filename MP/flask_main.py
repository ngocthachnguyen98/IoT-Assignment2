# pip3 install flask flask_sqlalchemy flask_marshmallow marshmallow-sqlalchemy
# python3 flask_main.py
from flask import Flask, Blueprint, request, jsonify, render_template, flash, redirect, url_for, session, escape
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json
from flask_api import api, db
from flask_site import site
from flask_bootstrap import Bootstrap
import MySQLdb
from flask_session import Session
import socket, threading

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
Bootstrap(app)

# Set up session for storing session data and showing flashed messages
sess = Session()
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
sess.init_app(app)

# Variables for MySQL database connection on GCloud
# Update HOST and PASSWORD appropriately.
HOST        = "35.201.22.170"
USER        = "root"
PASSWORD    = "password"
DATABASE    = "Carshare"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{}:{}@{}/{}".format(USER, PASSWORD, HOST, DATABASE)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db.init_app(app)

app.register_blueprint(api)
app.register_blueprint(site)

# TCP Server
TCP_IP = ''         # Empty string means to listen on all IP's on the machine
TCP_PORT = 5000     # Port to listen on
ADDRESS = (TCP_IP, TCP_PORT)

def launchServer():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(ADDRESS)

        # Listen for connection
        s.listen(1)
        print("Listening on {}...".format(ADDRESS))


        # Accept connection
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

                # Check with database
                user_id = checkCredentials(username, password)

                print("Sending data back.")
                conn.sendall(user_id.encode())
            
            print("Disconnecting from client.")
        print("Closing listening socket.")
    print("Done.")

def checkCredentials(username, password):
    data = db.session.query(User.id, User.password).filter_by(username = username).first()

    if data is None: # If username does not exist
        return None
    else: # If username exists
        user_id = data[0]
        stored_password = data[1] 

        # Verify password
        if sha256_crypt.verify(password, stored_password): #Validated
            return user_id
        else: # Invalidated
            return None


if __name__ == "__main__":
    # Run a separate thread to accept connection in the background
    t = threading.Thread(target=launchServer)
    t.daemon = True
    t.start()

    app.run(use_reloader=False)
