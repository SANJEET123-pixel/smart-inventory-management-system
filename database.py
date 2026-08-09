import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="*****",
    password="******",
    database="smart_inventory"
)

cursor = connection.cursor()

print("Database Connected Successfully!")
