# methods of dictonery

student = {
    "name" : "jinendra",
    "age" : 19,
    123 : "div",
    "sub": ("c","c++","python"),
    "is_adult" : True,
    "name1" : "chetan"

}

s1={
    "frds" :"vatsal",
    "bestfrds":"chetan"
}

a=student.copy()
print(a)
student.clear()
print(student)
# del student   --> delet to compleate dectionery
# print(student)

print(student["name"])
print(student.get("name"))
print(student.keys())
print(student.values())
print(student.items())
student.update({"abc":12})
print(student)
student.update(s1)
print(student)
student.pop("sub")
print(student)
student.popitem()
print(student)

