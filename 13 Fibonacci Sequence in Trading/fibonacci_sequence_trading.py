#1️⃣3️⃣ Fibonacci Sequence in Trading: Generate the first 10 Fibonacci 
# numbers (used in technical analysis).
def fibonacci_generator(n):
    fibonacci_Sequence = [0, 1]
    for i in range(n-2):
        next_num = fibonacci_Sequence[-1] + fibonacci_Sequence[-2]
        fibonacci_Sequence.append(next_num)
    return fibonacci_Sequence

numbers = fibonacci_generator(10)
print(f'the 10 fibonacci numbers are: {numbers}')