#find average from 1 to n number

n=int(input("enter the number:"))
sum=0
i=1

while i<=n:
    sum +=i
    i+=1

average = sum/n
print("average is:",average)   