#wap to find smallest postive integer from the list

li=[2,3,1,-3,-6,-10,89,90,12,55]
li1=[]

for i in li:
   if i>0:
    li1.append(i)

print(li)    
li1.sort()
print("smallest number is:" , li1[0])