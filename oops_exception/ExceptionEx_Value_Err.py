# 2. ValueError
# Occurs when you pass an invalid value to a function (like converting "abc" to int)
num = int("123")
try:
    num = int("abc")
except ValueError as e:
    print("ValueError raised...\n",e)

print("Number is  : ",num)
