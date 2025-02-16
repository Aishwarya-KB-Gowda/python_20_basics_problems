#6️⃣ Price Movement Analysis: Given a list of daily closing prices [100, 102, 105, 101, 98], 
# find the largest increase and decrease between consecutive days.

def price_movement_analysis(prices):
    max_increase = float('-inf')  # Initialize to very low value
    max_decrease = float('inf')   # Initialize to very high value

    for i in range(1, len(prices)):
        diff = prices[i] - prices[i - 1]  # Calculate difference

        if diff > max_increase:
            max_increase = diff  # Update max increase
        
        if diff < max_decrease:
            max_decrease = diff  # Update max decrease

    return max_increase, max_decrease

# Taking input as a space-separated string of numbers and converting to a list
price_input = input('Enter the list of prices (space-separated): ')
prices = list(map(int, price_input.split()))  # Convert input string to list of integers

if len(prices) < 2:
    print("Error: At least two prices are required for comparison.")
else:
    max_increase, max_decrease = price_movement_analysis(prices)
    print(f'Largest increase: {max_increase}')
    print(f'Largest decrease: {max_decrease}')

