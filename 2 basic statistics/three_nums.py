# 2️⃣ Basic Statistics: Take three numbers as input and calculate 
# the sum, average, maximum, and minimum.

# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compute values once
sum_numbers = num1 + num2 + num3
average = sum_numbers / 3
maximum = max(num1, num2, num3)
minimum = min(num1, num2, num3)

# Ask user for the operation
operation = input("Enter the operation you want to perform (sum, average, maximum, minimum): ").strip().lower()

# Perform the operation
if operation == "sum":
    print(f"The sum is {sum_numbers}")
elif operation == "average":
    print(f"The average is {average:.2f}")  # Rounded for better display
elif operation == "maximum":
    print(f"The maximum is {maximum}")
elif operation == "minimum":
    print(f"The minimum is {minimum}")
else:
    print("Invalid operation! Please enter sum, average, maximum, or minimum.")
