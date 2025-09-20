s1 = "my name is vatsal. "

print(s1[: : -1])

"""
task  : 1  print the pelindrome string using lambda function.
input : ["aba", "1221","maam","python"]
output : ["aba","1221","maam"]
"""

li1= ["aba", "1221","maam","python"]
li2=[]

for i in li1:
    if i==i[::-1]:
        li2.append(i)

print(li2)        

