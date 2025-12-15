# Python Program for Find remainder of array multiplication divided by n

arr = [100, 10, 5, 25, 35, 14]
n = 100
result = 1

for num in arr:
    result = (result*num)%n

print("reminder:",result)    

