import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

df = pd.read_csv("blood_data.csv", parse_dates=["date"])

# فصيلة O+ بس، وبنغيّر أسماء الأعمدة لأن Prophet بيطلب كده
o_pos = df[df["blood_type"] == "O+"][["date", "units_consumed"]]
o_pos.columns = ["ds", "y"]

# نحتفظ بآخر 14 يوم للاختبار (الموديل مايشوفهمش)
train = o_pos[:-14]
test = o_pos[-14:]

# تدريب الموديل
model = Prophet(weekly_seasonality=True, yearly_seasonality=True)
model.fit(train)

# توقع 14 يوم
future = model.make_future_dataframe(periods=14)
forecast = model.predict(future)

# مقارنة التوقع بالحقيقي
pred = forecast.tail(14)["yhat"].values
actual = test["y"].values
mae = abs(pred - actual).mean()
print("متوسط الخطأ (MAE):", round(mae, 2), "وحدة في اليوم")

# رسم
model.plot(forecast)
plt.show()