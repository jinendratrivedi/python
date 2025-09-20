# Write a Python script to check whether a given key already exists in a dictionary.

d={
    "name":"abc",
    "age":12,
    "sub":["C","C++","Python"]
}
key= input("enter the key:")

if key in d:
    print("present")
else:
    print("not present")
        
