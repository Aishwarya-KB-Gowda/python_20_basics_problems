#1️⃣8️⃣ Read Forex Data from CSV: Write a program that reads a CSV file 
#containing forex prices and prints the highest closing price.
import csv

def highest_closing_price(file_path):
    highest_price = float('-inf')  # Use negative infinity for correct comparison
    highest_price_date = None  # Store None in case of an empty file

    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    close_price = float(row['Close'])  # Convert Close price to float

                    if close_price > highest_price:
                        highest_price = close_price
                        highest_price_date = row['Date']
                except ValueError:
                    print(f"Skipping invalid data: {row}")  # Handle any incorrect values

        if highest_price_date:
            return f"Highest close price: {highest_price} on {highest_price_date}"
        else:
            return "No valid data found in the file."

    except FileNotFoundError:
        return "Error: The file was not found. Please check the file path."

csv_file = 'forex_prices.csv'
print(highest_closing_price(csv_file))
