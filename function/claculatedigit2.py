# waf to calculate sum of digits of a number using recursion

def sum_digit(num):
    if num==0:
        return 0
    return num%10+sum_digit(num//10)

print("sum of digits is:",sum_digit(14235))