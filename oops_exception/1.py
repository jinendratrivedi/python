def dividebyzero():
    
    try:
        a=30/0
        print(a)
    except ZeroDivisionError as e:
        print("msg from obj e-->",e)
        print("denominator cut by zero..")
        
    a=10+20
    print("addition:-",a)
    
dividebyzero()        