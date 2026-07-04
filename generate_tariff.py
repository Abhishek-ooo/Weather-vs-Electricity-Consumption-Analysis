import pandas as pd

tariff = pd.DataFrame({
    "city": [
        "Delhi",
        "Noida",
        "Gurugram",
        "Faridabad",
        "Ghaziabad"
    ],
    "unit_price": [8.5, 8.2, 8.8, 8.0, 8.3],
    "peak_hour_price": [11.0, 10.5, 11.2, 10.3, 10.7],
    "effective_from": [
        "2025-01-01",
        "2025-01-01",
        "2025-01-01",
        "2025-01-01",
        "2025-01-01"
    ]
})

tariff.to_csv("data/electricity_tariff.csv", index=False)

print("electricity_tariff.csv created successfully!")