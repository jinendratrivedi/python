#in the given list, sort elements of list on the basis of middle element
# li=[(2,5,1),(4,0,2),(5,6,1),(2,3,4)]
#res=[((4,0,2),(2,3,4),(2,5,1),(5,6,1))]

li=[(2,5,1),(4,0,2),(5,6,1),(2,3,4)]

for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        if li[i][1] > li[j][1]:
                li[i],li[j] = li[j], li[i]
                
print("sorted list is :",li)                