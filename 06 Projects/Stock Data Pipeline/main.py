from stock import (
    get_stock_data,
    get_last_close,
    get_high_price,
    get_low_price,
    get_average_volume,
    plot_technical_dashboard,
    plot_volume,
    add_daily_returns,
    add_moving_average,
    add_20_day_moving_average,
    add_exponential_moving_average,
    get_volatility,
    add_price_change,
    add_gains,
    add_losses,
    add_average_gain,
    add_average_loss,
    add_relative_strength,
    add_rsi,
    add_macd,
    add_signal_line,
    add_macd_histogram,
    add_standard_deviation,
    add_upper_bollinger_band,
    add_lower_bollinger_band
)

valid_periods = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]

ticker = input("Enter stock ticker: ").upper()
print(f"Available time periods:  {', '.join(valid_periods)}")
period = input("Enter time period: ").lower()
if period not in valid_periods:
    print("Invalid time period. Please choose from the available options.")
    print(f"Available time periods:  {', '.join(valid_periods)}")
    exit()

data = get_stock_data(ticker, period)

# Price calculations
data = add_price_change(data)
data = add_daily_returns(data)

# Momentum indicators
data = add_gains(data)
data = add_losses(data)
data = add_average_gain(data)
data = add_average_loss(data)
data = add_relative_strength(data)
data = add_rsi(data)

# Trend indicators
data = add_moving_average(data)
data = add_exponential_moving_average(data)
data = add_20_day_moving_average(data)

# MACD
data = add_macd(data)
data = add_signal_line(data)
data = add_macd_histogram(data)

# Bollinger Bands
data = add_standard_deviation(data)
data = add_upper_bollinger_band(data)
data = add_lower_bollinger_band(data)


close = get_last_close(data)
high = get_high_price(data)
low = get_low_price(data)
average_volume = get_average_volume(data)
plot_technical_dashboard(data)
volatility = get_volatility(data)


print(f"Last Close: ${close:.2f}")
print(f"Highest Price: ${high:.2f}")
print(f"Lowest Price: ${low:.2f}")
print(f"Average Volume: {average_volume:.0f}")
print(data[["Close", "5-Day MA", "5-Day EMA", "14-day RSI", "MACD", "Signal Line", "MACD Histogram", "Upper Bollinger Band", "Lower Bollinger Band"]].tail())
print(f"Volatility: {volatility:.2%}")