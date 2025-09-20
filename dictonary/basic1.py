# Dictionary -> It is a datatype which store values in the form of key-value pair.
#             -> It is rep in { }
#             -> It is ordered , mutable , do not allow duplicates
#        NOTE -> list cannot be used as key in dictonary

student = {
    "name" : "jinendra",
    "age" : 19,
    123 : "div",
    ("c","c++","python") : "sub",
    "is_adult" : True,
    "name1" : "chetan"
}

student["age"] = 20
print(student)
student["friends"] = ("vatsal" , "cheatn")
print(student)