# find armstrong number 

n=int(input("enter the number:"))
sum=0
value=n

while(n>0):
    reminder = n%10
    sum+=reminder**3
    n//=10

if value==sum:
    print("it is a armstrong number.")

else:
    print("it is not a armstrong number.")      