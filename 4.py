# Demonstrates one parent (Shape) with two children (Circle, Rectangle).
class shape():
    def parentofcr(self):
        print("shape include many shapes like circle , rectangle , square , circle")

class circle(shape):
    def AreaC(self,radius):
        # self.r = radius
        self.AreaC = 3.14 *(radius * radius)
        print("area of circle is:",self.AreaC)

class rectangle(shape):
    def areaR(self,length,bradth):
        self.l = length
        self.b = bradth
        self.areaR = (self.l * self.b)
        print("ara of rectangle is:",self.areaR)

c = circle()
radius = int(input("entet the radius of circle:"))
c.AreaC(radius)
c.parentofcr()

r = rectangle()
length = int(input("enter the length:"))
breadth = int(input("enter the breadth:"))
r.areaR(length,breadth)
r.parentofcr()