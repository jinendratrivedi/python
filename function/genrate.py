# waf to generate a dictionary which store value till a number
# in the form of x : x*x*x

def genrate(num):
    d={}
    for i in range(1,num+1):
        d[i]=i*i*i
        
    print(d)

genrate(5)

