# Display the various Date Time formats.
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week
# Parse the given date string 'Jul 1 2014 2:43PM' into a datetime object using the specified format '%b %d %Y %I:%M%p'
# Get the current date and time using datetime.now() and then retrieve the time component using time() Print the current time
import datetime as dt

# a) Current date and time
print("current date and time:",dt.datetime.now())

# b) Current year
print("current year:",dt.date.today().strftime("%Y"))

# c) Month of year
print("month of  year:",dt.datetime.today().strftime("%b"))

# d) Week number of the year
print("week number of thr year:",dt.datetime.today().strftime("%W"))

# e) Weekday of the week
print("weekdays of week:",dt.datetime.today().strftime("%w"))

# f) Day of year
print("day of year:",dt.datetime.today().strftime("%j"))

# g) Day of the month
print("day of month:",dt.datetime.today().strftime("%d"))

# h) Day of week
print("day of week:",dt.datetime.today().strftime("%A"))

# Parse the given date string 'Jul 1 2014 2:43PM' into a datetime object
# print("date string is:",dt.strptime('Jul 1 2014 2:43PM','%Y-%m-%d %I:%S %p'))
from datetime import datetime , timedelta
date_object = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')
print(date_object)

# Get the current date and time using datetime.now() and then retrieve the time component using time() Print the current time

print("current time:",dt.datetime.now().time())

# Print the current date using date.today()

print("today date:",dt.date.today())

# Calculate the date 5 days after today's date
future_date=dt.date.today() + dt.timedelta(5)
print("future date is:",future_date)

# Write a Python program to print yesterday, today, tomorrow.
print("today date:",dt.date.today())
print("yesterday date:",dt.date.today() - dt.timedelta(1))
print("tomorrow date:",dt.date.today() + dt.timedelta(1))