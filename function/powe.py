# Calculate a^b (power of a number) using recursion.

def power(a,b):
    if b==0:
        return 1
    return a* power(a,b-1)

print("power this number is:",power(2,3))   