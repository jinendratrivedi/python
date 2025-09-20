# Sort a list of tuples based on the second element.
# list_of_tuples = [(1, 3), (4, 2), (5, 1)]

list_of_tuples = [(1, 3), (4, 2), (5, 1)]

for i in range(0,len(list_of_tuples)):
    for j in range(i+1,len(list_of_tuples)):
        if list_of_tuples[i][1] > list_of_tuples[j][1]:
         list_of_tuples[i],list_of_tuples[j] = list_of_tuples[j],list_of_tuples[i]

print("sorted element in list is:",list_of_tuples)