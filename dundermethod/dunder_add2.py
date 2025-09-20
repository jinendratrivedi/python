class val:

    def __init__(self,a,b):
        self.a = a
        self.b = b
        #instance variable

    def printsum(self):
        print("sum:",self.a)
        print("sum:",self.b)

    def __add__(self,num):
        sum = self.a +num.a
        sum1 = self.b + num.b

        return val(sum,sum1)



obj1 = val(20, 30)
obj2 = val(40, 50)

result = obj1 + obj2
result.printsum()