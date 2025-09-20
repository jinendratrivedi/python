class student:
    a=50
    b=40
    
    def addition(self):
        c=self.a + self.b
        print("addition:",c)
    
    def subtraction(self):
        c=self.a - self.b
        print("subtraction:",c)

    def mulplication(self):
        c=self.a * self.b
        print("multiplication:",c)

    def division(self):
        c=self.a / self.b
        print("division:",c)     

stu = student()
stu.addition()
stu.subtraction()      
stu.mulplication()
stu.division()  