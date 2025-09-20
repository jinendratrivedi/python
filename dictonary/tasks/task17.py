# Write a program to create a dictionary and print its keys and values.
student = {
    "name" : "jinendra",
    "age" : 20,
    "city" : "palanpur",
    "pincode":385001
}
print(student)

# Write a program to add a key-value pair to a dictionary.
student["names"] = ("chetan" , "vatsal")
print(student)

# Write a program to remove a key from a dictionary.
student.pop("names")
print(student)

# Write a program to check if a key exists in a dictionary.

if "name" in student:
    print("yes")
else:
    print("no")

# Write a program to iterate through a dictionary and print all key-value pairs.
for key, value in student.items():
    print(key, value)

# Write a program to merge two dictionaries into one.
student = {
    "name" : "jinendra",
    "age" : 20,
    "city" : "palanpur",
}
student2={
    "name1":"chetan",
    "age2":20,
    "city3":"deesa"
}
marge={**student, **student2}
print(marge)

# Write a program to find the value of a specific key in a dictionary.
student = {
    "name" : "jinendra",
    "age" : 20,
    "city" : "palanpur",
    "pincode":385001
}
print(student["name"])

# Write a program to sort a dictionary by its keys.
student = {
    "name" : "jinendra",
    "age" : 20,
    "city" : "palanpur",
    "pincode":385001
}

for key in sorted(student):
 print(key, student[key])
