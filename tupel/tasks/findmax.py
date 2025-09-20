# wap to find second max element of tup

tup=(2,3,4,1,11,2,3,24,24)
fmax=max(tup)
smax=tup[0]

for i in tup:
    if i > smax and i!=fmax:
        smax=i

print("second max is:",smax)        