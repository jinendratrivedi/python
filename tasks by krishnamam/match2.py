# Write a program to determine whether a given triangle is equilateral, isosceles, or scalene based on the lengths of its sides


a=int(input("Enter the length of side a: "))
b=int(input("Enter the length of side b: "))
c=int(input("Enter the length of side c: "))


match (a,b,c):
    case (a,b,c) if a == b == c:
        print("The triangle is equilateral.")
    case (a,b,c) if a == b or b == c:
        print("The triangle is isosceles.")
    case (a,b,c) if a != b and b != c and a != c:
        print("The triangle is scalene.")

    case _:
        print("Invalid triangle sides.")