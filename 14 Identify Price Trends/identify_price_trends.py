#1️⃣4️⃣ Identify Price Trends: Given a list of prices [101, 103, 107, 105, 100], 
# check if prices are increasing, decreasing, or mixed.

def identify_price_trends(prices):
    increasing = True
    decreasing = True
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1] :
            decreasing = False
        elif prices[i] < prices[i - 1]:
            increasing = False
        
    if increasing:
        return "increasing"
    elif decreasing:
        return "decreasing"
    else:  
        return "mixed"

prices = input("Enter the prices with separatedly: ")
prices = list(map(int,prices.split()))
print("Trends :",identify_price_trends(prices))
