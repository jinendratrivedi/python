# IndexError
 # Occurs when accessing an index that does not exist in a list
 
a = [11,22,33,44,55]
try:
    print(a[0])
    print(a[1])
    print(a[22])
except IndexError as e:
    print(e,"\n") 
    print("Array index out of bound..")
