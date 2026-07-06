import yfinance as yf
import matplotlib.pyplot as plt


def get_stock_data(ticker, period):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def get_last_close(data):
    return data["Close"].iloc[-1]


def get_high_price(data):
    return data["High"].max()


def get_low_price(data):
    return data["Low"].min()


def get_average_volume(data):
    return data["Volume"].mean()


def plot_technical_analysis(data):
    plt.figure(figsize=(12, 6))
    plt.plot(
        data.index,
        data["Close"],
        label="Closing Price",
        linewidth=2,
    )
    plt.plot(
        data.index,
        data["5-Day MA"],
        label="5-Day Moving Average",
        linewidth=2,
    )
    plt.plot(
        data.index,
        data["5-Day EMA"],
        label="5-Day Exponential Moving Average",
        linewidth=2,
    )
    plt.title("Technical analysis: Price, SMA & EMA")
    #technical analisys = Stock Price vs 5-Day Moving Average and Exponential Moving Average
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.grid(True)
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


def add_daily_returns(data):
    data["Daily Return"] = data["Close"].pct_change()
    return data


def add_moving_average(data):
    data["5-Day MA"] = data["Close"].rolling(window=5).mean()
    return data


def add_exponential_moving_average(data):
    data["5-Day EMA"] = data["Close"].ewm(span=5, adjust=False).mean()
    return data


#def plot_price_and_volume(data):
    #fig, ax1 = plt.subplots(figsize=(12, 6))

    #ax1.set_xlabel("Date")
    #ax1.set_ylabel("Price ($)", color="tab:blue")
    #ax1.plot(data.index, data["Close"], label="Closing Price", color="tab:blue", linewidth=2)
    #ax1.plot(data.index, data["5-Day MA"], label="5-Day Moving Average", color="tab:orange", linewidth=2)
    #ax1.tick_params(axis="y", labelcolor="tab:blue")
    #ax1.legend(loc="upper left")

    #ax2 = ax1.twinx()
    #ax2.set_ylabel("Volume", color="tab:green")
    #ax2.bar(data.index, data["Volume"], alpha=0.3, color="tab:green")
    #ax2.tick_params(axis="y", labelcolor="tab:green")

    #plt.title("Stock Price and Volume")
    #fig.tight_layout()
    #plt.grid()
    #plt.xticks(rotation=45)
    #plt.show()


def get_volatility(data):
    return data["Daily Return"].std()