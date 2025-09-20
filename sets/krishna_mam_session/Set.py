a = {1,2,3,4,5,6,7}
b = {3,4,5,7,8,9,10}


# intersection : {3,4}
# union = {1,2,3,4,5,7}

print(a)
a.add(77)
print(a)

a.remove(3)
print(a)

# union

uni = a | b
print(uni)

# intersection

intr = a & b
print(intr)

# difference

diff = a - b
print(diff)

diff = b - a
print(diff)