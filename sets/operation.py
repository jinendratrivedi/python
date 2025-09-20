#operation of sets

s1={1,2,3,4,5}
s2={2,3,4,5,6,7,8}

#union-> it will return all the elements of both the sets
print(s1.union(s2))
print(s1|s2)

#intersection-> it will return common elements of both the sets

print(s1.intersection(s2))
print(s1&s2)

#difference-> it will returns 
print(s1.difference(s2))
print(s2-s1)

#symmetric difference-> it will remove common values of both sets

print(s1.symmetric_difference(s2))
print(s1^s2)