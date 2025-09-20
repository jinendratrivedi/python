# functions -> It is a block of code which is used to reduce redundancy
#           -> def keyword is used
# 1- no argument function

# def say_hi():
#     print("Hello")
#     print("Good Morning")

# say_hi()
# say_hi()

# 2- with argument function

# def add(a,b):
#     sum=a+b
#     print("sum is:",sum)

# c=100
# d=78

# add(c,d)
# add(10,20)

# num1= int(input("enter first number:"))
# num2= int(input("enter second number:"))
# add(num1,num2)


#*args -> arbitary arguments-> when we do know that how many argument will pass

# def add(*num):
#     print("sum is:",sum(num))

# add(10,20)
# add(10,20,30)
# add(12,34,56,78,90)    

#function with return type

#waf for area of circle-> pi*r*r
#waf for area of cylinder-> pi*r*r*h

# def area_circle(r):
#     return 3.14*r*r 

# print("area of circle is:",area_circle(5))

# def area_cylinder(r,h):
#     print(area_circle(r)*h)

# area_cylinder(2,5)    

#Recursion-> function calling itself repeatedly

# def fact(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return num*fact(num-1)
    
# print(fact(5))
# print(fact(1))
# print(fact(0))    