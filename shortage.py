import pandas as pd
from prophet import Prophet

df = pd.read_csv("blood_data.csv", parse_dates=["date"])
o_pos = df[df["blood_type"] == "O+"][["date", "units_consumed"]]
o_pos.columns = ["ds", "y"]

# تدريب على كل الداتا
model = Prophet(weekly_seasonality=True, yearly_seasonality=True)
model.fit(o_pos)

# توقع 14 يوم جاي
future = model.make_future_dataframe(periods=14)
forecast = model.predict(future).tail(14)

# بيانات المخزون (أرقام تجريبية، الباك هو اللي هيبعتها بعدين)
current_stock = 120  # المخزون الحالي
daily_donations = 25       # التبرعات المتوقعة في اليوم
safety_threshold = 40      # الحد الأدنى الآمن

stock = current_stock
shortage_day = None

for i, (date, row) in enumerate(forecast.iterrows(), 1):
    consumption = max(row["yhat"], 0)
    stock = stock + daily_donations - consumption
    print(f"يوم {i}: استهلاك متوقع {consumption:.1f} | مخزون {stock:.1f}")
    if stock < safety_threshold and shortage_day is None:
        shortage_day = i

# التنبيه
if shortage_day is None:
    print("🟢 آمن: مفيش نقص متوقع خلال 14 يوم")
elif shortage_day <= 3:
    print(f"🔴 خطر: نقص متوقع بعد {shortage_day} يوم")
else:
    print(f"🟡 انتبه: نقص متوقع بعد {shortage_day} يوم")