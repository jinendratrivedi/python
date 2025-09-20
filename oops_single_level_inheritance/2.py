class Add:
    def Addition(self,a,b):
        print(a+b)

class Sub(Add):
    def Subtraction(self,a,b):
        print(a-b)

class Mul(Sub):
    def Multiplication(self,a,b):
        print(a*b)

class Div(Mul):
    def Division(self,a,b):
        print(a/b)

obj = Div()
a=int(input("Enter Number A:"))
b=int(input("Enter Number B:"))
obj.Addition(a,b)
obj.Subtraction(a,b)
obj.Multiplication(a,b)
obj.Division(a,b)
