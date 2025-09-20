class val:
    
    def __init__(self,a):
        self.a = a
        #  instance variable
        
        
    def printSum(self):
        print("Sum : ",self.a)
        
    def __add__(self,num):
        sum = self.a + num.a
        return val(sum)
        
        
        
obj1 = val(20)
obj2 = val(40)

sum = obj1 + obj2 

sum.printSum()


