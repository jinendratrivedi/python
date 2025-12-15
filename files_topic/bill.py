file = open("bill.txt", "w")

name = input("Enter name: ")


print("1. Pizza - 120")
print("2. Burger - 60")
print("3. Sandwich - 50")
print("4. Pasta - 80")
print("5. French Fries - 40")


grand_total = 0


for i in range(5):
    
    choice = int(input("Enter your choice: "))
    qty = int(input("Enter quantity: "))

    item = ""
    price = 0

    match choice:
        case 1:
            item = "Pizza"
            price = 120
        case 2:
            item = "Burger"
            price = 60
        case 3:
            item = "Sandwich"
            price = 50
        case 4:
            item = "Pasta"
            price = 80
        case 5:
            item = "French Fries"
            price = 40
        case _:
            print("Invalid choice!")
            continue   # skip to next loop

    total = price * qty
    grand_total += total

    file.write(f"Item: {item}\n")
    file.write(f"Qty: {qty}\n")         
    file.write(f"Price: {price}\n")        
    file.write(f"Total: {total}\n")     

# Discount
discount = 0
if grand_total >= 100:
    discount = grand_total * 0.10

final_amount = grand_total - discount

file.write(f"\nGrand Total: {grand_total}")
file.write(f"\nDiscount: {discount}")
file.write(f"\nFinal Amount: {final_amount}")

file.close()


