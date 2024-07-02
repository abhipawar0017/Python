class Employee:
    def __init__(self, name, age, salary, batch):
        self.name = name
        self.age = age
        self.salary = salary
        self.batch = batch

    def getInfo(self):
        print(f"The Name of Employee is {self.name}")
        print(f"The age of Employee is {self.age}")
        print(f"The Salary of Employee is {self.salary}")
        print(f"The Batch of Employee Working is {self.batch}")

abhi = Employee("Abhi Pawar", 18, 12345, "D3")
abhi.getInfo()
