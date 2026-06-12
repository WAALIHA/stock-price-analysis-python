import yfinance as yf
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

# Download data
data = yf.download("AAPL", start="2020-01-01", end="2025-01-01")

# Use today's closing price to predict tomorrow's closing price
data["Tomorrow"] = data["Close"].shift(-1)

# Remove missing values
data = data.dropna()

# Features and target
X = data[["Close"]]
y = data["Tomorrow"]

# Split data: 80% training, 20% testing
split = int(len(data) * 0.8)

X_train = X[:split]
X_test = X[split:]

y_train = y[:split]
y_test = y[split:]

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Measure error
rmse = np.sqrt(mean_squared_error(y_test, predictions))

print("RMSE:", round(rmse, 2))

# Plot actual vs predicted prices
plt.figure(figsize=(10, 5))
plt.plot(y_test.index, y_test, label="Actual Price")
plt.plot(y_test.index, predictions, label="Predicted Price")

plt.title("Apple Stock Price Forecast")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()

plt.show()
