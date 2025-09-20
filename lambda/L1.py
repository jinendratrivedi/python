#even or odd using lambda function
evenodd = lambda x: True if x % 2 == 0 else False
print(f"Is  even? {evenodd(3)}")

#sub , mul ,div

sub = lambda a, b: a - b
print(f"Subtraction: {sub(10, 5)}")
mul = lambda a, b: a * b
print(f"Multiplication: {mul(10, 5)}")
div = lambda a,b:a/b 
print(f"Division: {div(10, 5)}")

# power using lambda
power = lambda a, b: a ** b
print(f"Power: {power(2, 3)}")


