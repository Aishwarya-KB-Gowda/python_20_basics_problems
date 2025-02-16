#3📌 Problem: Store and Lookup Commodity Prices
#Store commodity prices (like gold, silver, crude oil) using tuples 
# and allow the user to look up the price by entering the commodity name.

commodities = (
    ("GOLD", 58500.75),
    ("SILVER", 72000.50),
    ("CRUDEOIL", 6450.20),
    ("NATURALGAS", 220.75),
    ("COPPER", 710.30)
)

def lookup_price(commodity):
    for item in commodities:
        if item[0] == commodity:
            return item[1]  # Return price if found
    return None  # If not found, return None

commodity = input("Enter the commodity name: ").upper().strip()
price = lookup_price(commodity)

if price is not None:
    print(f'The price of {commodity} is {price}')
else:
    print(f"I am sorry, we don't have the price of {commodity}")
