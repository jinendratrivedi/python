#  Write a program to swap keys and values in a dictionary.
#  Assume all values are unique.   
    
original = {'a': 1, 'b': 2, 'c': 3}
#output={1:"a",2:"b",3:"c"}
d={}

for key,values in original.items():
    d[values]=key

print(d)