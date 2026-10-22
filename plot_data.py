import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("blood_data.csv", parse_dates=["date"])

# نختار فصيلة واحدة: O+
o_pos = df[df["blood_type"] == "O+"]

plt.figure(figsize=(12, 5))
plt.plot(o_pos["date"], o_pos["units_consumed"])
plt.title("Daily consumption of O+")
plt.xlabel("Date")
plt.ylabel("Units consumed")
plt.show()