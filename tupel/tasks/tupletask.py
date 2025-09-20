# Write a program to create a tuple and print its elements.

tup=(1,2,"abc",4,10.00)
print(tup)

# Write a program to find the index of an element in a tuple.

a=(1,2,"abc",4,10.00)

print(a[0])
print(a[3])

# Write a program to count the number of occurrences of an element in a tuple.

a=(1,2,3,"abc",10.00)

print("occurrences of an element in a tuple:",a.count(3))

# Write a program to convert a tuple into a list.

a=(1,2,3,"abc",10.00)
b=list(a)
print(b)    

# Write a program to find the length of a tuple.

a=(1,2,3,"abc",10.00)
print("length of a tuple:",len(a))

# Write a program to concatenate two tuples.

a=(1,2,3,"abc",10.00)
b=(4,5,6,"def",20.00)
c=a+b
print(c)

# Write a program to find the maximum and minimum elements in a tuple.

a=(1,2,3,4,5,6,7,8,9,10)
print("maximum element in a tuple:",max(a))
print("minimum element in a tuple:",min(a))

# Write a program to slice a tuple.

a=(1,2,3,4,5,6,7,8,9,10)
print(a[1:5])

# Write a program to check if an element exists in a tuple.

a=(1,2,3,4,5,6,7,8,9,10)
if 5 in a:
    print("yes exists in a tuple")
else:
    print("no exists in a tuple")

# Write a program to convert a tuple into a string.

a=(1,2,3,4,5,6,7,8,9,10)
b=str(a)
print(b)