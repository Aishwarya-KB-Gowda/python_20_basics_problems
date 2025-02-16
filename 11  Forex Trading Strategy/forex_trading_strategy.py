# 1️⃣1️⃣ Forex Trading Strategy: Ask the user for the Open and Close price of a currency pair. 
# Print "Buy" if the closing price is higher, "Sell" if lower, and "Hold" if unchanged.

# Forex Trading Strategy
open_price = float(input("Enter the open price: "))
close_price = float(input("Enter the close price: "))

price_change = close_price - open_price
percentage_change = (price_change / open_price) * 100  # Calculate percentage change

if close_price > open_price:
    print(f"Buy (Price increased by {percentage_change:.2f}%)")
elif close_price < open_price:
    print(f"Sell (Price decreased by {abs(percentage_change):.2f}%)")
else:
    print("Hold ➖ (No price change)")
