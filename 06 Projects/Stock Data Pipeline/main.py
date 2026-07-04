import yfinance as yf

ticker = "MSFT"

stock = yf.Ticker(ticker)

data = stock.history(period="1mo")

print(data)