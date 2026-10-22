import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range("2024-01-01", "2025-12-31")

blood_share = {
    "O+": 0.50, "A+": 0.28, "B+": 0.15, "AB+": 0.04,
    "O-": 0.01, "A-": 0.01, "B-": 0.005, "AB-": 0.005,
}

rows = []
for date in dates:
    base = 40

    if date.month in [6, 7, 8]:
        base *= 1.2

    if date.dayofweek in [3, 4]:
        base *= 0.8

    for blood_type, share in blood_share.items():
        expected = base * share
        consumed = np.random.poisson(expected)
        rows.append([date, blood_type, consumed])

df = pd.DataFrame(rows, columns=["date", "blood_type", "units_consumed"])
df.to_csv("blood_data.csv", index=False)

print(df.head(10))
print("عدد الصفوف:", len(df))