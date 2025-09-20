# Parent : getdata : Name : display 
# child : getData : age cno : display

class Parent:
    def getdata(self,name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Child(Parent):
    def getData(self,age, cno):  
        self.age = age
        self.cno = cno
    
    def display1(self):
        print("Age:", self.age)
        print("Contact Number:", self.cno)

obj = Child()
name = input("Enter your name: ")
age = int(input("Enter your age: "))
cno = input("Enter your contact number: ")
obj.getdata(name)
obj.getData(age, cno)
obj.display()
obj.display1()