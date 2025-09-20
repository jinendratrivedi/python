#  KeyError
# Occurs when trying to access a non-existent key in a dictionary

a = {'name':"hello",
     "age":22}
try:
    print(a['name'])
    print(a["age"])
    print(a["ages"])
except KeyError as e :
    print(e)
    print("Undefined key")
