class even:
    def getdata(self):
        self.a=int(input("enter the number:"))

    def even(self):
        if(self.a%2==0):
            print("even number")
        else:
            print("odd number")    

e = even()
e.getdata()
e.even()                   