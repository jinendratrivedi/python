# Write a program to remove duplicate elements from a list while maintaining the order.

li=[1,2,3,4,5,2,2,2,2]
li1=[]

for i in li:
    if i not in li1:
        li1.append(i)

print("list after removing duplicates is:",li1)      