# Importing module
import mysql.connector
import webbrowser

# Creating connection object
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "password",
    database = "xenon"
)

# Printing the connection object
cursor = mydb.cursor()
#cursor.execute("CREATE DATABASE xenon")
#cursor.execute("CREATE TABLE data (name VARCHAR(255), username VARCHAR(255),email VARCHAR(200), subject VARCHAR(200), message VARCHAR(200))")
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)
