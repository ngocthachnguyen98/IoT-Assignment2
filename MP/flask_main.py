# pip3 install flask flask_sqlalchemy flask_marshmallow marshmallow-sqlalchemy
# python3 flask_main.py
from flask import Flask, Blueprint, request, jsonify, render_template, flash, redirect, url_for, session, escape
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json
from flask_api import api, db
from flask_site import site
from flask_bootstrap import Bootstrap
# import MySQLdb
from flask_session import Session
import socket, threading
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons


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
HOST="35.189.9.144"
USER="root"
PASSWORD="iotassignment2"
DATABASE="CarShare"


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{}:{}@{}/{}".format(USER, PASSWORD, HOST, DATABASE)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db.init_app(app)

GoogleMaps(
    app,
    key="AIzaSyCvPI5uYTmN5D_phy_drF_B1iCMbem0Uf0"
)

app.register_blueprint(api)
app.register_blueprint(site)

if __name__ == "__main__":
    app.run()
