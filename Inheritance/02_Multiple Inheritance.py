class Employee:
    company = "Google"
    def show(self):
        print(f"The name of the Employee is {self.name} and company is {self.company}")

class coder:   # For multiple inheritance we can create another class and inherit it in the child class
    language = "Python"
    def printlanguages(self):
        print(f"out of all the languages here is your language: {self.language}")   


class Programmer(Employee, coder):    # For multiple inheritance we can inherit from multiple classes
    company = "Google Youtube"
    def show(self):
        print(f"The name is {self.company} and he is good with {self.language}")

a = Employee()
b = Programmer()
print(a.company, b.company) 
 
b.printlanguages()    # This will work because we have inherited the coder class in the Programmer class
