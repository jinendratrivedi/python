#wap to print fibbonacci series upto n

a=0
b=1

n=int(input("enter the elements:"))

for i in range(1,n+1):
    print(a,end=" ")
    a,b=b,a+b


