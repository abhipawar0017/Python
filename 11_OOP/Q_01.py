class Employee:
    Company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product
    def getInfo(self):
        print(f"The Name of Employee is {self.name}")
        print(f"The Product of on Working is {self.product}")

abhi = Employee("Abhi", "Github")
abhi.getInfo()
abhi = Employee("Ram", "Skype")
abhi.getInfo()

