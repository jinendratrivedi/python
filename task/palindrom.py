#wap to  enter a number and check whether it is palindrome or not without using string functions

num = int(input("Enter a number: "))
temp = num
rev = 0
while num > 0:
    a = num % 10
    rev = rev * 10 + a
    num = num // 10
    
if temp == rev:
    print("The number is palindrome!")      
else:
    print("The number isn't palindrome!")

