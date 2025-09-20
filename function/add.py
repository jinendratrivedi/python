#waf to add 50 in an tuple

def add(t):
    l=list(t)
    l.append(50)
    
    print(tuple(l))
add((1,2,3,4))