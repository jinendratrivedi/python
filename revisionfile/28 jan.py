# reduce : if you have element  and  iteration  of all element and print the single value. 

from functools import reduce 

"""
l1=[1,2,3,4,5]

a= reduce(lambda x,y :x+y,l1)
print(a)
"""

# multiply of all element  : 
"""
l1=[1,2,3,4,5,6]

b=reduce(lambda x , y : x*y,l1)
print(b)

"""

# factorial  using reduce  : 

"""
n=int(input("enter the number  : "))
x=reduce(lambda x ,y :x * y,range(1,n+1))
print(x)
"""
# print n natural number sum  using reduce : 

"""n=int(input("enter the number  : "))
x=reduce(lambda x ,y :x + y,range(1,n+1))
print(x)
"""

# concate the string using  reduce : 
"""
input : l1=["i", "love","python"]
output : i love python.
"""
# l1=["i", "love","python"]
# a =reduce(lambda x,y : x + " " + y ,l1)
# print(a)

"""
match  : 
    c switch  

    switch  (choice) 
    case 1  
"""

a=int(input("enter the number  : "))
b= int(input("enter the number  : "))
print("welcome my calculator ")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modular")

choice=int(input("enter the choice : "))

match(choice):
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4 :
        print(a/b)
    case 5 :
        print(a%b)
    case _:
        print("invalid choice")

# ask user to enter the character and check it is vowel or consonant  or number or special character using match function..
