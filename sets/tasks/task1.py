# in a set find +ve minimum element
s={2,3,-4,-5,-3,-2,11,2,9}
for i in s:
    if i>0:
     s=i
     break

print("minimum positive element is:",s)
