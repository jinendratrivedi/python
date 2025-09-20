# Reverse , Palindrome , Armstrong
class R:
    rvs = 0
    def Reverse(self,no):   
        while(no!=0):
            self.temp = no %10
            self.rvs = self.rvs*10 + self.temp
            no = no//10
        
        print("Reverse :",self.rvs)

class P(R):
    def Palindrome(self,no):
        self.rvs = 0
        self.t = no
        while(no!=0):
            self.temp = no %10
            self.rvs = (self.rvs*10) + self.temp
            no = no//10
        print(self.t,self.rvs)
        if(self.t == self.rvs):
            print("Palindrome")
        else:
            print("Not Palindrome")
    
class A(P):

    def armstrong(self,num):
        for self.i in range(1,num+1):
            self.temp=self.i
            self.sum=0
            self.digit=len(str(self.i))
        while self.temp>0:
            self.r=self.temp%10
            self.sum+=pow(self.r,self.digit)
            self.temp//=10
        if (self.sum==num):
            print("Armstrong")
        else:
            print("Not Armstrong")

obj = A()
no = int(input("Enter Number :"))
obj.Reverse(no)
obj.Palindrome(no)
obj.armstrong(no)