# waf that square all elemnts of a list
li1=[]
def square(li):
    for i in li:
        li1.append(i*i)
    print("list of squares is:",li1)

square([1,2,3,4,5])        

