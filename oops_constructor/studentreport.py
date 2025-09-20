class Student:

    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln

    def getData(self):
        self.cn = input("Enter Course Name: ")
        self.cno = int(input("Enter Contact Number: "))
        self.m1 = int(input("Enter Marks 1: "))
        self.m2 = int(input("Enter Marks 2: "))
        self.m3 = int(input("Enter Marks 3: "))
        self.m4 = int(input("Enter Marks 4: "))
        self.m5 = int(input("Enter Marks 5: "))
        self.total = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
        self.avg = self.total / 5

    def DispData(self):
        print("\n--------------Student Details--------------")
        print("First Name :", self.fn)
        print("Last Name :", self.ln)
        print("Course Name :", self.cn)
        print("Contact NO :", self.cno)
        print("Marks 1 :", self.m1)
        print("Marks 2 :", self.m2)
        print("Marks 3 :", self.m3)
        print("Marks 4 :", self.m4)
        print("Marks 5 :", self.m5)
        print("Total Marks :", self.total)
        print("Average :", self.avg)
        if self.avg > 90:
            print("Grade : A")
        elif 80 <= self.avg <= 90:
            print("Grade : B")
        elif 70 <= self.avg < 80:
            print("Grade : C")
        elif 60 <= self.avg < 70:
            print("Grade : D")
        elif 50 <= self.avg < 60:
            print("Grade : E")
        else:
            print("Grade : Fail")


# Taking name input from user
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

# Creating object
obj = Student(first_name, last_name)
obj.getData()
obj.DispData()
