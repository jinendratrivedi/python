def divideByZero():
    try:
        a = 30/0
        print(a)
    except ZeroDivisionError as e:   
        print("msg from object e : ---> ",e)
        print("Denominator cnt be Zero..")
    a = 80+ 90
    print("Addition : ",a)
divideByZero()
    
    