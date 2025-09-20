class EmailException(Exception):
    pass

try:
    email = input("Enter your email: ")

    if "@" not in email or "." not in email:
        raise EmailException("Invalid Email! Must contain '@' and '.' ")
    else:
        print(" Email is valid")

except EmailException as e:
    print("Error:", e)

print("Thank You...!!!")
