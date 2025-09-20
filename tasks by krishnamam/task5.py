#. Write a program to convert temperature from
# Celsius to Fahrenheit. Equation to convert Celsius
# to Fahrenheit:
# 𝐹 = (9/5) * 𝐶 + 32

number = int(input("Enter the number of Celsius: "))
print("Celsius:", number)

def celsius_to_fahrenheit(celsius):
    fahernhit = (9 / 5) * celsius + 32
    return fahernhit

print("celsius to fahrenheit: ",  celsius_to_fahrenheit(number), "F")
