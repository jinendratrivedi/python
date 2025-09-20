class Person:
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    def input_details(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Teacher(Person):
    def __init__(self, name='', age=0, subject='', salary=0.0):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def input_details(self):
        super().input_details()
        self.subject = input("Enter subject: ")
        self.salary = float(input("Enter salary: "))

    def display_details(self):
        super().display_details()
        print("Subject:", self.subject)
        print("Salary:", self.salary)

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

class Administrator(Person):
    def __init__(self, name='', age=0, department='', role=''):
        super().__init__(name, age)
        self.department = department
        self.role = role

    def input_details(self):
        super().input_details()
        self.department = input("Enter department: ")
        self.role = input("Enter role: ")

    def display_details(self):
        super().display_details()
        print("Department:", self.department)
        print("Role:", self.role)

    def manage(self):
        print(f"{self.name} is managing the {self.department} department as a {self.role}.")

print("Select Option:")
print("1. Teacher Details")
print("2. Administrator Details")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        t = Teacher("jinendra",20)
        t.input_details()
        t.display_details()
        t.teach()
    case 2:
        a = Administrator()
        a.input_details()
        a.display_details()
        a.manage()
    case _:
        print("Invalid choice. Please try again.")
