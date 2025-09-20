import random as r

print(r.randint(1,11))
# random integer numbers between 1 to 11
# where 1 and 11 are included

print(r.random())
# random number btween 0 to 1

print(r.uniform(10,30))
# floating number between given range

lst = ['apple','banana','kiwi','coconut','orange','mango']

print(r.choice(lst))

print(r.shuffle(lst))
print(lst)

print(r.sample(lst,k=3))




