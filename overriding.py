class Add():
    def operation(self,a,b):
        self.addition = a + b
        print("Addition : ",self.addition)
        
class Sub(Add):
    def operation(self,a,b):
        super().operation(10,5)
        self.subtraction = a - b
        print("Subtraction : ",self.subtraction)
        
class Mul(Sub):
    def operation(self,a,b):
        super().operation(10,5)
        self.multi = a * b
        print("Multiplication : ",self.multi)
        
class Div(Mul):
    def operation(self,a,b):
        super().operation(10,5)
        self.division = a / b
        print("Division : ",self.division)
        
d = Div()
d.operation(10,5)