import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abhi@4545",
    database="weather_electricity_db"
)

query = """
SELECT
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

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()

connection.close()