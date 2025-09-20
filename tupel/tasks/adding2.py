#addition of  two tuppel

tuple1=(1,2,3,4)
tuple2=(5,6,7,8)
# li3=[]

# for i in range(len(li1)):
#     li3.append(li1[i]+li2[i])

# print("addition is:",tuple(li3))

a=tuple(a+b for a,b in zip(tuple1,tuple2))
print(a)
