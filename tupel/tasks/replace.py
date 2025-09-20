# Write a Python program to replace the last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

li=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
li1=[]

for i in li:
    li1.append(i[:2]+(100,))

print("replace:",li1)   