# Write a Python program to remove an empty tuple(s) from a list of tuples.

# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

li = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
li1=[]

for i in li:
    if len(i)==0:
       pass
    else:
        li1.append(i)
       
print(li1)      


