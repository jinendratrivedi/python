# menu 
# addition of two int 
# string concate 
# addition of 4 int


class menu:
    def addition(self,a,b):
        print(f"Addition of {a} and {b} is {a + b}")

    def string_concate(self,a,b):
        print(f"Concatenation of '{a}' and '{b}' is '{a + b}'")

    def addition2(self,a,b,c,d):
        print(f"Addition of {a}, {b}, {c}, and {d} is {a + b + c + d}")

obj = menu()

while True:
    print("\nMenu:")
    print("1. Addition of two integers")
    print("2. String concatenation")
    print("3. Addition of four integers")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        obj.addition(a,b)
    elif choice == '2':
        a = input("Enter first string: ")
        b = input("Enter second string: ")
        obj.string_concate(a,b)
    elif choice == '3':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = int(input("Enter third number: "))
        d = int(input("Enter fourth number: "))
        obj.addition2(a,b,c,d)
    else:
        print("Invalid choice, please try again.")
        continue
