#find armstrong number using function and range

def armstrong(start,end):
    for i in range(start,end+1):
        sum = 0
        temp = i
        while i>0:
            digit = i%10
            sum+=digit**3
            i//=10
        if temp==sum:
            print(temp)

armstrong(1,10000)