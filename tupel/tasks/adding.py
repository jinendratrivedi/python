#in a list of tuple add both elements of tuple
# data = [(1, 2), (3, 5), (4, 6), (1, 1), (2, 3)]
# output=[3,8,10,2,5]


data = [(1, 2), (3, 5), (4, 6), (1, 1), (2, 3)]
out = []

for i in data:
    a=sum(i)
    # a= i[0]+i[1]
    out.append(a)

print("result is",out)

