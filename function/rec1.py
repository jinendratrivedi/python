# waf to print name upto n times using recursion

def print_name(n):
    if n==0:
        return
    print("jinendra")
    print_name(n-1)

print_name(5)    