# find perfact number

n=int(input("enter the number:"))
i=1
sum=0

while i<n:
    if n%i==0:
        sum+=i
    i+=1

if sum==n:
    print("this is perfact number.")
else:
    print("this is not a perfact number.")          
