# waf which give all possible subsets of a given set
    
s={7,8,9,1}

def subset(set):
    sub=[[]]

    for i in set:
        for j in sub[:]:
          sub.append([i]+j)
    print(s) 
subset(s)
subset({2,4,5})
