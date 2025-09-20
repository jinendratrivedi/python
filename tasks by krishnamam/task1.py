
def add(a,b):
    print(f"addition of {a} and {b}:",a+b)
def sub(a,b):
    return a-b
def mul(a,b):
    print(f"multiplication of {a} and {b}:",a*b)
def div(a,b):
    return a/b

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
def default():
    print("Invalid choice")

choice = int(input("Enter your choice:"))
match choice:
    case 1:
        add(a,b)
    case 2:
        print(sub(a,b))
    case 3:
        mul(a,b)
    case 4:
        print(div(a,b))
    case _:
        default()



