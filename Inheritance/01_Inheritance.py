class Employee:
    company = "Google"
    def show(self):
        print(f"The name of the Employee is {self.name} and company is {self.company}")

class Programmer(Employee):
    company = "Google Youtube"
    def show(self):
        print(f"The name is {self.name} and he is good with {self.language}")

a = Employee()
b = Programmer()
print(a.company, b.company)
