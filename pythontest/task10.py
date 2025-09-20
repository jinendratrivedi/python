# Remove empty lists from a list of lists.
# list_of_lists = [[], [1, 2], [], [3, 4, 5], []]

list_of_lists = [[], [1, 2], [], [3, 4, 5], []]
li=[]
for i in list_of_lists:
    if len(i)==0:
        pass
    else:
        li.append(i)    

print("list after removing empty lists is:",li)         