# NameError
 
# Occurs when using a variable that hasn’t been defined
try:
    a= 40
    print(a)
    print(aa)
except NameError as e:
    print(e)
    print("cnt use variable without defining")

