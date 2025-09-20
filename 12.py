# Design a system where a person can be both a Student and a Faculty member. A person may have both student and faculty-specific actions.

class Person:
    def person_details(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def set_student_details(self, student_id):
        self.student_id = student_id

    def attend_class(self):
        print(f"{self.name} is attending class as a student.")

    def show_student_info(self):
        print(f"Student ID: {self.student_id}")

class Faculty(Person):
    def set_faculty_details(self, faculty_id):
        self.faculty_id = faculty_id

    def teach_class(self):
        print(f"{self.name} is teaching a class.")

    def show_faculty_info(self):
        print(f"Faculty ID: {self.faculty_id}")

class StudentFaculty(Student, Faculty):
    def perform_roles(self):
        self.show_details()
        self.show_student_info()
        self.show_faculty_info()
        self.attend_class()
        self.teach_class()


sf = StudentFaculty()
sf.person_details("jinendra trivedi", 21)
sf.set_student_details("S123")
sf.set_faculty_details("F456")
sf.perform_roles()
