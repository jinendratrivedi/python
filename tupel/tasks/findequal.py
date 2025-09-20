# You are given a list of tuples where each tuple contains three integers: (x, y, z). 
# Find all tuples where the sum of any two numbers equals the third number.
data = [(1, 2, 3), (3, 5, 8), (4, 6, 10), (1, 1, 1), (2, 3, 5)]
res=[]
for i in data:
        if i[0]+i[1] == i[2] or i[1]+i[2]==i[0] or  i[0]+i[2]==i[1]:
            res.append(i)
                
print("list is:",res)                
                 