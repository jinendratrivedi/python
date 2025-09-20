# waf to return factorial of a number

def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

print(fact(5))
