class student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def __eq__(self, roll):
        return self.rollno == roll

s1 = student("raj",1)
s2 = student("ram",1)
s3 = student("jay",2)

if s1==s2:
    print("two values are equal")
else:
    print("two values are not equal")    
