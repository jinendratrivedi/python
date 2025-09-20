# Write a Python program to find repeated items in a tuple

tup=(1,2,3,1,1,6,8)
li=[]
for i in range(0,len(tup)):
    for j in range(i+1,len(tup)):
        if tup[i]==tup[j]:
            li.append(tup[i])

print("repeated element is:",li)            
