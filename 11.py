# Create a class system that represents different kinds of employees in an organization. An employee could be both a Manager and a Developer, and you need to inherit both the managerial and technical skills.

class Employee:
    def set_employee_details(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def show_employee_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")


class Manager(Employee):
    def set_manager_details(self, department):
        self.department = department

    def conduct_meeting(self):
        print(f"{self.name} is conducting a meeting in the {self.department} department.")

    def show_manager_info(self):
        print(f"Manager Department: {self.department}")


class Developer(Employee):
    def set_developer_details(self, programming_language):
        self.language = programming_language

    def write_code(self):
        print(f"{self.name} is writing code in {self.language}.")

    def show_developer_info(self):
        print(f"Programming Language: {self.language}")


class ManagerDeveloper(Manager, Developer):
    def perform_roles(self):
        self.show_employee_details()
        self.show_manager_info()
        self.show_developer_info()
        self.conduct_meeting()
        self.write_code()


emp = ManagerDeveloper()
emp.set_employee_details("Jinendra Trivedi", "EMP101")
emp.set_manager_details("IT")
emp.set_developer_details("Python")
emp.perform_roles()
