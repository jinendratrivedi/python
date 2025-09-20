#wap to create a dictionary using 2 list
key=[1,2,3]
value=["a","b","c"]

d={}

for i in range(len(key)):
    d[key[i]] = value[i]

print(d)    