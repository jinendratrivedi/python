file = open("report.txt", "w")


fname = input("Enter first name: ")
lname = input("Enter last name: ")
rno = input("Enter roll number: ")
s1 = int(input("Enter marks for subject 1: "))
s2 = int(input("Enter marks for subject 2: "))
s3 = int(input("Enter marks for subject 3: "))
s4 = int(input("Enter marks for subject 4: "))
s5 = int(input("Enter marks for subject 5: "))

total = s1 + s2 + s3 + s4 + s5
avg = total / 5


if avg >= 90:
    grade = "A+"
elif avg >= 80:
    grade = "A"
elif avg >= 70:
    grade = "B"
elif avg >= 60:
    grade = "C"
elif avg >= 50:
    grade = "D"
else:
    grade = "Fail"

file.write(f"Name: {fname} {lname}\n")
file.write(f"Roll No: {rno}\n")
file.write(f"Marks: {s1}, {s2}, {s3}, {s4}, {s5}\n")
file.write(f"Total: {total}\n")
file.write(f"Average: {avg}\n")
file.write(f"Grade: {grade}\n")

file.close()