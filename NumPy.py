import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print(arr)


# Operations
# print(arr + 10)       # Add 10 to each element -> [11 12 13 14 15]
# print(np.mean(arr))   # Average -> 3.0
# print(np.sum(arr))    # Sum -> 15


# --------
arr = np.arange(0, 10,2)
# print(arr)  # [0 2 4 6 8]

# ---------------
arr = np.array([10, 20, 30, 40])
# print(np.mean(arr))  # 25.0
# print(np.sum(arr))   # 100
# print(np.min(arr))   # 10
# print(np.max(arr))   # 40

# ----------------
arr = np.random.rand(3)
# print(arr)  # [0.52 0.74 0.25] (example)

arr = np.random.randint(3)
# print(arr)  # [0.52 0.74 0.25] (example)











import numpy as np

# 1. Create a 1D array of numbers from 0 to 9
arr1 = np.arange(10)
# print("1:", arr1)

# 2. Create a 2D array with ones
# arr2 = np.ones((3, 3))
# arr = np.ones((2, 2)) * 5
# print("2:\n", arr2)

# --------
# arr = np.ones(9)
# arr_reshaped = arr.reshape((3, 3))
# print(arr_reshaped)

# -------------
# weights = np.ones((3, 1))  # Initial weights for 3 features
# print("Weights:\n", weights)

# dummy_data = np.ones((5, 4))  # 5 samples, 4 features
# print("Dummy Data:\n", dummy_data)

# identity_plus_ones = np.identity(3) + np.ones((3, 3))
# print("Identity + Ones:\n", identity_plus_ones)

# 3. Create a 3x3 identity matrix
# arr3 = np.eye(3)
# print("3:\n", arr3)

# 4. Create an array of random numbers
arr4 = np.random.rand(5)
# print("4:", arr4)

# 5. Get the shape of an array
# print("5:", arr3.shape)

# 6. Reshape a 1D array into a 2D array
arr5 = np.arange(12).reshape(3, 4)
# print("6:\n", arr5)

# 7. Find the maximum value in an array
# print("7:", arr5.max())

# 8. Find the mean of an array
# print("8:", np.mean(arr5))

# 9. Find the standard deviation
# print("9:", np.std(arr5))

# 10. Perform element-wise addition
arr6 = np.array([1, 2, 3]) + np.array([4, 5, 6])
# print("10:", arr6)

# 11. Perform matrix multiplication
arr7 = np.dot(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]]))
# print("11:\n", arr7)

# 12. Get the transpose of a matrix
# print("12:\n", arr5.T)

# 13. Generate an array of even numbers from 2 to 20
arr8 = np.arange(2, 21, 2)
# print("13:", arr8)

# 14. Stack two arrays vertically
arr9 = np.vstack([arr1[:5], arr1[5:]])
# print("14:\n", arr9)

# 15. Stack two arrays horizontally
arr10 = np.hstack([arr1[:5].reshape(5, 1), arr1[5:].reshape(5, 1)])
# print("15:\n", arr10)

# 16. Find unique elements in an array
arr11 = np.array([1, 2, 2, 3, 4, 4, 5])
# print("16:", np.unique(arr11))

# 17. Replace all elements greater than 5 with 0
arr12 = np.array([2, 6, 8, 1, 4, 10])
arr12[arr12 > 5] = 0
# print("17:", arr12)

# 18. Find the index of the maximum element
# print("18:", np.argmax(arr12))

# 19. Find the cumulative sum
# print("19:", np.cumsum(arr1))

# 20. Check if any element is greater than 5
# print("20:", np.any(arr1 > 5))

# 21. Check if all elements are greater than 0
# print("21:", np.all(arr1 > 0))

# 22. Sort an array
arr13 = np.array([3, 1, 4, 1, 5, 9])
# print("22:", np.sort(arr13))

# 23. Compute the dot product of two vectors
# print("23:", np.dot(np.array([1, 2, 3]), np.array([4, 5, 6])))

# 24. Create a diagonal matrix
arr14 = np.diag([1, 2, 3])
# print("24:\n", arr14)

# 25. Generate a random integer array
arr15 = np.random.randint(1, 100, (3, 3))
# print("25:\n", arr15)
