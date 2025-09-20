class Person:
    def set_person(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Professor(Person):
    def set_professor(self, title):
        self.title = title

    def show_professor(self):
        print("Title:", self.title)

class ComputerScience:
    def teach_cs(self):
        print(self.name, "is teaching Computer Science.")

class Mathematics:
    def teach_math(self):
        print(self.name, "is teaching Mathematics.")

# Role class
class Researcher:
    def do_research(self):
        print(self.name, "is doing research.")

# Role class
class Administrator:
    def do_admin(self):
        print(self.name, "is handling administration.")

# Final class combining all roles
class MultiRoleProfessor(Professor, ComputerScience, Mathematics, Researcher, Administrator):
    def show_all(self):
        self.show_person()
        self.show_professor()
        self.teach_cs()
        self.teach_math()
        self.do_research()
        self.do_admin()

# 🔰 Example usage
prof = MultiRoleProfessor()
prof.set_person("Dr. Jinendra", 45)
prof.set_professor("Senior Professor")
prof.show_all()
