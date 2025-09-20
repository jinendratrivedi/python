#Find Common Elements in Two Lists

li1=[1,2,3,4,5,6,7,8,9]
li2=[2,4,6,8,10,12,14,16,18]

li=[]

for i in li1:
    for j in li2:
        if i==j:
            li.append(i)

print(li)            
