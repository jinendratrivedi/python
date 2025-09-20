# concate the string using  reduce : 
"""
input : l1=["i", "love","python"]
output : i love python.
"""

from functools import reduce

l1=["i", "love","python"]

result = reduce(lambda a,b:a+" "+b,l1)+"."
print(result)
