# Count duplicate Elements in a Tuple

tup=(1,2,3,4,5,2,2,2,2)
count=0

for i in tup:
    if i==2:
        count+=1

print("total count of 2 is:",count)      

# find out all even numbers from a tuple and return a new tuple with the odd numbers.

# Write a program to remove duplicate elements from a list while maintaining the order.

li=[1,2,3,4,5,2,2,2,2]
li1=[]

for i in li:
    if i not in li1:
        li1.append(i)

print("list after removing duplicates is:",li1)      

# Reverse a List Without Using Built-in Functions

li= [1,2,3,4,5,6]
li1=[]

for i in range(len(li)-1,-1,-1):
    li1.append(li[i])

print("reversed list is:",li1)   


# Write a program to find the second largest element in a list.

li=[1,2,3,4,5,2,7,10]
fmax=max(li)
smax=li[0]

for i in li:
    if i > smax and i!=fmax:
        smax=i

print("second largest element is:",smax)        


# Check if a list is palindrome

li=[1,2,1,3,4,5]

if li==li[::-1]:
    print("list is palindrome")
else :
    print("list is not palindrome")   


#Find Common Elements in Two Lists

li1=[1,2,3,4,5,6,7,8,9]
li2=[2,4,6,8,10,12,14,16,18]

li=[]

for i in li1:
    for j in li2:
        if i==j:
            li.append(i)

print(li)            


# Generate a list of squares for numbers in a range.
li=[]

for i in range(1,21):
    li.append(i*i)

print("list of squares is:",li)    

# Sort a list of tuples based on the second element.
# list_of_tuples = [(1, 3), (4, 2), (5, 1)]

list_of_tuples = [(1, 3), (4, 2), (5, 1)]

for i in range(0,len(list_of_tuples)):
    for j in range(i+1,len(list_of_tuples)):
        if list_of_tuples[i][1] > list_of_tuples[j][1]:
         list_of_tuples[i],list_of_tuples[j] = list_of_tuples[j],list_of_tuples[i]

print("sorted element in list is:",list_of_tuples)


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