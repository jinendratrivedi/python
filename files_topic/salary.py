basic = int(input("enter the basic salary:"))

file = open("salary.txt","w")
file.write(str(basic))
file.close()




