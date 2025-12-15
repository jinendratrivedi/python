# Problem:
# A store sells multiple products, each with layered discount schemes including percentage discounts, flat reductions, conditional discounts for high-priced items, and festival or seasonal offers. Write a Python program that:
# 1. Allows the user to enter price and quantity for each product.
# 2. Automatically applies the appropriate layered discount for each item.
# 3. Calculates final price, savings per item, total payable amount, and total savings.
# 4. Generates a detailed itemized bill and stores it in a text file.
# Note: Clearly display each discount applied and the final amount for every product.


total_payable = 0
total_savings = 0
items = []

n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i+1)
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))

    original = price * qty
    discount = 0

    # Simple Layered Discounts
    if original >= 500:
        discount = discount + (original * 10 / 100)

    if original >= 1000:
        discount = discount + 50

    if original >= 2000:
        discount = discount + (original * 5 / 100)

    if original >= 1500:
        discount = discount + 100

    final = original - discount

    total_payable = total_payable + final
    total_savings = total_savings + discount

    items.append((name, original, discount, final))




print("\n====== BILL ======")

for item in items:
    print("\nProduct:", item[0])
    print("Original Price:", item[1])
    print("Total Discount:", item[2])
    print("Final Price:", item[3])

print("\nTotal Savings:", total_savings)
print("Total Payable Amount:", total_payable)


# ===== SAVE BILL TO FILE =====

file = open("bill.txt", "w")
for item in items:
    file.write("Product: " + item[0] + "\n")
    file.write("Original Price: " + str(item[1]) + "\n")
    file.write("Total Discount: " + str(item[2]) + "\n")
    file.write("Final Price: " + str(item[3]) + "\n")
    file.write("----------------------\n")

file.write("\nTotal Savings: " + str(total_savings))
file.write("\nTotal Payable Amount: " + str(total_payable))

file.close()


