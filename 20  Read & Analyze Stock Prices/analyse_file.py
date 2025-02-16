#2️⃣0️⃣ Read & Analyze Stock Prices: Read a stock price file and find the day with the highest
# price volatility.

import csv

input_file = "stock_prices.csv"  # File containing raw stock price data
output_file = "stock_volatility.csv"  # File to store volatility results

def calculate_volatility():
    """Reads stock_prices.csv, calculates volatility, and writes results to stock_volatility.csv"""
    try:
        with open(input_file, mode="r") as file:
            reader = csv.DictReader(file)
            stock_data = list(reader)

            if not stock_data:
                print("Error: The input CSV file is empty.")
                return

            highest_volatility = 0
            most_volatile_day = None
            volatility_data = []

            for row in stock_data:
                try:
                    date = row["Date"]
                    high = float(row["High"])
                    low = float(row["Low"])

                    volatility = round(high - low, 2)
                    volatility_data.append([date, volatility])

                    # Check if this is the highest volatility day
                    if volatility > highest_volatility:
                        highest_volatility = volatility
                        most_volatile_day = date

                except ValueError:
                    print(f"Skipping invalid row: {row}")
                    continue

        # Write volatility results to a new CSV file
        with open(output_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Volatility"])  # Writing headers
            writer.writerows(volatility_data)

        print(f"Stock volatility data saved to {output_file}")
        print(f"The most volatile day was {most_volatile_day} with a volatility of {highest_volatility}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found. Please provide a valid stock prices file.")

# Run the function
calculate_volatility()

            