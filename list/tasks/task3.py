#wap to input 10 values from user and store only non repeating values in list

li=[]

for i  in range(1,11):
 a=input("enter the elements for list:")
 if a not in li:
    li.append(a)

print(li)


