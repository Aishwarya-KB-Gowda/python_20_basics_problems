# 1️⃣ Currency Converter: Write a program that converts USD to INR. 
# Take input from the user for USD and convert it using a fixed exchange rate.

#Exchange rate: 1 USD = 86.87 INR
currency_type = input("Enter which currency you want to convert (INR/USD) :").strip().upper() #this two methods are used to remove extra spaces and convert the input to uppercase
amount = float(input("Enter the amount you want to convert :"))
if currency_type == "INR":
    amount_in_usd = round(amount / 86.87,2) # this is the formula to convert INR to USD
    print(f'{amount} INR = {amount_in_usd} USD')
elif currency_type == "USD":
    amount_in_inr = round(amount * 86.87,2) # this is the formula to convert USD to INR
    print(f'{amount} USD = {amount_in_inr} INR')
else:
    print("Invalid currency type")

# I use if-elif-else statement to check the currency type and then convert the amount accordingly.
# and also use round() function to round the amount upto 2 decimal places.