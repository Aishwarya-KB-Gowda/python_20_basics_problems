#1️⃣6️⃣ Currency Conversion Function: Write a function that converts any 
#amount from INR to USD and vice versa using a predefined exchange rate.

def currency_converter(amount, currency):
    exchange_rate = 86.76  # Exchange rate (1 USD = 86.76 INR)

    if currency == "INR":
        currency_usd = round(amount / exchange_rate, 2)
        return f'{amount} INR is equal to {currency_usd} USD'

    elif currency == "USD":
        currency_inr = round(amount * exchange_rate, 2)
        return f'{amount} USD is equal to {currency_inr} INR'

    else:
        return "Invalid currency...!"

# Taking user input
input_currency = input("Enter the currency (INR/USD): ").upper().strip()
amount = float(input("Enter the amount you want to convert: "))

# Calling the function and printing the result
result = currency_converter(amount, input_currency)
print(result)
