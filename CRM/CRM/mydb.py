import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Shrestha90@"
)

# prepare a cursor object using cursor() method
cursorObject = dataBase.cursor()

# Create a database
try:
    cursorObject.execute("CREATE DATABASE dcrud")
except:
    print("Database Already exists.")
else:
    print("Database created successfully")
