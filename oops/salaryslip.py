class Salary:
    def TotalSalary(self,basic_salary):
        self.basic_salary = basic_salary
        self.hra = (self.basic_salary*20)/100
        self.ta = (self.basic_salary*10)/100
        self.ma = (self.basic_salary*5)/100

        self.income_tax = (self.basic_salary*12)/100
        self.professional_tax = (self.basic_salary*2)/100

        self.basic_salary = self.basic_salary - (self.income_tax+self.professional_tax) 

        self.Total_Sal = self.basic_salary + self.ta + self.ma + self.hra   

    def SalaryData(self):

        print("HRA :",self.hra)
        print("TA :",self.ta)
        print("MA :",self.ma)
        print("Total Allowances: ",self.hra+self.ma+self.ta)

        print("Income Tax :",self.income_tax)
        print("Professional Tax :",self.professional_tax)
        print("Total Taxes :",self.income_tax+self.professional_tax)

        print("Basic Salary :",self.basic_salary)
        print("Total Salary :",self.Total_Sal)

sal = Salary()

bs = int(input("Enter Basic Salary :"))
sal.TotalSalary(bs)
sal.SalaryData() 