import yfinance as yf
import matplotlib.pyplot as plt

# Download data
data = yf.download("AAPL", start="2024-01-01", end="2025-01-01")

# Calculate moving averages
data["MA20"] = data["Close"].rolling(window=20).mean()
data["MA50"] = data["Close"].rolling(window=50).mean()

# Plot
plt.figure(figsize=(10,5))

plt.plot(data["Close"], label="Apple Price")
plt.plot(data["MA20"], label="20-Day Moving Average")
plt.plot(data["MA50"], label="50-Day Moving Average")

plt.title("Apple Stock Price with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()

plt.show()
