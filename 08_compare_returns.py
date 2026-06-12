import yfinance as yf

stocks = ["AAPL", "MSFT", "NVDA"]

for stock in stocks:

    data = yf.download(stock,
                       start="2024-01-01",
                       end="2025-01-01")

    start_price = data["Close"].iloc[0]
    end_price = data["Close"].iloc[-1]

    total_return = ((end_price - start_price)
                    / start_price) * 100

    print(stock)
    print("Total Return: {:.2f}%".format(float(total_return)))
    print()
