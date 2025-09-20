# waf to check that no is prime or not

def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
        else:
            print("prime")
            break  

is_prime(8)
is_prime(7)
