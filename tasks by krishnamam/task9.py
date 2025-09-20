# 1. Get squares of numbers from 1 to 10.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in list1]
print("Squares of numbers from 1 to 10:", squares)

# 2. List all even numbers between 1 and 20.
list2 = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers between 1 and 20:", list2)

# 3. Convert all strings in a list to uppercase.
list3 = ["hello", "world", "python"]
uppercase_list = [x.upper() for x in list3]
print("Uppercase strings:", uppercase_list)

# 4. Filter numbers divisible by 3 from a list.
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
divisible_by_3 = [x for x in list4 if x % 3 == 0]
print("Numbers divisible by 3:", divisible_by_3)

# 5. Remove vowels from a given string.

str = "my name is jinendra trivedi"
cons = [char for char in str if char.lower() not in "aeiou"]
print("String without vowels:",cons)

# 6. Create a list of (number, square) tuples from 1 to 5.

list5 = [(x, x**2) for x in range(1, 6)]
print("List of (number, square) tuples:", list5)

# 7. Flatten a 2D list into a 1D list.

li = [[1, 2], [4, 5], [6, 7, 8]]

li1= [num for li in li for num in li]
print("Flattened list:", li1)

# 8. Replace negative numbers in a list with 0.
list6 = [1,2,3,-4,5,-6,7,-8,9]
list6 = [x if x > 0 else 0 for x in list6]
print("List with negative numbers replaced by 0:", list6)

# 9. Find common elements between two lists.
list7 = [1, 2, 3, 4, 5]
list8 = [4, 5, 6, 7, 8]

for i in list7:
    if i in list8:
        common_elements = i
        break
print("Common elements between two lists:", common_elements)

# 10. Extract digits from a string

str = "abc123def456"
digits = [char for char in str if char.isdigit()]
print("Digits extracted from string:", digits)

# 11. Reverse all strings in a list.

list9 = ["hello", "world", "python"]
li2= [x[::-1] for x in list9]
print("Reversed strings:", li2)

# 12. Get the length of each word in a list.

list10 = ["hello", "world", "python"]
lengths = [len(x) for x in list10]
print("Lengths of each word:", lengths)

# 13. Filter out all odd numbers from 0 to 19.
lisst11= [x for x in range(20) if x % 2 == 0]
print("even numbers from 0 to 19:", lisst11)

# 14. Remove empty strings from a list.
list12 = ["hello", "", "world", "", "python"]
list12 = [x for x in list12 if x]
print("List without empty strings:", list12)

# 15. Convert a list of temperatures from Celsius to Fahrenheit

list13 = [0, 20, 37, 100]
fahrenheit = [(x * 9/5) + 32 for x in list13]
print("Temperatures in Fahrenheit:", fahrenheit)

#16. Count vowels in a word.
word = "hello world"
vowels = "aeiou"
count = sum(1 for char in word if char.lower() in vowels)
print("Number of vowels in the word:", count)

# 17. Convert a list of numbers to strings.
del str 
lst= [1, 2, 3, 4, 5]
num_strs = [str(n) for n in lst]
print (num_strs)

# 18. Extract all capital letters from a sentence.
sentence = "Hello World! This is a Test."
capital = [char for char in sentence if char.isupper()]
print("Capital letters in the sentence:", capital)

# 19. Double each number in a list.

list15 = [1, 2, 3, 4, 5]
list15 = [x * 2 for x in list15]
print("Doubled numbers:", list15)

# 20. Filter names that are longer than 4 characters.
list16 = ["John", "Jane", "Sam", "Alexander"]
list16 = [x for x in list16 if len(x) > 4]
print("Names longer than 4 characters:", list16)

# 21. Square only the even numbers from a list.
list17 = [10,20,30,40,50]
list17 = [num**2 for num in list17 if num % 2 == 0]
print("square of even numbers:",list17)

# 22. Find all palindromes in a list of words.
lisst18 = ["mam", "hello", "racer", "wow", "python"]
palindromes = [word for word in lisst18 if word == word[::-1]]
print("Palindromes in the list:", palindromes)

# 23. Get ASCII values of characters in a string.
str = "hello"
words = [ord(char) for char in str]
print("ASCII values of characters:",words)

# 24. Multiply corresponding elements of two lists.
list19 = [1,2,3]
list20 = [4,5,6]
mul = [x * y for x, y in zip(list19, list20)]
print("Multiplied corresponding elements:", mul)

# 25. Convert binary strings to integers.

binary_strings = ["101","110","111","1000"] 
convert = [int(b,2)for b in binary_strings] 
print("Converted binary strings to integers:", convert) 

# 26. Remove duplicates from a list.
list21= [1, 2, 2, 3, 4, 4, 5]
list21 = list(set(list21))
print("List without duplicates:", list21)

# 27. Keep only alphabetic characters from a string.
str = "hello123"
alpha_chars = [char for char in str if char.isalpha()]
print("Alphabetic characters in the string:", alpha_chars)

# 28. Create a list of the first letters of each word.
sentance = "Hello World This is Python"
first_letters = [word[0] for word in sentance.split()]
print("First letters of each word:", first_letters)

# 29. Filter out falsy values (like 0, None, '') from a list.
list22 = [0, 1, None, 2, '', 3, 'hello']
list22 = [x for x in list22 if x] # This will remove all falsy values
print("List without falsy values:", list22) # This will remove all falsy values

# 30. Create a list of prime numbers less than 20.
prime=[]

for num in range(2, 20):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(num)
print("Prime numbers less than 20:", prime)