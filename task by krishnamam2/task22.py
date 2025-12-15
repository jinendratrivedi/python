#Remove multiple elements from a list in Python
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
list2 = [20, 40, 60]

for item in list2:
    for i in list1:
        if item == i:
            list1.remove(i)

print(list1)