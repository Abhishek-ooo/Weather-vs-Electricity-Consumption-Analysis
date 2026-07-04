import pandas as pd
import mysql.connector

# ----------------------------
# Connect to MySQL
# ----------------------------
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abhi@4545",
    database="weather_electricity_db"
)

cursor = connection.cursor()

# ----------------------------
# Import Buildings
# ----------------------------
buildings = pd.read_csv("data/buildings.csv")

for _, row in buildings.iterrows():
    cursor.execute("""
        INSERT INTO buildings
        (building_name, building_type, city, area_sqft, installation_year)
        VALUES (%s,%s,%s,%s,%s)
    """, (
        row["building_name"],
        row["building_type"],
        row["city"],
        row["area_sqft"],
        row["installation_year"]
    ))

connection.commit()
print("Buildings imported.")

# ----------------------------
# Import Weather
# ----------------------------
weather = pd.read_csv("data/weather.csv")

for _, row in weather.iterrows():
    cursor.execute("""
        INSERT INTO weather
        (record_date, temperature, humidity, rainfall,
         wind_speed, weather_condition)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (
        row["record_date"],
        row["temperature"],
        row["humidity"],
        row["rainfall"],
        row["wind_speed"],
        row["weather_condition"]
    ))

connection.commit()
print("Weather imported.")

# ----------------------------
# Import Sensors
# ----------------------------
sensors = pd.read_csv("data/sensors.csv")

for _, row in sensors.iterrows():
    cursor.execute("""
        INSERT INTO sensors
        (sensor_name, sensor_type, manufacturer,
         installation_date, status)
        VALUES (%s,%s,%s,%s,%s)
    """, (
        row["sensor_name"],
        row["sensor_type"],
        row["manufacturer"],
        row["installation_date"],
        row["status"]
    ))

connection.commit()
print("Sensors imported.")

# ----------------------------
# Import Electricity Tariff
# ----------------------------
tariff = pd.read_csv("data/electricity_tariff.csv")

for _, row in tariff.iterrows():
    cursor.execute("""
        INSERT INTO electricity_tariff
        (city, unit_price, peak_hour_price, effective_from)
        VALUES (%s,%s,%s,%s)
    """, (
        row["city"],
        row["unit_price"],
        row["peak_hour_price"],
        row["effective_from"]
    ))

connection.commit()
print("Tariff imported.")

# ----------------------------
# Import Electricity Usage
# ----------------------------
usage = pd.read_csv("data/electricity_usage.csv")

for _, row in usage.iterrows():
    cursor.execute("""
        INSERT INTO electricity_usage
        (building_id, weather_id,
         units_consumed, peak_load, cost)
        VALUES (%s,%s,%s,%s,%s)
    """, (
        row["building_id"],
        row["weather_id"],
        row["units_consumed"],
        row["peak_load"],
        row["cost"],
    ))

connection.commit()
print("Electricity usage imported.")

# ----------------------------
# Import Maintenance Logs
# ----------------------------
logs = pd.read_csv("data/maintenance_logs.csv")

for _, row in logs.iterrows():
    cursor.execute("""
        INSERT INTO maintenance_logs
        (building_id,sensor_id, maintenance_date,
         issue, technician, status)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (
        row["building_id"],
        row["sensor_id"],
        row["maintenance_date"],
        row["issue"],
        row["technician"],
        row["status"]
    ))

connection.commit()
print("Maintenance logs imported.")

cursor.close()
connection.close()

print("\nAll CSV files imported successfully!")