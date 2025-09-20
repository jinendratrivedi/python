# waf to print table of number n using recursion

def table(n,i):
    if i>10:
        return
    print(n,"*",i,"=",n*i)
    table(n,i+1)    

table(5,1)          

