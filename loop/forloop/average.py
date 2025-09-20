# find average from 1 to n number

n=int(input("enter the number:"))
sum=0

for i in range(1,n+1):
    sum+=i
    i+=1

average = sum/n
print("average is:",average)       