# Create a class "Programmer" for storing information of few programmers. Working at microsoft...
class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, address, experience):
        self.name = name
        self.salary = salary
        self.address = address
        self.experience = experience


p1 = Programmer("Vansh", 2000000, "Meerut", "8 years" )
print(p1.name, p1.salary, p1.address, p1.experience) 
a1 = Programmer("Aditiya", 2000000, "Meerut", "5 years" )
print(a1.name, a1.salary, a1.address, a1.experience) 