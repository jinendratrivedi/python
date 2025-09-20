# 1. Design a function that greets a user. If no name is given, greet as "User".
def greet_user(uname=""):
    print(f"ram {uname}")
greet_user()  

# 2. Create a function that adds two numbers. If the second number isn’t passed, assume it's 10.

def add(num1,num2=10):
    return num1 + num2
print("addition is:",add(5)) 

# 3. Show user info with name and age. If age is missing, use 18 as default.
def show_user_info(name, age=18):
    print(f"Name: {name}, Age: {age}")
show_user_info("ram", 25)
show_user_info("shyam")

# 4. Write a function that raises a number to a power. If no power is provided, square it.
def power(num, exp=2): 
    return num ** exp
print("Power is:", power(3)) 

# 5. Print a list of fruits. If no list is provided, print a default list.
def print_fruits(fruits=None):
    if fruits is None:
        fruits = ["Apple", "Banana", "Cherry"]
    print("Fruits:", fruits)

# 6. Calculate the final price after applying discount. Use 10% discount if none is specified.
def calculate_final_price(price, discount=0.10):
    final_price = price * (1 - discount)
    return final_price
print("Final price is:", calculate_final_price(100))
# 7. Display a message with city and country. If country isn't provided, assume it’s India.
def location_message(city, country="India"):
    print(f"Location: {city}, Country: {country}")
location_message("Delhi")

# 8. Send an email with subject and optional body. If no body is given, use a default message.
def send_email(subject, body="No content provided."):
    print(f"Email sent with subject: '{subject}' and body: '{body}'")
send_email("Meeting Reminder")

# 9. Record a student’s grade. If not assigned, label it as "Not Assigned".
def record_student_grade(name, grade="Not Assigned"):
    print(f"Student: {name}, Grade: {grade}")
record_student_grade("John")

# 10. Print a star pattern. If the count is not passed, print 5 stars by default.
def print_star_pattern(count=5):
    for i in range(count):
        print("*", end="")
    # print()
print_star_pattern()
