f = open("data.txt", "w")

total = 0
for i in range(10):
    n = int(input("Enter number: "))
    total += n
    f.write(str(n) + "\n")

f.close()

print("Sum =", total)
