# Write a Python program to get a list, sorted in increasing order by the last element
# in each element from a given list .
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


li= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        if li[i][1] > li[j][1]:
            li[i],li[j] = li[j],li[i]

print("sorted element list is:",li)