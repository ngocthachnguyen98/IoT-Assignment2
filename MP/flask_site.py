from flask import Flask, Blueprint, request, jsonify, render_template, flash, redirect, url_for, session, escape
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json
from flask import current_app as app

site = Blueprint("site", __name__)

# CLIENT WEB PAGES

# Welcome page
@site.route('/')
def index():
    return render_template('index.html')


# Register page
@site.route('/register')
def registerPage():
    return render_template('register.html')


# Login page
@site.route('/login')
def loginPage():
    return render_template('login.html')


# Home page
@site.route('/home')
def homePage():
    return render_template('home.html')


# Car Search page
@site.route('/car/search')
def carSearchPage():
    return render_template('car_search.html')


