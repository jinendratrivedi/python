# 1. Create a tuple with different data types.

# Creating a tuple
my_tuple = (1, "apple", 3.14, True)
print(my_tuple)

# 2. Problem: Access the first and last elements of a tuple.

my_tuple = (10, 20, 30, 40)

# Accessing elements
first_element = my_tuple[0]
last_element = my_tuple[-1]

print(f"First: {first_element}, Last: {last_element}")

# 3. Problem: Count the number of elements in a tuple.

my_tuple = (1, 2, 3, 4, 5)

# Length of the tuple
length = len(my_tuple)

print(f"Length: {length}")

# 4. Problem: Combine two tuples into one.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenating tuples
combined_tuple = tuple1 + tuple2

print(f"Combined Tuple: {combined_tuple}")

# 5. Problem: Check if a specific element exists in a tuple.

my_tuple = ("apple", "banana", "cherry")

# Check existence
exists = "banana" in my_tuple

print(f"Exists: {exists}")

# 6. Problem: Find the index of a specific element in a tuple.

my_tuple = ("a", "b", "c", "d")

# Finding the index
index = my_tuple.index("c")

print(f"Index of 'c': {index}")

# 7. Problem: Count how many times an element appears in a tuple.

my_tuple = (1, 2, 2, 3, 2, 4)

# Counting occurrences
count = my_tuple.count(2)

print(f"Count of 2: {count}")

# 8. Problem: Extract a slice from a tuple (e.g., first three elements).

my_tuple = (10, 20, 30, 40, 50)

# Slicing the tuple
sliced_tuple = my_tuple[:3]

print(f"Sliced Tuple: {sliced_tuple}")

# 9. Problem: Unpack the elements of a tuple into variables.

my_tuple = (1, "apple", 3.5)

# Unpacking
a, b, c = my_tuple

print(f"a: {a}, b: {b}, c: {c}")

# 10. Problem: Access an element in a nested tuple.

# Nested tuple
nested_tuple = (1, (2, 3), (4, (5, 6)))

# Accessing elements
inner_element = nested_tuple[2][1][1]

print(f"Accessed Element: {inner_element}")


# 14: Merge Two Sorted Lists into a Sorted List of Tuples
list1 = [1, 3, 5]
list2 = [2, 4, 6]

merged = sorted(zip(list1, list2))
print(merged)  

# Output: [(1, 2), (3, 4), (5, 6)]
