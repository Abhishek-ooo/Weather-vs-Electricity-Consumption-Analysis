import pandas as pd
import numpy as np

# Generate 365 days of weather data
dates = pd.date_range(start="2025-01-01", periods=365)

weather = pd.DataFrame({
    "record_date": dates,
    "temperature": np.random.randint(18, 45, size=365),
    "humidity": np.random.randint(30, 95, size=365),
    "rainfall": np.round(np.random.uniform(0, 40, size=365), 2),
    "wind_speed": np.round(np.random.uniform(2, 20, size=365), 2),
    "weather_condition": np.random.choice(
        ["Sunny", "Cloudy", "Rainy", "Foggy"],
        size=365
    )
})

weather.to_csv("data/weather.csv", index=False)

print("weather.csv created successfully!")