# create class : IdentifyNumber
#         def palindrom ()
#         def armstrong ()
#         def decimal()

class IdentifyNumber :
    def PalinDrome(self,no):
        temp = no
        rvs = 0
        while temp > 0:
            digit = temp % 10
            rvs = (rvs * 10) + digit
            temp = temp // 10
        if no == rvs:
            print("It's a Palindrome")
        else:
            print("It's not a Palindrome")
    
    def ArmStrong(self,no):
        ogno = no
        c = len(str(no))
        sum =0
        while no > 0:
            digit = no%10
            sum+=digit ** c
            no = no//10
        if ogno == sum:
            print("Number is Armstrong")
        else:
            print("Number is not armstrong")
            
    def Decimal(self,no):
        if no%1!=0:
            print("Number is Decimal")
        else:
            print("Number is not Decimal")
n = IdentifyNumber()
no = int(input("Enter Number :"))
n.PalinDrome(no)
n.ArmStrong(no)
no = float(input("Enter Number : "))
n.Decimal(no)


