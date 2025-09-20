# create a list with 5 elements
#     and give options
#     1. insert at end 
#     2. insert on given index 
#     3. remove by index 
#     4. remove by value

li=["apple", "banana",'cherry', 'date', 'elderberry']

print("Choose an option:")
print("1. Insert at End")
print("2. Insert on Given Index")
print("3. Remove by Index")
print("4. Remove by Value")

choice = int(input("Enter the choice number: "))

match choice:
    case 1:
        element = input("Enter the element to insert at end: ")
        li.append(element)
    case 2:
        index = int(input("enter the index:"))
        element = input("enter the element to insert given index:")
        li.insert(index,element)
    case 3:
        index = int(input("enter the element to remove by index:"))
        li.pop(index)
    case 4:
        element = input("enter the element to remove:")
        li.remove(element)
    case _:
         print("invalid choice")

print(li)                
