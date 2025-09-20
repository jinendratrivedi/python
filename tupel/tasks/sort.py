# Write a Python program to sort a tuple by its float element.
# Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

li= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        if li[i][1] < li[j][1]:
         li[i],li[j] = li[j],li[i]


print("sorted element list is:",li)         
