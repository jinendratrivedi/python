#wap to input a string and calculate no of alphabets present in it

str=input("enter the string:")
count=0

for i in str:
    if i.isalpha():
        count+=1

print("total alphabets in string is:",count)        