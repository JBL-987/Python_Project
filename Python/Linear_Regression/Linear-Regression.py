import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

Data = {
    "Customer": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    "Number_Of_Cases": [52, 64, 73, 85, 95, 103, 116, 121, 143, 157, 161, 184, 202, 218, 243, 254, 267, 275, 287, 298],
    "Delivery_Time": [32.1, 34.8, 36.2, 37.8, 37.8, 39.7, 38.5, 41.9, 44.2, 47.1, 43.0, 49.4, 57.2, 56.8, 60.6, 61.2, 58.2, 63.1, 65.6, 67.3],
}

df = pd.DataFrame(Data)

df = df.sort_values(by="Number_Of_Cases")

x = df["Number_Of_Cases"].values.reshape(-1, 1)
y = df["Delivery_Time"].values

model = linear_model.LinearRegression()
model.fit(x, y)

y_pred = model.predict(x)
residual = y - y_pred
delivery_time_150 = model.predict([[150]])
r2 = model.score(x, y)

plt.figure(figsize=(10, 6))
plt.grid(True)
plt.scatter(x, y, color="blue", label="Actual Data", marker="o")
plt.plot(x, y_pred, color="red", label="Regression Line", linewidth=2)
plt.xlabel("Number Of Cases")
plt.ylabel("Delivery Time")
plt.title("Delivery Time vs Number of Cases")
plt.scatter([[150]], delivery_time_150, color="green", s=50, label="Prediction (150 cases)")
plt.legend(fontsize=12)
print(f'R-squared: {r2:.4f}')
print(f'residual: {residual}')
print(f'Predicted Delivery Time for 150 cases: {delivery_time_150[0]:.2f} hours')
plt.show()