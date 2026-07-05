# Functions

Functions make code reusable.
Instead of repeating code, place it inside a function and call it whenever needed.
Example:
def get_high_price(data):
    return data["High"].max()

---
# Parameters

Parameters allow functions to work with different inputs.
Example:
get_stock_data("AAPL")
get_stock_data("MSFT")

---
# Return Values

A function should return a value rather than print it whenever possible.
Good:
return data
Bad:
print(data)
Returning values allows other functions to use the result.

---
# Modules

Python files can be imported into other Python files.
Example:
stock.py
main.py
main.py imports functions from stock.py.