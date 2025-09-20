#wap to check that no is perfect no

n=int(input("enter the number:"))
sum=0

for i in range(1,n):

    if n%i==0:
        sum+=i

if sum==n:
    print("it is a perfact number.")

else:
    print(" it is not a perfact number.")          
