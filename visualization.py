import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abhi@4545",
    database="weather_electricity_db"
)

query = """
SELECT
    w.temperature,
    e.units_consumed
FROM weather w
JOIN electricity_usage e
ON w.weather_id = e.weather_id;
"""

df = pd.read_sql(query, connection)

plt.figure(figsize=(8,5))
plt.scatter(df["temperature"], df["units_consumed"])
plt.title("Temperature vs Electricity Usage")
plt.xlabel("Temperature (°C)")
plt.ylabel("Units Consumed")
plt.grid(True)

plt.show()

connection.close()