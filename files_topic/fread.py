f= open("test.txt",'r')
print(f)

# txt = f.read()
# print(txt)

for char in f:
    print(f"-> {char}")