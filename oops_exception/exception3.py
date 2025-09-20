class stringlen(Exception):
    pass

str = "jinendra"

try:
    if  len(str) < 5:
        print("Exception raising")
        raise stringlen("Your string length should be more than 5")
except stringlen as e:
    print(e)
else:
    print("string length is above minimum limit")

print("Thank You...!!!")