 # 3. TypeError
# Occurs when an operation is applied to an object of inappropriate type

try:
    a = 20
    b = "70" # exception raised here
    add = a + b
    print("Addition : ",add)
except TypeError as e :
    print("Type Error raised...")
    print("---> ",e)
    add = a + int(b)
print("Addition : ",add)
    