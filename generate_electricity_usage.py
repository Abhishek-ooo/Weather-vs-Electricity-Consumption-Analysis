import pandas as pd
import numpy as np

np.random.seed(42)

records = []

usage_id = 1

for building in range(1, 6):
    for weather in range(1, 366):

        temperature = np.random.randint(18,45)

        units = np.random.randint(100,250)

        if temperature > 35:
            units += 40

        peak = round(units * 0.30,2)

        cost = round(units * 8.5,2)

        records.append([
            building,
            weather,
            building,
            units,
            peak,
            cost,
            f"2025-{((weather-1)//30)+1:02}-{((weather-1)%30)+1:02} 12:00:00"
        ])

df = pd.DataFrame(records, columns=[
    "building_id",
    "weather_id",
    "sensor_id",
    "units_consumed",
    "peak_load",
    "cost",
    "record_time"
])

df.to_csv("data/electricity_usage.csv", index=False)

print("electricity_usage.csv created successfully!")