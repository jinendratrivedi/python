#Program to accept the strings which contains all vowels
s = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0

for v in vowels:
    if v in s:
        count += 1

if count != 0:
    print("String contains vowels")
else:
    print("String does not contain vowels")

