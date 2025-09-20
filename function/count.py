# waf that counts uppercase , lowercase of a string

def count(s):
    u=0
    l=0
    for i in s:
        if i.upper()==i:
            u+=1
        elif i.lower()==i:
            l+=1

    print("uppercase:",u)
    print("lowercase:",l)

count("JinendraTRIVEDI")
count("hello")                    
  
