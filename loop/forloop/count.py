#wap to input a string and count no of alphabets,digits and special sym in it

str=input("enter the string:")
count=0

for i in str:
    if i.isalnum():
        count+=1
    else:
        count+=1    

print("total count of all char is:",count)        