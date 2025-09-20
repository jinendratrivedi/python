#wap to continously input values from user and store it in a list but stop storing in list
# if user input 100

li=[]

while True:
    a=int(input("enter the number:"))
    if a==100:
        break
    li.append(a)

print(li)    

