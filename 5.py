# Employee as parent, Manager and Developer as children take value from user.
class employee():
    def emp(self):
        print("manager and devloper are employees")

class manager(employee):
    def getdata(self):
        self.id = int(input("enter the manager id:"))
        self.name = input("enter the manager name:")
        self.conactno = int(input("enter the manager contact number:"))
        self.emil = input("enter the manager email:")
        self.designation = input("entet the manager designation:")

    def displaydata(self):
        print("id:",self.id)
        print("name:",self.name)
        print("contact no:",self.conactno)
        print("Email:",self.emil)
        print("designation:",self.designation)

class developer(employee):
    def getdata(self):
        self.id = int(input("enter the developer id:"))
        self.name = input("enter the developer name:")
        self.conactno = int(input("enter the developer contact number:"))
        self.emil = input("enter the developemail:")
        self.designation = input("entet the designation:")

    def displaydata(self):
        print("id:",self.id)
        print("name:",self.name)
        print("contact no:",self.conactno)
        print("Email:",self.emil)
        print("designation:",self.designation)
        

m = manager()
m.getdata()
m.displaydata()

d = developer()
d.getdata()
d.displaydata()
d.emp()
m.emp()
