# find armstrong number 

num = int(input("enter the number:"))
sum=0


for i in str(num):
    sum+=int(i)**3
    
if num==sum:
    print("it is a armstrong number.")
else:
    print("it is not a armstrong number.")        
