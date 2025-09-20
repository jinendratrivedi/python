# Use recursion to print numbers from n to 1.

def print_num(n):
    if n==0:
        return
    print(n,end=" ")
    return print_num(n-1)

print_num(10)



