import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abhi@4545",
    database="weather_electricity_db"
)

cursor = connection.cursor()

print(" Connected to MySQL Successfully")