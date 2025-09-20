# find out all even numbers from a tuple and return a new tuple with the odd numbers.

tuple1 = (1,2,3,4,5,6,7,8,9,10)
tuple2 = tuple()

for i in tuple1:
    if i % 2 != 0:
        tuple2 += (i,) 
          
print(tuple2)

 