# Write a program to get change values in Quarter,Dime, Nickels and Pennies, and calculate the value of change in Dollars. Consider Quarter = 0.25 $, Dime = 0.10 $, Nickels = 0.05 $ and Penny = 0.01 $ using functions.

def get_change_values(a, b, c, d):

    total = (a * 0.25) + (b * 0.10) + (c * 0.05) + (d * 0.01)
    return total

print("Enter the number of Quarters, Dimes, Nickels and Pennies:")
a=int(input("Enter the number of Quarters: "))
b=int(input("Enter the number of Dimes: "))
c=int(input("Enter the number of Nickels: "))
d=int(input("Enter the number of Pennies: "))


total = get_change_values(a, b, c, d)
print("Total value of change in Cents: ", total * 100) 
print("Total value of change in Quarters: ", total * 4) 
print("Total value of change in Dimes: ", total * 10)
print("Total value of change in Nickels: ", total * 20)
print("Total value of change in Pennies: ", total * 100)
print("Total value of change in Dollars: $", total)



