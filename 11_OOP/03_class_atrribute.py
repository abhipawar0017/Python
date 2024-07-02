class Employee:
    company = "MicroSoft"
    def info(self):
        print(f"The Name of Worker is {self.name}")
        print(f"The Salary of Employee is {self.salary}")
        print(f"The Company of Employee is {self.company}")

abhi = Employee()
abhi.name = "Abhi"
abhi.salary = "100k"
abhi.company = "Google"
abhi.info()
