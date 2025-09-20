#Tuple ->It is collection of various datatype
#      -> It is rep in ( )
#      -> It is ordered , immutable and allow duplicates

# tupel = (2,3,"abc","def",True,78.89,"abc",3,2)
# print(tupel)
# print(type(tupel))
# print(len(tupel))

# # tuple[1]="dhdshf" --> generate the error because immutable
# # print(tuple)

# print(tupel[4])
# print(tupel[2:8])
# print(tupel[:5])
# print(tupel[4:])
# print(tupel[-5:-1])

# # adding perameter in slicing

# print(tupel[::3])

# # to create a single element in tupel

# tuple = ("abc",)
# print(type(tupel))

# #tupel consructor

li=[2,3,4,5,"a"]
a= tuple(li)

print(a)
print(type(a))

# methods of tupel

# tupel = (1,2,3,4,5,"abcdd",1,1,1,1,1)

# print("count is:",tupel.count(1)) # count the element of tupel
# print("index is:",tupel.index("abcdd")) #return index of element in tupel