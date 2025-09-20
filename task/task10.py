# take list from user append all element in list and print odd and even element sum  .

li= []
li1=int(input("enter the elements of list:"))

for i in range(li1):
    li.append(int(input("enter the number:")))

print("list:",li)

odd=0
even=0

for i in li:
    if i%2==0:
        even+=i
    else:
        odd +=i

print("even sum is:",even)
print("odd sum is",odd)            