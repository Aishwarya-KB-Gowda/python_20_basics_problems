#1️⃣9️⃣ Write Trade Logs: Allow users to enter their trades 
#(symbol, price, quantity) and store them in a CSV file.

import csv

trade_log_file = "trade_logs.csv"
trade_summary_file = "trade_summary.csv"

def write_trade_log(symbol, price, quantity):
    """Writes trade details to the trade_logs.csv file."""
    with open(trade_log_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        
        # Write headers if the file is empty
        if file.tell() == 0:
            writer.writerow(["Symbol", "Price", "Quantity"])
        
        # Write trade data
        writer.writerow([symbol, price, quantity])

    print(f"Trade recorded: {symbol} - {quantity} shares at ${price}")

def generate_trade_summary():
    """Reads trade_logs.csv and generates a summary, then saves it to trade_summary.csv."""
    total_trades = 0
    total_quantity = 0
    total_price = 0.0

    try:
        with open(trade_log_file, mode="r") as file:
            reader = csv.DictReader(file)
            trades = list(reader)

            if not trades:
                print("No trades found in trade log. Summary not created.")
                return

            for trade in trades:
                total_trades += 1
                total_quantity += int(trade["Quantity"])  # Convert to integer
                total_price += float(trade["Price"])  # Convert to float

            avg_price = round(total_price / total_trades, 2) if total_trades > 0 else 0

        # Save summary in another CSV file
        with open(trade_summary_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Total Trades", "Total Quantity", "Average Price"])
            writer.writerow([total_trades, total_quantity, avg_price])

        print(f"Trade summary saved to {trade_summary_file}")

    except FileNotFoundError:
        print("Error: No trade log found. Cannot generate summary.")
    except ValueError:
        print("Error: Invalid data in trade log. Ensure prices and quantities are numbers.")

# Allow the user to enter multiple trades
while True:
    symbol = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
    try:
        price = float(input("Enter trade price: "))  # Ensure valid float
        quantity = int(input("Enter quantity: "))  # Ensure valid integer
    except ValueError:
        print("Invalid input! Please enter numerical values for price and quantity.")
        continue  # Restart the loop

    write_trade_log(symbol, price, quantity)
    
    cont = input("Do you want to enter another trade? (yes/no): ").strip().lower()
    if cont != "yes":
        print("Trade log updated. Generating summary...")
        generate_trade_summary()
        print("Exiting...")
        break
