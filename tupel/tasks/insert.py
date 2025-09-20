# wap to insert an element at 4th index of tuple
tup=(2,3,4,5,"abc","def",11,12)

a=list(tup)

a.insert(4,"new_element")
tup = tuple(a)
print(tup)