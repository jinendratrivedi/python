# waf to print fibbonacci series upto n terms using recursion

def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

def gen_fib(length):
    print("finonacci series is:")
    for i in range(length):
        print(fib(i),end=" ")   

gen_fib(3)
