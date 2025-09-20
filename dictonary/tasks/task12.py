#in a given dictionary swap the key with square of the value and value with key
d={2:"a", 4:"b",7:"c"}
#output={"a":4,"b":16,"c":49}d={}

d1={}
for key,values in d.items():
    d1[values]=key**2

print(d1)