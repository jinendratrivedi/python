class student:

    def __init__(self):
        self.a=10
        self.b=20

    #  def __init__(self,a,b):
    #dunder
    #initialisation obj
    #     self.a=a
    #     self.b=b   

    def addition(self):
        print("print def")
        c=self.a + self.b
        print("Addition:",c)

obj = student()
obj.addition()        