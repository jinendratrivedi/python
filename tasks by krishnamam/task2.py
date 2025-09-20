num = int(input(("Enter the Number: ")))

def PosiNega():
    if num > 0:
        # print("Number is Positive")
        return "number is positive"
    else:
        # print("Number is Negative")
        return "number is negetive"

def EvenOdd(num):
    if num%2==0:
        print("Number is Even")
    else:
        print("Number is Odd")

def Prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        return "Prime"
    else:
        return "Not Prime"

print("1.Check for Positive OR Negative")
print("2.Check for Even OR Odd")
print("3.Check for Prime Number")
choice=int(input("Enter the Choice:"))

match choice:
    case 1:
        x=PosiNega()
        print(x)

    case 2:EvenOdd(num)
    case 3:Prime(num)
        