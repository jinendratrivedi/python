# waf to check that number is perfect no or not
# 6-> 1+2+3 =6 

def is_perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        print("perfect number")
    else:
        print("not perfect number")

is_perfect(6)
is_perfect(28)        