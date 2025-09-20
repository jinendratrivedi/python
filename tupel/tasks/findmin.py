# wap to find second minimum element of tup

tup=(2,3,4,1,11,2,3,24,24)
fmin=min(tup)
smin=tup[0]

for i in tup:
    if i < smin and i!=fmin:
        smax=i

print("second min is:",smin)        