# An Account class with accountType is extended by SavingsAccount and CurrentAccount, each providing their unique functionality. This design showcases hierarchical inheritance for different banking accounts sharing common attributes while maintaining specialized methods.

# Base class
class Person:
    def set_person(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)

class ComputerScience:
    def teach_cs(self):
        print(self.name, "is teaching Computer Science.")

class Mathematics:
    def teach_math(self):
        print(self.name, "is teaching Mathematics.")

class Researcher:
    def do_research(self):
        print(self.name, "is conducting research.")

class Administrator:
    def do_admin(self):
        print(self.name, "is handling administration.")

class Professor(Person, ComputerScience, Mathematics, Researcher, Administrator):
    def set_professor(self, title):
        self.title = title

    def show_professor(self):
        print("Title:", self.title)

    def show_all(self):
        self.show_person()
        self.show_professor()
        self.teach_cs()
        self.teach_math()
        self.do_research()
        self.do_admin()

prof = Professor()
prof.set_person("Dr. Jinendra", 45)
prof.set_professor("Senior Professor")
prof.show_all()
