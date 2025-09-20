# Combine two lists into a dictionary, where one list contains keys and the other contains values.
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d={}

for i in range(len(keys)):
    d[keys[i]]=values[i]

print("combined dictionary:",d)