class Student:
    a = 99
    b = 44
    # class / instance variable
    # data member
    def addition(self):
        a = 90
        b = 70
        
        print("addition")
        # c = self.a+self.b 
        c = a+b
        print(c)
    
    def subtraction(self):
        c = self.a - self.b
        print("Subtraction : ",c)
    
        
# create an object
stu = Student()

stu.addition()
stu.subtraction()

 