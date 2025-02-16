#8️⃣ Stock Price Lookup: Create a dictionary where keys are stock symbols
#  (e.g., 'AAPL', 'TSLA') and values are prices. Let users enter a symbol to get the price.

# Indian Stock Market Prices (Sample Data)
stock_prices = {
    'RELIANCE': 2600.50,
    'TCS': 4005.75,
    'HDFCBANK': 1542.60,
    'INFY': 1650.30,
    'ICICIBANK': 1025.45,
    'SBIN': 590.80,
    'BAJFINANCE': 7350.20,
    'HCLTECH': 1305.40,
    'WIPRO': 500.75,
    'TITAN': 3650.10,
    'LT': 3265.90,
    'MARUTI': 10525.35
}

input_stock = input('Enter the stock symbol: ').upper().strip()

if input_stock in stock_prices:
    print(f'The price of {input_stock} is {stock_prices[input_stock]}')
else:
    print('Stock symbol not found in the dictionary')
