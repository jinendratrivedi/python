# Many companies pay time-and-a-half for any hours worked above 40 hours in a given week. Write a
# program to input the number of hours worked and hourly rate and calculate the total wages for the week. using functions.

def calculate_wages(hours,rate):
    if hours > 40:
        overtime = hours - 40
        total = (40 * rate) + (overtime * rate * 1.5)
    else:
        total = hours * rate  
    return total

hours = int(input("Enter the number of hours worked: "))
rate = float(input("Enter the hourly rate: "))
wages = calculate_wages(hours, rate)
print(f"The total wages for the week is: rs{wages:.2f}")