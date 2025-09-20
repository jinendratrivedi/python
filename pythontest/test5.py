# Write a program to find the second largest element in a list.

li=[1,2,3,4,5,2,7,10]
fmax=max(li)
smax=li[0]

for i in li:
    if i > smax and i!=fmax:
        smax=i

print("second largest element is:",smax)        
