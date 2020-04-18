"""
This Seeder class is for migrating data to the MySQL database
"""

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


class Seeder:

	def seedUsersTable():
		"""
		A list of queries will be executed to populate Users table with 2 Admins, 3 Engineers and 5 Customers.
		"""        
		# List of 10 queries to be executed
		queries = [
			"INSERT INTO Users (username, password, email, fname, lname, role) VALUES ('User1', 'pw1', 'user1@carshare.com', 'Adams', 'Ada', 'Admin')",
			"INSERT INTO Users (username, password, email, fname, lname, role) VALUES ('User2', 'pw2', 'user2@carshare.com', 'Baker', 'Bak', 'Admin')",
			"INSERT INTO Users (username, password, email, fname, lname, role) VALUES ('User3', 'pw3', 'user3@carshare.com', 'Clark', 'Cla', 'Engineer')",
			"INSERT INTO Users (username, password, email, fname, lname, role) VALUES ('User4', 'pw4', 'user4@carshare.com', 'Davis', 'Dav', 'Engineer')",
			"INSERT INTO Users (username, password, email, fname, lname, role) VALUES ('User5', 'pw5', 'user5@carshare.com', 'Evans', 'Eva', 'Engineer'')",
			"INSERT INTO Users (username, password, email, fname, lname, role) VALUES ('User6', 'pw6', 'user6@carshare.com', 'Frank', 'Fra', 'Customer')",
			"INSERT INTO Users (username, password, email, fname, lname, role) VALUES ('User7', 'pw7', 'user7@carshare.com', 'Ghosh', 'Gho', 'Customer')",
			"INSERT INTO Users (username, password, email, fname, lname, role) VALUES ('User8', 'pw8', 'user8@carshare.com', 'Hills', 'Hil', 'Customer')",
			"INSERT INTO Users (username, password, email, fname, lname, role) VALUES ('User9', 'pw9', 'user9@carshare.com', 'Irwin', 'Irw', 'Customer'')",
			"INSERT INTO Users (username, password, email, fname, lname, role) VALUES ('User10', 'pw10', 'user10@carshare.com', 'Jones', 'Jon', 'Customer')"
		]

		try:
			# Establish connection with MySQL database
			connection = mysql.connector.connect(host='localhost',
											database='carshare',
											user='root',
											password='pynative@#29')

			# Insert rows
			cursor = connection.cursor()
			for q in queries:
				cursor.execute(q)

			# Commit changes
			connection.commit()
			print("{} records inserted successfully into Users table".format(cursor.rowcount))

			cursor.close()

		except mysql.connector.Error as error:
			print("Failed to insert record into Users table {}".format(error))

		finally:
			if (connection.is_connected()):
				connection.close()
				print("MySQL connection is closed")

	def seedCarsTable():
		"""
		A list of queries will be executed to populate Cars table with 6 Toyatas and 4 Hondas.
		""" 
		# List of 10 queries to be executed 
		queries = [
			"INSERT INTO Cars (make, body_type, colour, seats, location, cost_per_hour, booked) VALUES ('Toyota', 'Sedan', 'Black', '5', '-37.814, 144.96332', 10.50,  False)",
			"INSERT INTO Cars (make, body_type, colour, seats, location, cost_per_hour, booked) VALUES ('Toyota', 'Sedan', 'Red', '5', '-37.814, 144.96332', 10.50,  False)",
			"INSERT INTO Cars (make, body_type, colour, seats, location, cost_per_hour, booked) VALUES ('Toyota', 'SUV', 'Black', '7', '-33.865143, 151.209900', 15.50,  False)",
			"INSERT INTO Cars (make, body_type, colour, seats, location, cost_per_hour, booked) VALUES ('Toyota', 'SUV', 'Red', '7', '-33.865143, 151.209900', 15.50,  False)",
			"INSERT INTO Cars (make, body_type, colour, seats, location, cost_per_hour, booked) VALUES ('Toyota', 'Van', 'Black', '10', '-35.282001, 149.128998', 20.50,  False)",
			"INSERT INTO Cars (make, body_type, colour, seats, location, cost_per_hour, booked) VALUES ('Toyota', 'Van', 'Red', '10', '-35.282001, 149.128998', 20.50,  False)",
			"INSERT INTO Cars (make, body_type, colour, seats, location, cost_per_hour, booked) VALUES ('Honda', 'Sedan', 'White', '5', '-35.282001, 149.128998', 12.50,  False)",
			"INSERT INTO Cars (make, body_type, colour, seats, location, cost_per_hour, booked) VALUES ('Honda', 'Sedan', 'Blue', '5', '-35.282001, 149.128998', 12.50,  False)",
			"INSERT INTO Cars (make, body_type, colour, seats, location, cost_per_hour, booked) VALUES ('Honda', 'SUV', 'White', '7', '-33.865143, 151.209900', 19.50,  False)",
			"INSERT INTO Cars (make, body_type, colour, seats, location, cost_per_hour, booked) VALUES ('Honda', 'SUV', 'Blue', '7', '-35.282001, 149.128998', 19.50,  False)"
		]

		try:
			# Establish connection with MySQL database
			connection = mysql.connector.connect(host='localhost',
												database='carshare',
												user='root',
												password='pynative@#29')

			# Insert rows
			cursor = connection.cursor()
			for q in queries:
				cursor.execute(q)
		
			# Commit changes
			connection.commit()
			print("{} records inserted successfully into Cars table".format(cursor.rowcount))

			cursor.close()

		except mysql.connector.Error as error:
			print("Failed to insert record into Cars table {}".format(error))

		finally:
			if (connection.is_connected()):
				connection.close()
				print("MySQL connection is closed")

	def seedHistoriesTable():
		"""
		A list of queries will be executed to populate Histories table (2 histories).
		""" 
		# List of 2 queries to be executed 
		queries = [
			"INSERT INTO Histories (user_id, car_id, begin_time, return_time) VALUES (6, 1, \'2020-04-01 08:00:00\', \'2020-04-01 09:00:00\')",
			"INSERT INTO Histories (user_id, car_id, begin_time, return_time) VALUES (7, 2, \'2020-03-01 18:00:00\', \'2020-03-01 19:00:00\')"
		]

		try:
			# Establish connection with MySQL database
			connection = mysql.connector.connect(host='localhost',
												database='carshare',
												user='root',
												password='pynative@#29')

			# Insert rows
			cursor = connection.cursor()
			for q in queries:
				cursor.execute(q)
		
			# Commit changes
			connection.commit()
			print("{} records inserted successfully into Histories table".format(cursor.rowcount))

			cursor.close()

		except mysql.connector.Error as error:
			print("Failed to insert record into Histories table {}".format(error))

		finally:
			if (connection.is_connected()):
				connection.close()
				print("MySQL connection is closed")

	def seed():
		seedUsersTable()
		seedCarsTable()
		seedHistoriesTable()