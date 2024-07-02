class Employee:
    company = "Microsoft"
    def info(self):
        print(f'''The Name of Company is {self.company} and Salary is {self.salary}''')
    
abhi = Employee()
abhi.company = "Google"
abhi.salary = "100k"
abhi.info()
