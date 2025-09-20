# Count the occurrences of number 4 in the list.

li=[1,2,3,4,5,4,6,7,8,9,4]
count=0

for i in li:
    if i==4:
        count+=1

print("The number 4 occurs", count, "times in the list.")