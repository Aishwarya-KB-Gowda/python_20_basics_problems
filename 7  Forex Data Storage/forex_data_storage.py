#7️⃣ Forex Data Storage: Store currency pairs (e.g., 'EUR/USD': 1.085, 'GBP/USD': 1.267) 
# in a dictionary and allow the user to query a pair's exchange rate.

forex_rate = {
    'EUR/USD': 1.085,
    'GBP/USD': 1.267,
    'USD/JPY': 149.35,
    'AUD/USD': 0.657,
    'USD/INR': 82.73
}

currency = input('Enter currency pair:').upper().strip().replace(' ', '').replace('/', '').replace('-','')
currency = currency[:3] + '/' + currency[3:]
if currency in forex_rate:
    print(f'currency rate for {currency} is {forex_rate[currency]}')
else:
    print("Invalid currency pair")