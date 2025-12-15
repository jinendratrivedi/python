# Python Program for cube sum of first n natural numbers

n = int(input("enter the number:"))

sum = 0

for i in range(1,n+1):
    sum += i**3

print("Cube sum of first", n)
print("natural numbers is:", sum)