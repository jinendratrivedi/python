#wap to add and find product all values of dictionary
d={
    1:20,
    2:30,
    3:40
}

total= sum(d.values())

print("sum of all values:",total)

total1=1

for value in d.values():
    total1 *=value

print("product of all values:",total1)