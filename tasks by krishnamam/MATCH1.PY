#  add sub mul div modules:evn-odd 


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

op = int(input("Enter operation (1: Add, 2: Subtract, 3: Multiply, 4: Divide, 5: Modulus ): "))
match op:

    case 1:
        print("Addition:", a + b)
        if(a + b) % 2 == 0:
            print("Even")
        else:
            print("Odd")

    case 2:
        print("Subtraction:", a - b)
        if(a - b) % 2 == 0:
            print("Even")
        else:
            print("Odd")

    case 3:
        print("Multiplication:", a * b)
        if(a * b) % 2 == 0:
            print("Even")
        else:
            print("Odd")

    case 4:
        print("Division:", a / b)
        if(a / b) % 2 == 0:
            print("Even")
        else:
            print("Odd")
            
    case 5:
        print("Modulus:", a % b)
        if(a % b) % 2 == 0:
            print("Even")
        else:
            print("Odd")
  
    case 6:
        if(a + b) % 2 == 0:
            print("Even")
        else:
            print("Odd")
    case _:
        print("Invalid operation")

