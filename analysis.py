import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abhi@4545",   # Use your MySQL password
    database="weather_electricity_db"
)

query = """
SELECT
    w.record_date,
    w.temperature,
    w.humidity,
    w.rainfall,
    e.units_consumed,
    e.peak_load,
    e.cost
FROM weather w
JOIN electricity_usage e
ON w.weather_id = e.weather_id;
"""

df = pd.read_sql(query, connection)

print(df.head())

connection.close()