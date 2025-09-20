# waf to make square of any number and by using square function make cube function

def square(num):

    return num **2

def cube(num):
     return square(num)*num

print("cube is:",cube(3))
