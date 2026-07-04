import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abhi@4545",
    database="weather_electricity_db"
)

# Fetch data
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
connection.close()

# Create Dashboard
plt.figure(figsize=(15,10))

# 1. Temperature vs Electricity Usage
plt.subplot(2,2,1)
plt.scatter(df["temperature"], df["units_consumed"], color="blue")
plt.title("Temperature vs Electricity Usage")
plt.xlabel("Temperature (°C)")
plt.ylabel("Units Consumed")
plt.grid(True)

# 2. Humidity vs Electricity Usage
plt.subplot(2,2,2)
plt.scatter(df["humidity"], df["units_consumed"], color="green")
plt.title("Humidity vs Electricity Usage")
plt.xlabel("Humidity (%)")
plt.ylabel("Units Consumed")
plt.grid(True)

# 3. Rainfall vs Electricity Usage
plt.subplot(2,2,3)
plt.scatter(df["rainfall"], df["units_consumed"], color="red")
plt.title("Rainfall vs Electricity Usage")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Units Consumed")
plt.grid(True)

# 4. Correlation Heatmap
plt.subplot(2,2,4)
sns.heatmap(
    df[[
        "temperature",
        "humidity",
        "rainfall",
        "units_consumed",
        "peak_load",
        "cost"
    ]].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()

# Summary Statistics
print("\n========== SUMMARY STATISTICS ==========\n")
print(df.describe())