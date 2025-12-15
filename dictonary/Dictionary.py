dict = {
    # key : value :
    "name" : "Riya",
    'age' : 20,
    'city' : "Ahmedabad"
}

dict['email'] = "riya@gmail.com"

# print(dict)
# print(dict["name"])
# a[0]
# print(dict['age'])
# print(dict['email'])

# for key in dict:
#     print(key)

# for value in dict.values():
#     print(value)
    
# age = dict.pop('age')
# del dict['city']
# print("--> Poped : ",age)

# for key,value in dict.items():
#     print(key , " : ",value)
    
# dict2 = {}
# print(type(dict2))

for key in dict.keys():
    print(key)

print("name  : ",dict.get('name'))

# fname lname cno email city pincode course nameofUni 
