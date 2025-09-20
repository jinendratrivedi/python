#  3 different shape class  circle square rectangle paret Shape
# area def

class Shape:
    def area(self):
        print("Calculating area in Shape class")

class Circle(Shape):
    def area(self):
        super().area()
        r = float(input("Enter radius of the circle: "))
        print("Area of Circle:", 3.14 * r * r)

class Square(Shape):
    def area(self):
        super().area()
        side = float(input("Enter side of the square: "))
        print("Area of Square:", side * side)

class Rectangle(Shape):
    def area(self):
        super().area()
        length = float(input("Enter length of the rectangle: "))
        width = float(input("Enter width of the rectangle: "))
        print("Area of Rectangle:", length * width)

print("Choose shape to calculate area:")
print("1. Circle")
print("2. Square")
print("3. Rectangle")

choice = int(input("Enter your choice (1-3): "))

match choice:
    case 1:
        c = Circle()
        c.area()
    case 2:
        s = Square()
        s.area()
    case 3:
        r = Rectangle()
        r.area()
    case _:
        print("Invalid choice.")


