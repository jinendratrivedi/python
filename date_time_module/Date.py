# In Python, you can work with dates using the datetime module, which provides classes for manipulating dates and times. Here's a quick overview of some common functionalities:

# Importing the Module

# from datetime import datetime, date, time, timedelta

### Getting the Current Date and Time
from datetime import datetime, timedelta

x = datetime.now()  # Current date and time
# print("Now:", x)

# print("year : ",x.year)
# print("strftime : ",x.strftime("%A"))
# print("strftime : ",x.strftime("%a"))

### Formatting Dates

# You can format dates as strings using the `strftime` method:
# x = datetime.datetime(2020, 5, 17)
# 
# print(x)

formatted_date = x.strftime("%Y-%m-%d %H:%M:%S")
# print("Formatted Date:", formatted_date)

# ### Creating a Date Object

my_date = datetime(2023, 9, 27)
# print("My Date:", my_date)


formatted_date = my_date.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)
### Calculating Date Differences

# You can calculate the difference between two dates using `timedelta`:

date1 = datetime(2023, 1, 10)
date2 = datetime(2024, 1, 10)
delta = date2 - date1
# print(delta)
# print("Days between:", delta.days)

### Adding or Subtracting Days

# You can use `timedelta` to add or subtract days:

# new_date = my_date + timedelta(days=10)
# print("New Date:", new_date)

### Example: Full Usage

# Here's a simple example that combines some of the above:

# from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print("Current Date and Time:", now)

# Format it
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", formatted)

# print(now.day)

# Add 7 days
future_date = my_date + timedelta(days=7)
print("Future Date:", future_date.strftime("%Y-%m-%d"))

# %a	Weekday, short version	Wed	
# %A	Weekday, full version	Wednesday	
# %w	Weekday as a number 0-6, 0 is Sunday	3	
# %d	Day of month 01-31	31	
# %b	Month name, short version	Dec	
# %B	Month name, full version	December	
# %m	Month as a number 01-12	12	
# %y	Year, short version, without century	18	
# %Y	Year, full version	2018	
# %H	Hour 00-23	17	
# %I	Hour 00-12	05	
# %p	AM/PM	PM	
# %M	Minute 00-59	41	
# %S	Second 00-59	08	
# %f	Microsecond 000000-999999	548513	
# %z	UTC offset	+0100	
# %Z	Timezone	CST	
# %j	Day number of year 001-366	365	
# %U	Week number of year, Sunday as the first day of week, 00-53	52	
# %W	Week number of year, Monday as the first day of week, 00-53	52	
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
# %C	Century	20	
# %x	Local version of date	12/31/18	
# %X	Local version of time	17:41:00	
# %%	A % character	%	
# %G	ISO 8601 year	2018	
# %u	ISO 8601 weekday (1-7)	1	
# %V	ISO 8601 weeknumber (01-53)	01