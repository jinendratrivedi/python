# Python f-strings provide a quick way to interpolate and format strings. 
# .format() method and the modulo operator (%).

# Before Python 3.6, you had two main tools for interpolating values, variables, and expressions inside string literals:

# The string interpolation operator (%), or modulo operator
# The str.format() method: LJ UNIVERSITY 



name = "Shyam"
# print("Hello, %s!" % name)
# 'Hello, Jane!'

name = "Shyam"
age = 25

# print("Hello, %s! You're %s years old." % (name, age))
# 'Hello, Shyam! You're 25 years old.'


# can use dictinary
# print("Hello, %(name)s! You're %(age)s years old." % {"name": "Shyam", "age": 25})
# "Hello, Shyam! You're 25 years old."


# print("Balance: $%.2f" % 5425.9292)
# print("bal : $%.3f" % 23.4445656)
# # 'Balance: $5425.93'

name = "riya"
num = 35
# print("Name: %s\nAge: %5s" % (name, num))
# # Name: John
# # Age:    35

# # f string format
# name = "Jane"
# age = 25

print(f"Hello, {name}! You're {age} years old.")
# 'Hello, Jane! You're 25 years old.'

# f"{2 * 21}"
# '42'
# name = "Jane"
# age = 25

# print(f"Hello, {name.upper()}! You're {age} years old.")
# # "Hello, JANE! You're 25 years old."

# print(f"{[2**n for n in range(3, 9)]}")
# # '[8, 16, 32, 64, 128, 256]'

# format(5425.9292, ".2f")
# # '5425.93'

balance = 5425.9292

# print(f"Balance: ${balance:.2f}")
# # 'Balance: $5425.93'

# # heading = "Centered string"
heading =  "Royal"

# print(f"{heading:*^11}")
# # '=======Centered string========'

integer = -1234567
# print(f"Comma as thousand separators: {integer:,}")
# # 'Comma as thousand separators: -1,234,567'

sep = "_"
# print(f"User's thousand separators: {integer:{sep}}")
# # 'User's thousand separators: -1_234_567'

# floating_point = 1234567.9876
# print(f"Comma as thousand separators and two decimals: {floating_point:,.2f}")
# # 'Comma as thousand separators and two decimals: 1,234,567.99'

date = (9, 6, 2023)
# print(f"Date: {date[0]:02}-{date[1]:02}-{date[2]}")
# # 'Date: 09-06-2023'

from datetime import datetime
date = datetime(2023, 9, 26)
print(f"Date: {date:%m/%d/%Y}")
# 'Date: 09/26/2023'  