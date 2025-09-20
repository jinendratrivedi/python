# Reverse a List Without Using Built-in Functions

li= [1,2,3,4,5,6]
li1=[]

for i in range(len(li)-1,-1,-1):
    li1.append(li[i])

print("reversed list is:",li1)   
