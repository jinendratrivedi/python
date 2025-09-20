import random as r1

array = list(range(1, 21))  # Numbers from 1 to 20

print(array)

input = int (input("enter the number between 1 to 20:"))


random_nubmer = r1.choice(array)
print(random_nubmer)

if input in array:
    print(f"The number {input} is present in the array.")
else:
     print(f"The number {input} is not present in the array.")


# user_input = int(input("Enter a number between 1 and 20: "))

# if user_input in array:
#     print(f"The number {user_input} is present in the array.")
# else:
#     print(f"The number {user_input} is not present in the array.")

# random_number = r1.randint(array)
# print(f"A random number from the array is: {random_number}")
