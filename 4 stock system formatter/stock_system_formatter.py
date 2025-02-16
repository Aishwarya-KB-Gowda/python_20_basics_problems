#4️⃣ Stock Symbol Formatter: Given a stock symbol like "apple inc", convert it into 
# uppercase and replace spaces with _ (e.g., "APPLE_INC").

def stock_symbol_formatter(stock_symbol):
    stock_symbol = stock_symbol.strip()
    return stock_symbol.upprer().replace(' ','_')

symbol = input('Enter the stock symbol:').strip()

if symbol :
    converted_symbol = stock_symbol_formatter(symbol)
    print(f'The converted stock symbol is {converted_symbol}')
else:
    print('Invalid stock symbol, Enter the correct one')