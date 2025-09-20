# Find the common elements between two lists using sets.

l1=[1,2,3,4,5]
l2=[4,5,6,7,8]

s1=set(l1)
s2=set(l2)

common=s1 & s2

print("common elements are:",list(common))
