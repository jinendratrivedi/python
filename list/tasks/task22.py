# Write a program to find the second largest number in a list.

li=[1,2,5,7,9,10]

fmax=max(li)
smax=min(li)

for i in li:
    if  i>smax and i!=fmax:
        smax=i

print("second largest element is:",smax)        
