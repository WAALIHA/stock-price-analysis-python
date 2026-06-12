import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("AAPL", start="2024-01-01", end="2025-01-01")

plt.plot(data["Close"])
plt.title("Apple Stock Price")
plt.show()
