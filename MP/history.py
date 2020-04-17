"""
This History class is for interaction with Histories table in the MySQL database
"""

import datetime
import idGenerator

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorCode

class History:

    # Part A
    def show_user_history(user_id):
        """
        Show all histories related to a specific user.

        A SELECT query will be executed in Histories table.
        """
        pass