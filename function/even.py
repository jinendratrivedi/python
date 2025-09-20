#print even numbers using recursion

def even(n,i=0):
    if i>n:
        return
    
    if i%2==0:
        print(i,end=" ")
    return even(n,i+1)

even(10)
