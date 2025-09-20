# Use recursion to print numbers from 1 to N.

def print_num(n):
    if n==0:
        return
    print_num(n-1)
    print(n,end=" ")

print_num(10)    
