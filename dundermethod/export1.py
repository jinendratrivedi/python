def add(a, b):
    return a + b

def sub(a, b):
    return a - b  

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


if __name__ == '__main__':
    a = int(input("Enter the value of x: "))
    b = int(input("Enter the value of y: "))

    print("Addition:", add(a, b))
    print("Subtraction:", sub(a, b))
    print("Multiplication:", mul(a, b))
    print("Division:", div(a, b))
