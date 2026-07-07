import yfinance as yf
import matplotlib.pyplot as plt

# Stock Data-------------------------------------------
def get_stock_data(ticker, period):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


# Statistics-------------------------------------------
def get_last_close(data):
    return data["Close"].iloc[-1]

def get_high_price(data):
    return data["High"].max()

def get_low_price(data):
    return data["Low"].min()

def get_average_volume(data):
    return data["Volume"].mean()

def get_volatility(data):
    return data["Daily Return"].std()


# Feature Engineering-------------------------------------------
def add_price_change(data):
    data["Price Change"] = data["Close"].diff()
    return data

def add_daily_returns(data):
    data["Daily Return"] = data["Close"].pct_change()
    return data


# Trend Indicators-------------------------------------------
def add_moving_average(data):
    data["5-Day MA"] = data["Close"].rolling(window=5).mean()
    return data

def add_exponential_moving_average(data):
    data["5-Day EMA"] = data["Close"].ewm(span=5, adjust=False).mean()
    return data


# Momentum Indicators-------------------------------------------
def add_gains(data):
    data["Gain"] = data["Price Change"].clip(lower=0)
    return data

def add_losses(data):
    data["Loss"] = -data["Price Change"].clip(upper=0)
    return data

def add_average_gain(data):
    data["Average Gain"] = data["Gain"].rolling(window=14).mean()
    return data

def add_average_loss(data):
    data["Average Loss"] = data["Loss"].rolling(window=14).mean()
    return data

def add_relative_strength(data):
    data["Relative Strength"] = data["Average Gain"] / data["Average Loss"]
    return data

def add_rsi(data):
    data["14-day RSI"] = 100 - (100 / (1 + data["Relative Strength"]))
    return data


# MACD--------------------------------------------------------
def add_macd(data):
    data["12-Day EMA"] = data["Close"].ewm(span=12, adjust=False).mean()
    data["26-Day EMA"] = data["Close"].ewm(span=26, adjust=False).mean()
    data["MACD"] = data["12-Day EMA"] - data["26-Day EMA"]
    return data


def add_signal_line(data):
    data["Signal Line"] = data["MACD"].ewm(span=9, adjust=False).mean()
    return data


def add_macd_histogram(data):
    data["MACD Histogram"] = data["MACD"] - data["Signal Line"]
    return data


# Visualization-----------------------------------------------
def plot_technical_dashboard(data):

    fig, (ax1, ax2, ax3) = plt.subplots(
        3,
        1,
        figsize=(14, 10),
        sharex=True,
        gridspec_kw={"height_ratios": [3, 1, 2]}
    )

    # -----------------------------
    # PRICE
    # -----------------------------
    ax1.plot(
        data.index,
        data["Close"],
        label="Close",
        linewidth=2
    )

    ax1.plot(
        data.index,
        data["5-Day MA"],
        label="5-Day SMA",
        linewidth=2
    )

    ax1.plot(
        data.index,
        data["5-Day EMA"],
        label="5-Day EMA",
        linewidth=2
    )

    ax1.set_title("Technical Analysis Dashboard")
    ax1.set_ylabel("Price ($)")
    ax1.grid(True)
    ax1.legend()

    # -----------------------------
    # VOLUME
    # -----------------------------
    ax2.bar(
        data.index,
        data["Volume"],
        label="Volume"
    )

    ax2.set_ylabel("Volume")
    ax2.set_title("Volume")
    ax2.grid(True)

    # -----------------------------
    # MACD
    # -----------------------------
    ax3.plot(
        data.index,
        data["MACD"],
        label="MACD",
        linewidth=2
    )

    ax3.plot(
        data.index,
        data["Signal Line"],
        label="Signal Line",
        linewidth=2
    )

    ax3.bar(
        data.index,
        data["MACD Histogram"],
        label="Histogram"
    )

    ax3.set_ylabel("MACD")
    ax3.set_xlabel("Date")
    ax3.set_title("MACD")
    ax3.grid(True)
    ax3.legend()
    colors = [
    "green" if x >= 0 else "red"
    for x in data["MACD Histogram"]]

    ax3.bar(
    data.index,
    data["MACD Histogram"],
    color=colors)

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
