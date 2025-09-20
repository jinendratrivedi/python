#make a gradecard with 5 subjects  using match case and also calate the total and percentage eithout using functions


print("Enter the marks of 5 subjects")

a=int(input("Enter the marks of subject 1: "))
b=int(input("Enter the marks of subject 2: "))
c=int(input("Enter the marks of subject 3: "))
d=int(input("Enter the marks of subject 4: "))
e=int(input("Enter the marks of subject 5: "))


total=a+b+c+d+e
percentage=total/5

print("Total marks: ", total)
print("Percentage: ", percentage)

match(a,b,c,d,e):

    case(a,b,c,d,e) if percentage >= 90:
        print("Grade: A")
    case(a,b,c,d,e) if percentage >= 80:
        print("Grade: B")
    case(a,b,c,d,e) if percentage >= 70:
        print("Grade: C")
    case(a,b,c,d,e) if percentage >= 60:
        print("Grade: D")
    case(a,b,c,d,e) if percentage >= 50:
        print("Grade: E")
    case(a,b,c,d,e) if percentage < 50:
        print("Grade: F")
    case _:
        print("Invalid marks")






