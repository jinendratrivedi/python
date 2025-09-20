class MarksException(Exception):
    pass

try:
    s1 = int(input("Enter the first subject marks: "))
    s2 = int(input("Enter the second subject marks: "))
    s3 = int(input("Enter the third subject marks: "))
    s4 = int(input("Enter the fourth subject marks: "))
    s5 = int(input("Enter the fifth subject marks: "))

    total = s1 + s2 + s3 + s4 + s5
    print("Total:", total)

    if total > 500:
        raise MarksException("Total cannot be greater than 500")
    elif total < 0:
        raise MarksException(" Total cannot be negative")
    else:
        print(" Total is valid")

except MarksException as e:
    print("Error:", e)

print("Thank You...!!!")
