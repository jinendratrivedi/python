#  Write a Python program to check if two given sets have no elements in common.

s1={1,2,3,4,5}
s2={6,7,8,9,10}

# method 1:

# if s1.isdisjoint(s2):
#     print("no common elements")
# else:
#     print("common elements are present")

# method 2:
common=s1 & s2

if len(common)==0:
    print(" no common elements")
else:
    print("common elements are present")