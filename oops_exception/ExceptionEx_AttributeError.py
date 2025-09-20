# AttributeError
   
# Occurs when trying to access an attribute/method that doesn’t exist
try:
    a = 90
    print(a)
    a.append(22)
except AttributeError as e:
    print(e)
    print("cnnt use any function which are not made for it")
 