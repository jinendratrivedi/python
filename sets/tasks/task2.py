# find second largest elemnt of set

s={2,3,-4,-5,-3,-2,11,2,9}

fmax=max(s)
smax=min(s)

for i in s:
    if i > smax and i!=fmax:
        smax=i

print("second largest element is:",smax)