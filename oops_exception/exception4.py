class alivedead(Exception):
    pass

age = 50

try:
    if age < 100 and age > 0 :
        print("Eaception raising")
        raise alivedead("You are on earth and alive")
except alivedead as e:
    print(e)
else:
    print("you are in heaven")
