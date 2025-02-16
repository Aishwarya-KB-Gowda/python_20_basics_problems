#1️⃣2️⃣ Stock Price Simulation: Print a sequence of 10 random stock prices
#starting from a given price, where each price fluctuates between -2% and +2%.

import random

start_price = float(input('Enter the starting price: '))
days = 10
stock_prices = [start_price]
for _ in range(days - 1):
    change_percent = random.uniform(-0.02, 0.02)
    new_price = stock_prices[-1] * (1 + change_percent)
    stock_prices.append(new_price)

for i, price in enumerate(stock_prices, start=1):
    print(f'Day {i} : price = {price:.2f}')

