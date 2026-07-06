from stock import (
    get_stock_data,
    get_last_close,
    get_high_price,
    get_low_price,
    get_average_volume,
    plot_price_and_moving_average,
    plot_volume,
    add_daily_returns,
    add_moving_average,
    get_volatility
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
data = add_daily_returns(data)
data = add_moving_average(data)


close = get_last_close(data)
high = get_high_price(data)
low = get_low_price(data)
average_volume = get_average_volume(data)
plot_price_and_moving_average(data)
plot_volume(data)
volatility = get_volatility(data)


print(f"Last Close: ${close:.2f}")
print(f"Highest Price: ${high:.2f}")
print(f"Lowest Price: ${low:.2f}")
print(f"Average Volume: {average_volume:.0f}")
print(data[["Close", "Daily Return", "5-Day MA"]])
print(f"Volatility: {volatility:.2%}")