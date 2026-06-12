import yfinance as yf

# Download data
data = yf.download("AAPL", start="2024-01-01", end="2025-01-01")

# Calculate returns
data["Return"] = data["Close"].pct_change()

# Best and worst trading days
best_day = data["Return"].idxmax()
worst_day = data["Return"].idxmin()

best_return = data["Return"].max()
worst_return = data["Return"].min()

print("Best Trading Day:", best_day.date())
print("Return:", "{:.2%}".format(best_return))

print()

print("Worst Trading Day:", worst_day.date())
print("Return:", "{:.2%}".format(worst_return))
