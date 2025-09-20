# using function  :  with arg with return   prime

def is_prime(num):
    for i in range(2,num):
        
        if num%i==0:
            return "number is prime."
            break
        else:
            return"number is not prime."
            break
print(is_prime(9))
print(is_prime(10))