import pandas as pd
import random

issues = [
    "Sensor Failure",
    "Cable Damage",
    "Power Loss",
    "Calibration",
    "Routine Maintenance"
]

status = [
    "Completed",
    "Pending",
    "In Progress"
]

records = []

for i in range(1,21):

    records.append([
        i,
        i,
        f"2025-{random.randint(1,12):02}-{random.randint(1,28):02}",
        random.choice(issues),
        f"Technician {i}",
        random.choice(status)
    ])

df = pd.DataFrame(records, columns=[
    "building_id",
    "sensor_id",
    "maintenance_date",
    "issue",
    "technician",
    "status"
])

df.to_csv("data/maintenance_logs.csv", index=False)

print("maintenance_logs.csv created successfully!")