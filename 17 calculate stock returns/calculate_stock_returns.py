#1️⃣7️⃣ Calculate Stock Returns: Given an initial investment and a list of 
#daily stock prices, calculate the percentage return.

def calculate_stock_return(investment, stock_prices):
    initial_price = stock_prices[0]
    final_price = stock_prices[-1]

    percentage_return = ((final_price - initial_price) / initial_price) * 100

    final_investment = investment * (1 + (percentage_return / 100))

    return f'Investment: {investment}\nFinal Investment: {round(final_investment, 2)}\nReturn: {round(percentage_return, 2)}%'

# Taking user input
investment = float(input("Enter the investment amount: "))
stock = input("Enter the stock prices separated by space: ")  

# Correctly converting space-separated numbers into a list of integers
stock_prices = list(map(int, stock.split()))

# Calling the function and printing results
print(calculate_stock_return(investment, stock_prices))


