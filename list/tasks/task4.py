#wap to input 10 integer values from user and store only even values

li=[]

for i in range(1,11):
    a=int(input("enter the number:"))
    if a%2==0:
     li.append(a)

print(li)      


