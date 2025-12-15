#  Convert Snake case to Pascal case

sc = input("Enter text:")
pc = sc.title().replace("_", "")
print("text is:",pc)