class MiniBal(Exception):
    pass

bal = 6000

try:
    if bal < 5000:
        print("Eaception raising")
        raise MiniBal("Your bal should be more than 5000")
except MiniBal as e:
    print(e)
else:
    print("Bal is above minimum limit")

print("Thank You...!!!")


    