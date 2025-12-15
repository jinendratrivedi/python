import numpy as np

# one = np.array([1, 2, 3, 4, 5])

# one = np.ones((6))
# one = np.ones((2,4))

# one = np.ones((1,4))

# print("1D Array = \n", one)
# print(type(one))
# print("Size =", one.size)
# print("Shape =", one.shape)
# print("Dimension =", one.ndim)
# print("Item Size =", one.itemsize)
# print("Type,\n", one.astype(int))
# print("Type,\n", one.astype('float'))
# print("Type,\n", one.astype('str'), "\n")

# two = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
# two =  np.array([[1,2,3,4,5],[1,2,3,4,5]])
# print("2D Array,\n", two)
# print(type(two))
# print("Size =", two.size)
# print("Shape =", two.shape)
# print("Dimension =", two.ndim)
# print("Item Size =", two.itemsize)
# print("Type,\n", two.astype(int))
# print("Type,\n", two.astype('float'))
# print("Type,\n", two.astype('str'), "\n")

three = np.array([[[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],
                  [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]])
print("\n3D Array\n", three)
print(type(three))
print("Size =", three.size)
print("Shape =", three.shape)
print("Dimension =", three.ndim)
print("Item Size =", three.itemsize)
print("Type,\n", three.astype(int))
print("Type,\n", three.astype('float'))
print("Type,\n", three.astype('str'), "\n")

