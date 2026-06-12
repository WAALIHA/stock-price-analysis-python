import yfinance as yf

stocks = ["AAPL", "MSFT", "NVDA"]

print("RISK-RETURN ANALYSIS")
print("-" * 50)

for stock in stocks:

    data = yf.download(stock,
                       start="2024-01-01",
                       end="2025-01-01")

    data["Return"] = data["Close"].pct_change()

    start_price = data["Close"].iloc[0]
    end_price = data["Close"].iloc[-1]

    total_return = ((end_price - start_price)
                    / start_price) * 100

    volatility = data["Return"].std() * 100

    ratio = total_return / volatility

    print(stock)
    print("Return: {:.2f}%".format(float(total_return)))
    print("Volatility: {:.2f}%".format(float(volatility)))
    print("Risk-Return Ratio: {:.2f}".format(float(ratio)))
    print()
