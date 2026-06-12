import yfinance as yf
import matplotlib.pyplot as plt

# Download data
data = yf.download("AAPL", start="2024-01-01", end="2025-01-01")

# Calculate daily returns
data["Return"] = data["Close"].pct_change()

# Display first few rows
print(data[["Close", "Return"]].head(10))
