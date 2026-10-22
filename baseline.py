import pandas as pd

df = pd.read_csv("blood_data.csv", parse_dates=["date"])
o_pos = df[df["blood_type"] == "O+"]["units_consumed"].values

train = o_pos[:-14]
test = o_pos[-14:]

# Baseline: نتوقع إن كل يوم هيبقى زي متوسط آخر 7 أيام
pred = [train[-7:].mean()] * 14

mae = abs(pred - test).mean()
print("Baseline MAE:", round(mae, 2))