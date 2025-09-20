import random

# Use random.choice to pick starting values from a list
a = random.choice([0, 1, 2, 3, 4, 5])
b = random.choice([0, 1, 2, 3, 4, 5])

# Take user input for the number of terms
n = int(input("Enter the number of terms in the Fibonacci series: "))

print("Fibonacci-like series:")
print(a, b, end=' ')

# Generate the Fibonacci-like series
for _ in range(n - 2):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
