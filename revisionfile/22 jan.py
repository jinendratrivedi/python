# lambda : 

"""
syntax : 

lambda arg :  expression  
"""

"""def sum(a,b):
    return a+b
print(sum(10,20))"""

"""x = lambda a,b : a+b 
print(x(10,20))
"""

# built  in function  : len min max sort sum 

"""a =lambda x : len(x)
print(a("my name jitu."))

b =lambda x : len(x)
c =lambda x : min(x)
d =lambda x : max(x)
e =lambda x : sorted(x)

print(a([1,20,3,0,4,5,6,7]))
print(c([1,20,3,0,4,5,6,7]))
print(d([1,20,3,0,4,5,6,7]))
print(e([1,20,3,0,4,5,6,7]))
"""
# if else using function : 
"""def big(x,y):
    if x>y:
        return x
    else:
        return y
print(big(100,20))
"""

# using lambda : 

"""a= lambda x,y : x if (x>y) else y
print(a(100,500))
"""
# string using slicing string rev  : 

s1 = "my name is vatsal. "

print(s1[: : -1])

"""
task  : 1  print the pelindrome string using lambda function.
input : ["aba", "1221","maam","python"]
output : ["aba","1221","maam"]
"""
"""
l1=["aba", "1221","maam","python"]
l2=[]
for i in l1: 
    if i ==i[::-1]:
        l2.append(i)
print(l2)
"""

# filter  : print the specific information you want .  

"""
jan  dec  :  fin tran 
jan  :  filter  ==> jan 

"""

"""
l1=[1,2,3,4,6,7,8,9,10,5]

a=list(filter(lambda x : x % 2 == 0,l1))
b=tuple(filter(lambda x : x % 2 == 1,l1))

print(a)
print(b)
"""
"""task  : 1  print the pelindrome string using lambda function.
input : ["aba", "1221","maam","python"]
output : ["aba","1221","maam"]
"""
# l1=["aba", "1221","maam","python"]
# a= list(filter(lambda x : x == x[: : -1],l1))
# print(a)

# map :it is given a new list . 
 
l1=[1,2,3,4,6,7,8,9,10,5]
"""
l2=[]
for i in l1:
    l2.append((i*5))
print(l2)
"""
#using map function : 
"""
a = list(map(lambda j : j *5,l1))
print(a)
"""

# reduce module  +  practice of function , bank  app , lambda map filter 