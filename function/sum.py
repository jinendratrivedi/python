# waf to find product and sum of all values of a dictionary

def sum(d):

    sum = 0
    prod = 1

    for i in d.values():
        prod*=i
        sum+=i

        
        
    print("Product:",prod)
    print("Sum:",sum)


d1={
    1:2,
    2:5
}        

d2={
    1:20,
    2:55  
}

sum(d1)
sum(d2)