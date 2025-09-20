class CheckPass(Exception):
    pass

password = "hello2345678kjhsdhdgkhdhf245346464dfhgjff"   

try:
    if len(password) < 8:
        raise CheckPass("Your password is too weak! Minimum 8 characters required.")
    elif len(password) > 32:
        raise CheckPass("Your password exceeds the maximum limit of 32 characters.")
    else:
        print("Your password is strong!")
except CheckPass as e:
    print(e)

print("Thank You...!!!")
