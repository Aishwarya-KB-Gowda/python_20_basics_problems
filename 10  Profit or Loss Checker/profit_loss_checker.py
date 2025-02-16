#🔟 Profit or Loss Checker: Ask the user for cost price and selling price of a stock. 
# Print whether they made a profit, loss, or no gain/loss.

# Profit or Loss Checker

cost_price = float(input('Enter the cost price of the stock: '))
selling_price = float(input('Enter the selling price of the stock: '))

profit_loss = selling_price - cost_price

if profit_loss > 0:
    print(f'You made a profit of {profit_loss:.2f}')
elif profit_loss < 0:
    print(f'You made a loss of {abs(profit_loss):.2f}') #abs() function returns the absolute value of the argument ,eg. abs(-5) = 5
else:
    print("You made no gain or loss.")
