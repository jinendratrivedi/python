f = open("even.txt", "w")

for i in range(15):
    num = int(input("Enter number: "))
    if num % 2 == 0:
        f.write(f"{num}\n")

f.close()
