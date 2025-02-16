#3️⃣ Simple Interest Calculator: Given principal, rate, and time, calculate the simple interest.
# Formula: Simple Interest = (principal * rate * time)/100
# Get user input
amount = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time_period = input("Enter the time period (M for Months / Y for Years): ").strip().upper()
time = float(input("Enter the time duration: "))

# Convert months to years if needed
if time_period == "M":
    time = time / 12  # Convert months to years
elif time_period == "Y":
    pass  # No conversion needed
else:
    print("Invalid time period! Please enter 'M' for months or 'Y' for years.")
    exit()

# Calculate Simple Interest
interest = (amount * rate * time) / 100
print(f"The simple interest is: {interest:.2f}")
