# waf to calculate sum of digits of a number
# 152 =>8

def sum_digit(num):
    sum=0
    while num>0:
        rem=num%10
        sum+=rem
        num=num//10
    return sum

print("sum of digits is:",sum_digit(152))