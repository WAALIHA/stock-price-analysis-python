import yfinance as yf

# Download data
data = yf.download("AAPL", start="2024-01-01", end="2025-01-01")

# Calculate returns
data["Return"] = data["Close"].pct_change()

# Average return
average_return = data["Return"].mean()

# Volatility
volatility = data["Return"].std()

print("Average Daily Return: {:.2%}".format(average_return))
print("Volatility:{:.2%}".format(volatility))
