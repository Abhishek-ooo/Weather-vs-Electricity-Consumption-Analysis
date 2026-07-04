import pandas as pd

sensor_types = [
    "Smart Meter",
    "Digital Meter",
    "IoT Sensor",
    "Power Analyzer"
]

manufacturers = [
    "Siemens",
    "ABB",
    "Schneider",
    "Honeywell"
]

data = []

for i in range(1, 51):
    data.append([
        f"SENSOR-{i:03}",
        sensor_types[i % len(sensor_types)],
        manufacturers[i % len(manufacturers)],
        f"2024-{(i%12)+1:02}-15",
        "Active"
    ])

df = pd.DataFrame(data, columns=[
    "sensor_name",
    "sensor_type",
    "manufacturer",
    "installation_date",
    "status"
])

df.to_csv("data/sensors.csv", index=False)

print("sensors.csv created successfully!")