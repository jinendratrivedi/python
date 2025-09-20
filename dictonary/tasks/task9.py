# Write a program to find the key with the highest & lowest value in a dictionary.
 
d={
    "a":10,
    "b":50,
    "c":20
}

a= max(d,key=d.get)
print("Key with the highest value:",a)

b= min(d,key=d.get)
print("Key with the lowest value:",b)