# Write a Python script that prints prime numbers less than 20


for num in range(2, 20):
    flag = True  
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break  
    if flag:
        print(num)
         