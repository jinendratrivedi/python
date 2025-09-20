# perfect in range  using function  : 
"""
6 factors : 1,2,3,6 
sum = 1+2+3 = 6  perfect  

28  factors  : 1,2,4,7,14,28 
sum = 1+2+4+7+14 = 28 perfect  

100 factors : 1,2,4,5,10,20,25,50,100 
sum  =1+2+4+5+10+20+25+50  = 117 not perfect 

"""

def perfact(start,end):
    for i in range(start,end+1):
        sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j
        if sum==i:
            return True
        return False
    
a=int(input("enter the starting number:"))
b=int(input("enter the ending number:"))    

for i in range (a,b+1):
    if perfact(i,b):
        print(i)