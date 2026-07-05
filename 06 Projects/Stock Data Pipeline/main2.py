import yfinance as yf

ticker = input("Enter stock ticker: ").upper()

stock = yf.Ticker(ticker)

data = stock.history(period="5d")

close_price = data["Close"].iloc[-1]
highest_price = data["High"].max()
lowest_price = data["Low"].min()

print("\nLast Closing Price:")
print(f"${close_price:.2f}")

print("\nHighest Price:")
print(f"${highest_price:.2f}")

print("\nLowest Price:")
print(f"${lowest_price:.2f}")