#1️⃣5️⃣ Simple Moving Average (SMA) Calculator: Write a function that takes
# a list of closing prices and a window size, then calculates the SMA.
def sma_calculator(prices, window):
    if len(prices) < window:
        print("Error: the working window is larger than the list of prices")
        return []
     
    sma = []
    for i in range(len(prices) - window + 1):
        window_avg = sum(prices[i:i+window]) / window
        sma.append(round(window_avg, 2))
    return sma

input_prices = input("Enter the list of closing prices separated by space: ")
prices = list(map(float, input_prices.split()))
window_size = int(input("Enter the window size: "))

sma = sma_calculator(prices, window_size)
print(f' The simple moving average(SMA) is {sma}')
