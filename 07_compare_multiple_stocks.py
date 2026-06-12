import yfinance as yf
import matplotlib.pyplot as plt

stocks = ["AAPL", "MSFT", "NVDA"]

for stock in stocks:
    data = yf.download(stock,
                       start="2024-01-01",
                       end="2025-01-01")

    plt.plot(data["Close"], label=stock)

plt.title("Stock Price Comparison")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()

plt.show()
