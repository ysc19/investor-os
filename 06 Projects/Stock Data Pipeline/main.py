from stock import (
    get_stock_data,
    get_last_close,
    get_high_price,
    get_low_price,
    get_average_volume,
    plot_closing_price,
    plot_volume,
    add_daily_returns,
    add_moving_average
)

ticker = input("Enter stock ticker: ").upper()

data = get_stock_data(ticker)
data = add_daily_returns(data)
data = add_moving_average(data)


close = get_last_close(data)
high = get_high_price(data)
low = get_low_price(data)
average_volume = get_average_volume(data)
plot_closing_price(data)
plot_volume(data)


print(f"Last Close: ${close:.2f}")
print(f"Highest Price: ${high:.2f}")
print(f"Lowest Price: ${low:.2f}")
print(f"Average Volume: {average_volume:.0f}")
print(data[["Close", "Daily Return", "5-Day MA"]])