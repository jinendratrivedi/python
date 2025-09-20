s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

# Union of two sets

union_set = s1 | s2
print("Union of s1 and s2:", union_set)

# Intersection of two sets

intersection_set = s1 & s2
print("intersection of s1 and s2:", intersection_set)

# Difference of two sets (s1 - s2)

difference_set = s1 - s2
print("Difference of s1 and s2 (s1 - s2):", difference_set)

# Difference of two sets (s2 - s1)
difference_set_s2 = s2 - s1
print("Difference of s1 and s2 (s2 - s1):", difference_set_s2)

# Symmetric Difference of two sets
symmetric_difference_set = s1 ^ s2
print("Symmetric Difference of s1 and s2:", symmetric_difference_set)

#remove an Element from a Set

s1.remove(3)
print("Set s1 after removing 3:", s1)
s2.remove(4)
print("Set s2 after removing 4:", s2)
