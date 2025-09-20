# An Employee class with work is inherited by Developer and Tester, who add code and test respectively. This enables code reuse with specialization under hierarchical inheritance, modeling a real-life employee structure


class Employee:
    def work1(self,name):
        self.name = name
        print(name,"is working.")


class Developer(Employee):
    def work2(self):
        print(self.name ,"is writing code.")


class Tester(Employee):
    def test(self):
        print(self.name , "is testing the application.")


emp1 = Developer()
emp2 = Tester()

emp1.work1("Vatsal")
emp1.work2()

emp2.work1("chetan")
emp2.test()
