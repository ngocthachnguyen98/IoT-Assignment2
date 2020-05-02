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

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
Bootstrap(app)

# Set up session for storing session data and showing flashed messages
sess = Session()
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
sess.init_app(app)


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

if __name__ == "__main__":
    app.run(host = "127.0.0.1")
