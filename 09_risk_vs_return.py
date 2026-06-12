import yfinance as yf
import pandas as pd

stocks = ["AAPL", "MSFT", "NVDA"]

print("STOCK ANALYSIS")
print("-" * 50)

for stock in stocks:

    data = yf.download(stock,
                       start="2024-01-01",
                       end="2025-01-01")

    # Daily returns
    data["Return"] = data["Close"].pct_change()

    # Total return
    start_price = data["Close"].iloc[0]
    end_price = data["Close"].iloc[-1]

    total_return = ((end_price - start_price)
                    / start_price) * 100

    # Volatility
    volatility = data["Return"].std() * 100

    print(stock)
    print("Total Return: {:.2f}%".format(float(total_return)))
    print("Volatility: {:.2f}%".format(float(volatility)))
    print()
