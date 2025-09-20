#print fibonacci series

a=0
b=1

n=int(input("enter the number:"))
i=1

while i<=n:
    print(a,end=" ")
    a,b = b,a+b
    i+=1