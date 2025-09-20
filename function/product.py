# waf to find cartesian product of 2 sets

s1={1,2}
s2={'a','b'}
s3=[]
def product(s1,s2,sum):
    
    for i in s1:
        for j in s2:
            sum+=i*j
            s3.append((i,j))
    print(s3)
product(s1,s2)