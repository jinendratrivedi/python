#wap to Check Common Member Between Two Lists

li1=["a","b","abc",2,1,4,5,6]
li2=["a",5,6,"abc","lmno",100,200]

li=[]

for i in li1:
    for j in li2:
        if i==j:
            li.append(i)

print(li)            