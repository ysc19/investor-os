import yfinance as yf
import matplotlib.pyplot as plt


def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1mo")
    return data


def get_last_close(data):
    return data["Close"].iloc[-1]


def get_high_price(data):
    return data["High"].max()


def get_low_price(data):
    return data["Low"].min()


def get_average_volume(data):
    return data["Volume"].mean()


def plot_closing_price(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data["Close"], marker="o", linestyle="-")
    plt.title("Closing Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Closing Price ($)")
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_volume(data):
    plt.figure(figsize=(10, 5))
    plt.bar(data.index, data["Volume"])
    plt.title("Trading Volume")
    plt.xlabel("Date")
    plt.ylabel("Volume")
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()