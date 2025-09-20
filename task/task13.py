#-1+2-3+4-5......n print only series

n = int(input("Enter the value of n:"))
for i in range(1,n+1):
    if i%2==0:
        print("+",i,end=" ")
    else:
        print(-i,end=" ")
